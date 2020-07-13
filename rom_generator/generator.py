import json
import types
import uuid
import time
import random
import os
import shutil
import ntpath
import copy
import logging
import argparse
import sys
from contextlib import contextmanager
from pathlib import Path
from PIL import Image
try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources

# Path hack for running modules within the rom_generator folder
sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath('..'))
import assets

# Utilities

@contextmanager
def cd(newdir):
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)

## Just some colors for fancy printing
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Make Project
scene_count = 0
generator_seed = "game boy generator"

def initializeGenerator(new_seed=None):
    scene_count = 0
    global generator_seed
    if not new_seed is None:
        generator_seed = new_seed
    random.seed(generator_seed)

base_gb_project = {
"settings": {},
"scenes": [],
"_version": "1.2.0",
"author": "Generator",
"name": "GenerationTest",
"variables": [],
"backgrounds": [],
"spriteSheets": [],
"music": [],
"customEvents": []
}

default_project_settings = {
        "showCollisions": True,
        "showConnections": True,
        "worldScrollX": 0,
        "worldScrollY": 0,
        "zoom": 100,
        "customColorsWhite": "E8F8E0",
        "customColorsLight": "B0F088",
        "customColorsDark": "509878",
        "customColorsBlack": "202850",
        "startX": 9,
        "startY": 9,
        "startDirection": "down",
        "startSceneId": "",
        "playerSpriteSheetId": "581d34d0-9591-4e6e-a609-1d94f203b0cd"
    }

### query current project for information
def getNumberOfScenes():
    return scene_count

scene_columns = 10
scene_spacing = 200

def assignSceneLocation(scene_number):
    x = (scene_number % scene_columns) * scene_spacing
    y = (scene_number // scene_columns) * scene_spacing
    return (x, y)

### Create a basic GBS element, with a unique ID
def makeElement():
    element = {}
    element["id"] = str(uuid.uuid4())
    return copy.deepcopy(element)

### Create a music element
def makeMusic(name, filename):
    element = makeElement()
    element["name"] = name
    element["filename"] = filename
    element["_v"] = int(round(time.time() * 1000.0)) # set creation time (for versioning?)
    return element

def getAssetFolder():
    with pkg_resources.path('assets', 'assets.txt') as asset_filename:
        return os.path.dirname(Path(asset_filename))
    raise FileNotFoundError("Asset folder not found")

def getImage(image_filename, image_type="sprites"):
    if os.path.basename(image_filename) != image_filename:
        dir_path = os.path.basename(os.path.dirname(image_filename))
        image_type = f"{image_type}.{dir_path}"
        image_filename = os.path.basename(image_filename)
    try:
        logging.info(f"Checking resources for {image_filename}: {pkg_resources.is_resource('assets', image_filename)}")
        with pkg_resources.path(f'assets.{image_type}', f"{image_filename}") as img_path:
            im = Image.open(img_path)
    except ValueError:
        import pdb; pdb.set_trace()
        f_name = os.path.basename(image_filename)
        f_type = os.path.basename(os.path.dirname(image_filename))
        return getImage(f_name, f_type)
    return im

def getImageInfo(image_filename, image_type="sprites"):
    """
    Get information about the image file from disk.
    image_type is a path that tells it where to look in the asset folder.
    """
    im = getImage(image_filename, image_type)
    res = {"pixel_width": im.size[0], "pixel_height": im.size[1], "image_format": im.format, "image_mode": im.mode}
    im.close()
    return res

## The way I decided to implement the API is that there are two kinds of
## functions that create stuff that will go into the project structure.
## The functions that start with 'make' create the element and return it.
## The functions that start with 'add' create the element and add it directly
## to the project. Mostly by calling the 'make' function to create the thing.
##

### A sprite sheet is a collection of images to display at the location of an actor or player.
### A sprite sheet can be one 16x16 static image...
### ...or can be animated by connecting multiple 16x16 frames horizontally in a single image.
def makeSpriteSheet(filename, name=None, type="static", frames=None):
    """
    Create a sprite sheet.
    """
    if name is None:
        name = filename
    element = makeElement()
    element["name"] = name
    element["type"] = type
    element["filename"] = filename
    element["_v"] = int(round(time.time() * 1000.0)) # set creation time (for versioning?)
    element["_generator_metadata"] = getImageInfo(filename)
    width = element["_generator_metadata"]["pixel_width"]
    height = element["_generator_metadata"]["pixel_height"]
    if (width % 16 != 0) or (height % 16 != 0):
        logging.warning(f"Sprite sheet {name} is not a multiple of 16: ({width},{height})")
    if frames is None:
        element["frames"] = width // 16
    else:
        element["frames"] = frames
    return element

def addSpriteSheet(project, filename, name=None, type="static", frames=None):
    """Create a sprite sheet and add it to the project."""
    element = makeSpriteSheet(filename, name, type, frames)
    project.spriteSheets.append(element)
    return element

### A background is a static image that players and actors traverse across on screen.
### GBStudio imports .png images in dimensions that are multiples of 8, breaks them into 8x8 pixels.
### The current released version of GBStudio has a maximum of 192 unique background tiles.
def makeBackground(filename, name=None, imageWidth=None, imageHeight=None, width=None, height=None):
    if name is None:
        name = filename
    element = makeElement()
    element["name"] = name
    element["width"] = width
    element["height"] = height
    element["imageWidth"] = imageWidth
    element["imageHeight"] = imageHeight
    element["filename"] = str(os.path.basename(Path(filename)))
    element["full_filepath"] = str(Path(filename))
    element["_v"] = int(round(time.time() * 1000.0))
    element["_generator_metadata"] = getImageInfo(filename, image_type="backgrounds")
    if imageWidth is None:
        element["imageWidth"] = element["_generator_metadata"]["pixel_width"]
    if imageHeight is None:
        element["imageHeight"] = element["_generator_metadata"]["pixel_height"]
    if width is None:
        element["width"] = element["_generator_metadata"]["pixel_width"] // 8
    if height is None:
        element["height"] = element["_generator_metadata"]["pixel_height"] // 8
    if (element["_generator_metadata"]["pixel_width"] % 8 != 0) or (element["_generator_metadata"]["pixel_height"] % 8 != 0):
        logging.warning(f"{filename} has a dimension that is not a multiple of 8")
    return element

### An actor is an object on the screen that the player can interact with.
def makeActor(sprite, x, y, movementType="static", animate=True):
    element = makeElement()
    element["spriteSheetId"] = sprite["id"]
    element["movementType"] = movementType
    element["moveSpeed"] = "1"
    element["animSpeed"] = "3"
    element["x"] = x
    element["y"] = y
    element["animate"] = animate
    return element

### A trigger causes a script to play when the player reaches the trigger's location.
def makeTrigger(trigger, x, y, width, height, script=[]):
  element = makeElement()
  element["x"] = x
  element["y"] = y
  element["width"] = width
  element["height"] = height
  element["script"] = script
  return element

def addSceneBackground(project, scene, background):
    print(scene)
    print(background)
    scene["backgroundId"] = background["id"]
    scene["width"] = background["width"]
    scene["height"] = background["height"]
    [print(s) for s in project.scenes if s["id"] == scene["id"]]
    return scene

def makeScene(name, background, width=None, height=None, x=None, y=None, collisions=[], actors=[], triggers=[]):
    """Creates a scene element.
    name is the scene name (arbitrary string)
    background is a background element (background data element).
    width and height are the size of the scene in tiles (optional, calculated from the background)
    x and y are the position of the scene in the GB Studio editor (optional)
    collisions is the collisions array (optional)
    actors is the array of actors in this scene (optional)
    triggers is the array of triggers in this scene (optional)
    Returns a data element in type 'scene'
    """
    global scene_count
    scene_count += 1
    element = makeElement()
    if name is None:
        element["name"] = f"Scene_{scene_count:04}"
    else:
        element["name"] = name
    element["backgroundId"] = background["id"]

    # width and height are the size of the scene in tiles.
    if not width is None:
        element["width"] = width
    else:
        element["width"] = background["width"]
    if not height is None:
        element["height"] = height
    else:
        element["height"] = background["height"]

    # x and y are the position of the scene in the editor window
    if not x is None:
        element["x"] = x
    else:
        element["x"] = assignSceneLocation(getNumberOfScenes())[0] # + background["imageWidth"]
    if not y is None:
        element["y"] = y
    else:
        element["y"] = assignSceneLocation(getNumberOfScenes())[1] # + background["imageHeight"]
    element["collisions"] = collisions
    element["actors"] = actors
    element["triggers"] = triggers
    return element

### Makes script to connect two scenes together.
def makeScriptConnectionToScene(target_scene, direction="right", location=None):
    destination_location = {
        "right": (1, target_scene["height"] // 2),
        "left":  (target_scene["width"] - 3, target_scene["height"] // 2),
        "up":    (target_scene["width"] // 2, target_scene["height"] - 2),
        "down":  (target_scene["width"] // 2, 1),
    }
    if location is None:
        location = destination_location[direction]
    script = []
    element = makeElement()
    element["command"] = "EVENT_SWITCH_SCENE"
    element["args"] = {
      "sceneId": target_scene["id"],
      "x": location[0],
      "y": location[1],
      "direction": direction,
      "fadeSpeed": "2"
    }
    script.append(element)
    element = makeElement()
    element["command"] = "EVENT_END"
    script.append(element)
    return script

reverse_direction = {"left": "right", "right": "left", "up": "down", "down": "up"}

### Adds trigger for scene connection.
def addTriggerConnectionToScene(project, scene, destination_scene, direction, doorway_sprite=None):
    source_location = {
        "right": (scene["width"] - 1, (scene["height"] // 2) - 1),
        "left":  (0, (scene["height"] // 2) - 1),
        "up":    (scene["width"] // 2, 0),
        "down":  (scene["width"] // 2, scene["height"] - 1)
    }
    trigger_size = {
    "right": (1, 2),
    "left":  (1, 2),
    "up":    (2, 1),
    "down":  (2, 2),
    }
    sign_offset = {
    "right": (0, 2),
    "left":  (0, 2),
    "up":    (2, 0),
    "down":  (2, 0),
    }
    trigger_connection = makeTrigger(f"walkTo{destination_scene['name']}", source_location[direction][0], source_location[direction][1], trigger_size[direction][0], trigger_size[direction][1], makeScriptConnectionToScene(destination_scene, direction))
    scene["triggers"].append(trigger_connection)

    if not doorway_sprite is None:
        actor_connector = makeActor(doorway_sprite, source_location[direction][0] + sign_offset[direction][0], (source_location[direction][1] + sign_offset[direction][1]) + 1, movementType="static")
        scene["actors"].append(actor_connector)
        actor_connector = makeActor(doorway_sprite, source_location[direction][0] - sign_offset[direction][0], (source_location[direction][1] - sign_offset[direction][1]) + 1, movementType="static")
        scene["actors"].append(actor_connector)

### Adds connections between scenes to the project.
def addSymmetricSceneConnections(project, scene, destination_scene, direction, doorway_sprite=None):
    addTriggerConnectionToScene(project, scene, destination_scene, direction, doorway_sprite)
    addTriggerConnectionToScene(project, destination_scene, scene, reverse_direction[direction], doorway_sprite)


### Writing the project to disk ###

def writeUIAssets(ui_asset_array, asset_path):
    ui_assets = []
    for ui_asset in ui_asset_array:
        temp_file = os.path.abspath(Path('temp').joinpath(ui_asset["asset_file_name"]))
        try:
            with pkg_resources.path(f'assets.{asset_path}', os.path.basename(ui_asset["asset_file_name"])) as img_path:
                copy_path = Path(img_path)
            logging.info(f"UI file copy: {copy_path} -> {temp_file}")
            os.makedirs(os.path.dirname(temp_file), exist_ok=True)
            shutil.copy2(copy_path, temp_file)
            ui_assets.append({"filename": ui_asset["filename"]})
        except FileNotFoundError as err:
            print(f"UI Asset File Missing: {err}")
            logging.warning(f"Asset File Missing: {err}")
            raise
    return ui_assets

# def findFileInAssets(assets_path, filename):
#     cur_directory = os.path.dirname(os.path.abspath(assets_path))
#     for root, dirs, files in os.walk(assets_path):
#         if filename in files:
#             return os.path.join(root, filename)
#     logging.error(f"File search for {filename} starting from {os.path.dirname(os.path.abspath(assets_path))} failed")
#     raise FileNotFoundError

def writeAssets(asset_array, output_path, sub_asset_path):
    output_assets_path = "assets/"
    Path(output_path).joinpath("assets/temp/").mkdir(parents=True, exist_ok=True)
    Path(output_path).joinpath(output_assets_path).mkdir(parents=True, exist_ok=True)
    for element in asset_array:
        f_name = element["filename"]
        add_path = []
        try:
            full_filepath = element["full_filepath"]
            rest = full_filepath
            while len(rest) > 0:
                rest = os.path.dirname(rest)
                last = str(os.path.basename(rest))
                if last == "assets":
                    break
                if len(last) > 0:
                    add_path.append(last)
            add_path.reverse()
        except KeyError:
            pass # doesn't have the full filepath
        print(f"writing {f_name}")
        logging.info(f"writing {f_name}")
        temp_file = os.path.abspath(Path(output_path).joinpath("assets/temp/scratch.file"))
        try:
            local_sub_asset_path = [sub_asset_path]
            local_sub_asset_path_str = sub_asset_path
            if (len(add_path)) > 0:
                local_sub_asset_path = add_path
                local_sub_asset_path_str = ".".join(add_path)
            with pkg_resources.path(f'assets.{local_sub_asset_path_str}', f_name) as img_path:
                copy_path = Path(img_path)
            if not os.path.isfile(copy_path):
                raise FileNotFoundError(f"Can't find {copy_path}")
            destination_path = Path(output_path).joinpath(output_assets_path).joinpath(*local_sub_asset_path).joinpath(f_name)
            Path(os.path.dirname(copy_path)).mkdir(parents=True, exist_ok=True)
            Path(os.path.dirname(destination_path)).mkdir(parents=True, exist_ok=True)
            logging.info(f"Asset file copy: {copy_path} -> {temp_file} -> {destination_path}")
            new_file = shutil.copy2(copy_path, temp_file)
            os.replace(new_file, destination_path)
            logging.info(f"Wrote {os.path.abspath(destination_path)}")
        except FileNotFoundError as err:
            print(f"Asset File Missing for writeAssets(): {err}")
            logging.warning(f"Asset File Missing: {err}")
            raise
    if not shutil.rmtree.avoids_symlink_attacks:
        logging.info("Temp directory deletion potentially vulnerable to symlink attacks.")
    shutil.rmtree(Path(output_path).joinpath("assets/temp/"))

def writeProjectToDisk(gb_project, filename="test.gbsproj", output_path="gbprojects/projects/"):
    # Write project to JSON
    output_path = os.path.abspath(Path(os.path.dirname(__file__)).joinpath('..').joinpath(output_path))
    logging.info(f"writeProjectToDisk: {bcolors.OKGREEN}{os.path.abspath(output_path)}{bcolors.ENDC}")
    logging.info(f"Writing {filename} project file...")
    gb_project_without_ui_elements = copy.deepcopy(gb_project)
    gb_project_without_ui_elements.ui = None
    generated_project = json.dumps(gb_project_without_ui_elements.__dict__, indent=4)
    Path(output_path).mkdir(parents=True, exist_ok=True)
    with open(Path(output_path).joinpath(filename), "w") as wfile:
        wfile.write(generated_project)

    # Copy assets to projects
    print("*** Writing assets ***")
    writeAssets(gb_project.spriteSheets, output_path, "sprites")
    writeAssets(gb_project.music,        output_path, "music")
    writeAssets(gb_project.backgrounds,  output_path, "backgrounds")
    ui_asset_array = writeUIAssets(gb_project.ui, "ui")
    writeAssets(ui_asset_array,          output_path, "ui")

    print(f"Wrote project to {os.path.abspath(output_path)}")

def makeBasicProject():
    project = types.SimpleNamespace(**base_gb_project)
    project.settings = default_project_settings.copy()
    project.ui = [
    {"filename": "ascii.png",  "asset_file_name": "original/ascii.png"},
    {"filename": "cursor.png", "asset_file_name": "original/cursor.png"},
    {"filename": "emotes.png", "asset_file_name": "original/emotes.png"},
    {"filename": "frame.png",  "asset_file_name": "original/frame.png"}]
    return project

#makes a border of collisions around a scene
def makeColBorder(scenex):
    wid = scenex["width"]
    hei = scenex["height"]
    tilenum = wid * hei
    work = [False] * tilenum
    for x in range(0, wid-1):
        work[x] = True
    y = 0 + wid
    while y < (wid * hei) - wid:
        work[y] = True
        y = y + wid
    z = wid - 1
    while z < (wid * hei):
        work[z] = True
        z = z + wid
    w = (wid * hei) - wid
    while w < (wid * hei):
        work[w] = True
        w = w + 1
    bytez = wid * hei
    cc = []
    max = 0
    while max < wid * hei - 1:
        g = 1
        j = " "
        while g < 9:
            if work[max] == True:
                j = j + "1"
            elif work[max] == False:
                j = j + "0"
            max = max + 1
            g = g + 1
        jnum = int(j, 2)
        cc.insert(0, jnum)
    scenex["collisions"] = cc

def makeCol(array01, scene01):
    """
    takes in 1D array (later 2D array) of 0s and 1s, puts in collisions accordingly
    """
    wid = scene01["width"]
    hei = scene01["height"]
    cc = []
    max = 0
    while max < wid * hei - 1:
        g = 1
        j = " "
        while g < 9:
            if array01[max] == 1:
                j = j + "1"
            elif array01[max] == 0:
                j = j + "0"
            max = max + 1
            g = g + 1
        jnum = int(j, 2)
        cc.insert(0, jnum)
    scene01["collisions"] = cc

def createExampleProject():
    # Set up a barebones project
    project = makeBasicProject()

    # Create sprite sheet for the player sprite
    player_sprite_sheet = makeSpriteSheet("actor_animated.png", "actor_animated", "actor_animated")
    project.spriteSheets.append(player_sprite_sheet)
    project.settings["playerSpriteSheetId"] = player_sprite_sheet["id"]

    # add a sprite we can use for the rocks
    a_rock_sprite = makeSpriteSheet("rock.png", "rock", "static")
    project.spriteSheets.append(a_rock_sprite)

    # Add a background image
    default_bkg = makeBackground("placeholder.png", "placeholder")
    project.backgrounds.append(default_bkg)

    # Get information about the background
    bkg_x = default_bkg["imageWidth"]
    bkg_y = default_bkg["imageHeight"]
    bkg_width = default_bkg["width"]
    bkg_height = default_bkg["height"]

    # add a sprite to indicate the location of a doorway
    # a better way to do this in the actual levels is to alter the background image instead
    doorway_sprite = makeSpriteSheet("tower.png", "tower", "static")
    project.spriteSheets.append(doorway_sprite)

    # We want to create a bunch of scenes.
    # Here I'm just creating them randomly.
    number_of_scenes_to_make = 7
    for make_scene_num in range(number_of_scenes_to_make):
        # Create a scene
        a_scene = copy.deepcopy(makeScene(f"Scene {make_scene_num}", default_bkg))
        # Create an actor
        for x in range(8): # Maximum number of actors in GB Studio is 9
            actor_x = random.randint(1,(bkg_width-3)) # Second value subtracted by 1 to keep sprite within bounds of the screen
            actor_y = random.randint(2,bkg_height-2) # First value added by 1 to keep sprite within bounds of the screen
            example_rock = makeActor(a_rock_sprite, actor_x, actor_y)
            a_scene["actors"].append(example_rock)
        # Add scene to project
        project.scenes.append(copy.deepcopy(a_scene))

    # Add some connections between the scenes.
    # This just throws down a bunch of random connections and tries to
    # make sure that they don't overlap
    scene_connections_translations = {"right":0, "left":1, "up":2, "down":3}
    scene_connections = [[True, True, True, True] for n in range(number_of_scenes_to_make)]
    for y in range(number_of_scenes_to_make):
        for attempts in range(3):
            other_scene = random.randint(0, number_of_scenes_to_make - 2)
            if other_scene >= y:
                other_scene += 1
            chosen_direction = random.choice(["right", "left", "up", "down"])
            if scene_connections[y][scene_connections_translations[chosen_direction]]:
                if scene_connections[other_scene][scene_connections_translations[reverse_direction[chosen_direction]]]:
                    scene_connections[y][scene_connections_translations[chosen_direction]] = False
                    scene_connections[other_scene][scene_connections_translations[reverse_direction[chosen_direction]]] = False
                    addSymmetricSceneConnections(project, project.scenes[y], project.scenes[other_scene], chosen_direction, doorway_sprite)
                    break

    # Add some music
    project.music.append(makeMusic("template", "template.mod"))

    # Set the starting scene
    project.settings["startSceneId"] = project.scenes[0]["id"]

    return project


### Run the generator
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate a Game Boy ROM via a GB Studio project file.")
    parser.add_argument('--destination', '-d', type=str, help="destination folder name", default="../gbprojects/projects3/")
    args = parser.parse_args()
    initializeGenerator()
    project = createExampleProject()
    writeProjectToDisk(project, output_path = args.destination)

    if args.destination == "../gbprojects/projects/":
        print(f"{bcolors.WARNING}NOTE: Used default output directory, change with the -d flag{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}See generate.py --help for more options{bcolors.ENDC}")
