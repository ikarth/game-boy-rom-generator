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
from pathlib import Path
from PIL import Image

# Utilities

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

# Ordinarily, global variables are bad things. But these aren't global variables
# in the classic sense: all variable in Python exist in a scope. In this case,
# these are localized to the module. You can think of the entire module as
# being a little bit like a class with one instance in Java, encapsulating a
# bunch of functions and variables.
main_asset_folder = "../assets/"

scene_count = 0
generator_seed = "game boy generator"

def initializeGenerator(asset_folder = "../assets/", new_seed=None):
    global main_asset_folder
    global scene_count
    main_asset_folder = asset_folder
    print(main_asset_folder)
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



def getImage(image_filename, image_type="sprites"):
    print(Path(main_asset_folder).joinpath(image_type, image_filename))
    im = Image.open(Path(main_asset_folder).joinpath(image_type, image_filename))
    return im

def getImageInfo(image_filename, image_type="sprites"):
    """
    Get information about the image file from disk.
    image_type is a path that tells it where to look in the asset folder.
    """
    im = getImage(image_filename, image_type)
    return {"pixel_width": im.size[0], "pixel_height": im.size[1], "image_format": im.format, "image_mode": im.mode}

## The way I decided to implment the API is that there are two kinds of
## functions that create stuff that will go into the project structure.
## The functions that start with 'make' create the element and return it.
## The functions that start with 'add' create the element and add it directly
## to the project. Mostly by calling the 'make' function to create the thing.
##


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

def makeBackground(filename, name=None, imageWidth=None, imageHeight=None, width=None, height=None):
    if name is None:
        name = filename
    element = makeElement()
    element["name"] = name
    element["width"] = width
    element["height"] = height
    element["imageWidth"] = imageWidth
    element["imageHeight"] = imageHeight
    element["filename"] = filename
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
        logging.warning(f"{filename} has a dimention that is not a multiple of 8")
    return element

def makeActor(sprite, x, y, movementType="static"):
    element = makeElement()
    element["spriteSheetId"] = sprite["id"]
    element["movementType"] = movementType
    element["moveSpeed"] = "1"
    element["animSpeed"] = "3"
    element["x"] = x
    element["y"] = y
    return element

def makeTrigger(trigger, x, y, width, height, script=[]):
  element = makeElement()
  element["x"] = x
  element["y"] = y
  element["width"] = width
  element["height"] = height
  element["script"] = script
  return element

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
        actor_connector = Actor(doorway_sprite, source_location[direction][0] + sign_offset[direction][0], (source_location[direction][1] + sign_offset[direction][1]) + 1, movementType="static")
        scene["actors"].append(actor_connector)
        actor_connector = makeActor(doorway_sprite, source_location[direction][0] - sign_offset[direction][0], (source_location[direction][1] - sign_offset[direction][1]) + 1, movementType="static")
        scene["actors"].append(actor_connector)


def addSymmetricSceneConnections(project, scene, destination_scene, direction, doorway_sprite=None):
    addTriggerConnectionToScene(project, scene, destination_scene, direction, doorway_sprite)
    addTriggerConnectionToScene(project, destination_scene, scene, reverse_direction[direction], doorway_sprite)


### Writing the project to disk ###

def writeUIAssets(ui_asset_array, asset_path):
    ui_assets = []
    for ui_asset in ui_asset_array:
        temp_file = Path("assets/temp/ui/" + ui_asset["filename"])
        try:
            copy_path = os.path.abspath(Path(asset_path).joinpath(ui_asset["asset_file_name"]))
            logging.info(f"UI file copy: {copy_path} -> {temp_file}")
            os.makedirs(os.path.dirname(temp_file), exist_ok=True)
            shutil.copy2(copy_path, temp_file)
            ui_assets.append({"filename": ui_asset["filename"]})
        except FileNotFoundError as err:
            print(f"UI Asset File Missing: {err}")
            logging.warning(f"Asset File Missing: {err}")
    return ui_assets


def writeAssets(asset_array, output_path, asset_path):
    Path(output_path + "assets/temp/").mkdir(parents=True, exist_ok=True)
    Path(output_path).joinpath(asset_path).mkdir(parents=True, exist_ok=True)
    for element in asset_array:
        f_name = element["filename"]
        print(f_name)
        temp_file = os.path.abspath(Path(output_path + "assets/temp/scratch.file"))
        try:
            #copy_path = os.path.abspath(Path("../").joinpath(Path(asset_path).joinpath(f_name)))
            copy_path = os.path.abspath(Path(asset_path).joinpath(f_name))
            destination_path = Path(output_path).joinpath(asset_path, f_name)
            logging.info(f"Asset file copy: {copy_path} -> {temp_file} -> {destination_path}")
            shutil.copy2(copy_path, temp_file)
            os.replace(Path(temp_file), destination_path)
            logging.info(f"Wrote {destination_path}")
        except FileNotFoundError as err:
            print(f"Asset File Missing for writeAssets(): {err}")
            logging.warning(f"Asset File Missing: {err}")
    if not shutil.rmtree.avoids_symlink_attacks:
        logging.info("Temp directory deletion potentially vulnerable to symlink attacks.")
    shutil.rmtree(Path(output_path + "assets/temp/"))

def writeProjectToDisk(gb_project, filename="test.gbsproj", output_path="../gbprojects/projects/", assets_path ="../assets/"):
    # Write project to JSON
    logging.info(f"Writing {filename} project file...")
    gb_project_without_ui_elements = copy.deepcopy(gb_project)
    print(gb_project)
    gb_project_without_ui_elements.ui = None
    generated_project = json.dumps(gb_project_without_ui_elements.__dict__, indent=4)
    print(generated_project)
    Path(output_path).mkdir(parents=True, exist_ok=True)
    with open(f"{output_path}{filename}", "w") as wfile:
        wfile.write(generated_project)

    # Copy assets to projects
    print("*** Writing assets ***")
    writeAssets(gb_project.spriteSheets, output_path, Path(assets_path + "sprites/"))
    writeAssets(gb_project.music, output_path, Path(assets_path + "music/"))
    writeAssets(gb_project.backgrounds, output_path, Path(assets_path + "backgrounds/"))
    ui_asset_array = writeUIAssets(gb_project.ui, Path(assets_path + "ui/"))
    writeAssets(ui_asset_array, output_path, Path(assets_path + "ui/"))

def makeBasicProject():
    project = types.SimpleNamespace(**base_gb_project)
    project.settings = default_project_settings.copy()
    project.ui = [
    {"filename": "ascii.png", "asset_file_name": "original/ascii.png"},
    {"filename": "cursor.png", "asset_file_name": "original/cursor.png"},
    {"filename": "emotes.png", "asset_file_name": "original/emotes.png"},
    {"filename": "frame.png", "asset_file_name": "original/frame.png"}]
    return project

# def createWithCallback(callback_func):
#     # Set up a barebones project
#     project = makeBasicProject()
#
#     # Add some music
#     project.music.append(makeMusic("template", "template.mod"))
#
#     # Create sprite sheets
#     player_sprite_sheet = makeSpriteSheet("actor_animated", "actor_animated", "actor_animated.png")
#
#     # Set the starting scene and player sprite
#     project.settings["startSceneId"] = project.scenes[0]["id"]
#     project.settings["playerSpriteSheetId"] = player_sprite_sheet["id"]
#
#     instructions = callback_func(project)
#
#     write_project_to_disk(project, output_path=main_project_output_path)
#
#


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
        for x in range(2): # Maximum number of actors in GB Studio is 9
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
    parser.add_argument('--destination', '-d', type=str, help="destination folder name", default="../gbprojects/projects2/")
    parser.add_argument('--assets', '-a', type=str, help="asset folder name", default="../assets/")
    parser.add_argument('--subfolder', '-s', type=bool, help="asset folder name", default=False)
    args = parser.parse_args()
    initializeGenerator(asset_folder=args.assets)
    project = createExampleProject()
    writeProjectToDisk(project, output_path = args.destination, assets_path=args.assets)
    if args.destination == "../gbprojects/projects/":
        print(f"{bcolors.WARNING}NOTE: Used default output directory, change with the -d flag{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}See generate.py --help for more options{bcolors.ENDC}")












def end():
    element = makeElement()
    element["commands"] = "EVENT_END"
    element["args"] = {
    }
    return element

def stop():
    element = makeElement()
    element["commands"] = "EVENT_STOP"
    element["args"] = {
    }
    return element

def wait(time = "0.5"):
    element = makeElement()
    element["commands"] = "EVENT_WAIT"
    element["args"] = {
        "time": time,
    }
    return element

def switchScene(sceneId = "498cfdcf-3000-453f-9b52-fe5d8d81cac2", x = "7", y = "6", direction = "", fadeSpeed = "2"):
    element = makeElement()
    element["commands"] = "EVENT_SWITCH_SCENE"
    element["args"] = {
        "sceneId": sceneId,
        "x": x,
        "y": y,
        "direction": direction,
        "fadeSpeed": fadeSpeed,
    }
    return element

def startBattle():
    element = makeElement()
    element["commands"] = "EVENT_START_BATTLE"
    element["args"] = {
    }
    return element

def returnToTitle():
    element = makeElement()
    element["commands"] = "EVENT_RETURN_TO_TITLE"
    element["args"] = {
    }
    return element

def scenePushState():
    element = makeElement()
    element["commands"] = "EVENT_SCENE_PUSH_STATE"
    element["args"] = {
    }
    return element

def scenePopState(fadeSpeed = "2"):
    element = makeElement()
    element["commands"] = "EVENT_SCENE_POP_STATE"
    element["args"] = {
        "fadeSpeed": fadeSpeed,
    }
    return element

def sceneResetState():
    element = makeElement()
    element["commands"] = "EVENT_SCENE_RESET_STATE"
    element["args"] = {
    }
    return element

def scenePopAllState(fadeSpeed = "2"):
    element = makeElement()
    element["commands"] = "EVENT_SCENE_POP_ALL_STATE"
    element["args"] = {
        "fadeSpeed": fadeSpeed,
    }
    return element

def loadData():
    element = makeElement()
    element["commands"] = "EVENT_LOAD_DATA"
    element["args"] = {
    }
    return element

def saveData():
    element = makeElement()
    element["commands"] = "EVENT_SAVE_DATA"
    element["args"] = {
    }
    return element

def clearData():
    element = makeElement()
    element["commands"] = "EVENT_CLEAR_DATA"
    element["args"] = {
    }
    return element

def ifTrue(variable = "L0", __collapseElse = "False", trueCommands = [], falseCommands = []):
    element = makeElement()
    element["commands"] = "EVENT_IF_TRUE"
    element["args"] = {
        "variable": variable,
        "__collapseElse": __collapseElse,
    }
    trueCommands.add(end())
    falseCommands.add(end())
    element["children"] = {
        "true": trueCommands,
        "false": falseCommands
    }
    return element

def ifFalse(variable = "L0", __collapseElse = "False", trueCommands = [], falseCommands = []):
    element = makeElement()
    element["commands"] = "EVENT_IF_FALSE"
    element["args"] = {
        "variable": variable,
        "__collapseElse": __collapseElse,
    }
    trueCommands.add(end())
    falseCommands.add(end())
    element["children"] = {
        "true": trueCommands,
        "false": falseCommands
    }
    return element

def ifValue(variable = "L3", operator = ">", comparator = "2", __collapseElse = "False", trueCommands = [], falseCommands = []):
    element = makeElement()
    element["commands"] = "EVENT_IF_VALUE"
    element["args"] = {
        "variable": variable,
        "operator": operator,
        "comparator": comparator,
        "__collapseElse": __collapseElse,
    }
    trueCommands.add(end())
    falseCommands.add(end())
    element["children"] = {
        "true": trueCommands,
        "false": falseCommands
    }
    return element

def ifValueCompare():
    element = makeElement()
    element["commands"] = "EVENT_IF_VALUE_COMPARE"
    element["args"] = {
    }
    return element

def ifInput(input = "['a', 'b']", __collapseElse = "False", trueCommands = [], falseCommands = []):
    element = makeElement()
    element["commands"] = "EVENT_IF_INPUT"
    element["args"] = {
        "input": input,
        "__collapseElse": __collapseElse,
    }
    trueCommands.add(end())
    falseCommands.add(end())
    element["children"] = {
        "true": trueCommands,
        "false": falseCommands
    }
    return element

def ifActorDirection(actorId = "player", direction = "up", __collapseElse = "False", trueCommands = [], falseCommands = []):
    element = makeElement()
    element["commands"] = "EVENT_IF_ACTOR_DIRECTION"
    element["args"] = {
        "actorId": actorId,
        "direction": direction,
        "__collapseElse": __collapseElse,
    }
    trueCommands.add(end())
    falseCommands.add(end())
    element["children"] = {
        "true": trueCommands,
        "false": falseCommands
    }
    return element

def ifSavedData(__collapseElse = "False", trueCommands = [], falseCommands = []):
    element = makeElement()
    element["commands"] = "EVENT_IF_SAVED_DATA"
    element["args"] = {
        "__collapseElse": __collapseElse,
    }
    trueCommands.add(end())
    falseCommands.add(end())
    element["children"] = {
        "true": trueCommands,
        "false": falseCommands
    }
    return element

def ifActorAtPosition(actorId = "player", x = "0", y = "0", __collapseElse = "False", trueCommands = [], falseCommands = []):
    element = makeElement()
    element["commands"] = "EVENT_IF_ACTOR_AT_POSITION"
    element["args"] = {
        "actorId": actorId,
        "x": x,
        "y": y,
        "__collapseElse": __collapseElse,
    }
    trueCommands.add(end())
    falseCommands.add(end())
    element["children"] = {
        "true": trueCommands,
        "false": falseCommands
    }
    return element

def setTrue(variable = "L0"):
    element = makeElement()
    element["commands"] = "EVENT_SET_TRUE"
    element["args"] = {
        "variable": variable,
    }
    return element

def setFalse(variable = "L0"):
    element = makeElement()
    element["commands"] = "EVENT_SET_FALSE"
    element["args"] = {
        "variable": variable,
    }
    return element

def choice(variable = "L0", trueText = "", falseText = ""):
    element = makeElement()
    element["commands"] = "EVENT_CHOICE"
    element["args"] = {
        "variable": variable,
        "trueText": trueText,
        "falseText": falseText,
    }
    return element

def resetVariables():
    element = makeElement()
    element["commands"] = "EVENT_RESET_VARIABLES"
    element["args"] = {
    }
    return element

def loop(loopCommand):
    element = makeElement()
    element["commands"] = "EVENT_LOOP"
    element["args"] = {
    }
    loopCommand.add(end())
    element["children"] = {
        "true": loopCommand
    }
    return element

def group(groupCommands):
    element = makeElement()
    element["commands"] = "EVENT_GROUP"
    element["args"] = {
    }
    groupCommands.add(end())
    element["children"] = {
        "true": groupCommands
    }
    return element

def menu(variable = "L0", items = "2", option1 = "", option2 = "", option3 = "", option4 = "", option5 = "", option6 = "", option7 = "", option8 = "", cancelOnB = "True", layout = "dialogue"):
    element = makeElement()
    element["commands"] = "EVENT_MENU"
    element["args"] = {
        "variable": variable,
        "items": items,
        "option1": option1,
        "option2": option2,
        "option3": option3,
        "option4": option4,
        "option5": option5,
        "option6": option6,
        "option7": option7,
        "option8": option8,
        "cancelOnB": cancelOnB,
        "layout": layout,
    }
    return element

def comment(text = ""):
    element = makeElement()
    element["commands"] = "EVENT_COMMENT"
    element["args"] = {
        "text": text,
    }
    return element

def setInputScript(input = "b",scripts=[]):
    element = makeElement()
    element["commands"] = "EVENT_SET_INPUT_SCRIPT"
    element["args"] = {
        "input": input,
    }
    scripts.add(end())
    element["children"] = {
        "true": scripts
    }
    return element

def setBackgroundScript():
    element = makeElement()
    element["commands"] = "EVENT_SET_BACKGROUND_SCRIPT"
    element["args"] = {
    }
    return element

def removeInputScript(input = "['b']"):
    element = makeElement()
    element["commands"] = "EVENT_REMOVE_INPUT_SCRIPT"
    element["args"] = {
        "input": input,
    }
    return element

def variableMath(vectorX = "L0", operation = "set", other = "true", vectorY = "L0", value = "1", minValue = "0", maxValue = "255"):
    element = makeElement()
    element["commands"] = "EVENT_VARIABLE_MATH"
    element["args"] = {
        "vectorX": vectorX,
        "operation": operation,
        "other": other,
        "vectorY": vectorY,
        "value": value,
        "minValue": minValue,
        "maxValue": maxValue,
    }
    return element

def setValue(variable = "L0", value = "0"):
    element = makeElement()
    element["commands"] = "EVENT_SET_VALUE"
    element["args"] = {
        "variable": variable,
        "value": value,
    }
    return element

def setRandomValue():
    element = makeElement()
    element["commands"] = "EVENT_SET_RANDOM_VALUE"
    element["args"] = {
    }
    return element

def incValue(variable = "L0"):
    element = makeElement()
    element["commands"] = "EVENT_INC_VALUE"
    element["args"] = {
        "variable": variable,
    }
    return element

def decValue(variable = "L0"):
    element = makeElement()
    element["commands"] = "EVENT_DEC_VALUE"
    element["args"] = {
        "variable": variable,
    }
    return element

def mathAdd():
    element = makeElement()
    element["commands"] = "EVENT_MATH_ADD"
    element["args"] = {
    }
    return element

def mathSub():
    element = makeElement()
    element["commands"] = "EVENT_MATH_SUB"
    element["args"] = {
    }
    return element

def mathMul():
    element = makeElement()
    element["commands"] = "EVENT_MATH_MUL"
    element["args"] = {
    }
    return element

def mathDiv():
    element = makeElement()
    element["commands"] = "EVENT_MATH_DIV"
    element["args"] = {
    }
    return element

def mathMod():
    element = makeElement()
    element["commands"] = "EVENT_MATH_MOD"
    element["args"] = {
    }
    return element

def mathAddValue():
    element = makeElement()
    element["commands"] = "EVENT_MATH_ADD_VALUE"
    element["args"] = {
    }
    return element

def mathSubValue():
    element = makeElement()
    element["commands"] = "EVENT_MATH_SUB_VALUE"
    element["args"] = {
    }
    return element

def mathMulValue():
    element = makeElement()
    element["commands"] = "EVENT_MATH_MUL_VALUE"
    element["args"] = {
    }
    return element

def mathDivValue():
    element = makeElement()
    element["commands"] = "EVENT_MATH_DIV_VALUE"
    element["args"] = {
    }
    return element

def mathModValue():
    element = makeElement()
    element["commands"] = "EVENT_MATH_MOD_VALUE"
    element["args"] = {
    }
    return element

def copyValue():
    element = makeElement()
    element["commands"] = "EVENT_COPY_VALUE"
    element["args"] = {
    }
    return element

def setFlags(variable = "L0", flag1 = "False", flag2 = "False", flag3 = "False", flag4 = "False", flag5 = "False", flag6 = "False", flag7 = "False", flag8 = "False"):
    element = makeElement()
    element["commands"] = "EVENT_SET_FLAGS"
    element["args"] = {
        "variable": variable,
        "flag1": flag1,
        "flag2": flag2,
        "flag3": flag3,
        "flag4": flag4,
        "flag5": flag5,
        "flag6": flag6,
        "flag7": flag7,
        "flag8": flag8,
    }
    return element

def addFlags(variable = "L0", flag1 = "False", flag2 = "False", flag3 = "False", flag4 = "False", flag5 = "False", flag6 = "False", flag7 = "False", flag8 = "False"):
    element = makeElement()
    element["commands"] = "EVENT_ADD_FLAGS"
    element["args"] = {
        "variable": variable,
        "flag1": flag1,
        "flag2": flag2,
        "flag3": flag3,
        "flag4": flag4,
        "flag5": flag5,
        "flag6": flag6,
        "flag7": flag7,
        "flag8": flag8,
    }
    return element

def clearFlags(variable = "L0", flag1 = "False", flag2 = "False", flag3 = "False", flag4 = "False", flag5 = "False", flag6 = "False", flag7 = "False", flag8 = "False"):
    element = makeElement()
    element["commands"] = "EVENT_CLEAR_FLAGS"
    element["args"] = {
        "variable": variable,
        "flag1": flag1,
        "flag2": flag2,
        "flag3": flag3,
        "flag4": flag4,
        "flag5": flag5,
        "flag6": flag6,
        "flag7": flag7,
        "flag8": flag8,
    }
    return element

def ifFlagsCompare(variable = "L0", flag = "1", __collapseElse = "False", trueCommands = [], falseCommands = []):
    element = makeElement()
    element["commands"] = "EVENT_IF_FLAGS_COMPARE"
    element["args"] = {
        "variable": variable,
        "flag": flag,
        "__collapseElse": __collapseElse,
    }
    trueCommands.add(end())
    falseCommands.add(end())
    element["children"] = {
        "true": trueCommands,
        "false": falseCommands
    }
    return element

def awaitInput(input = "['a', 'b']"):
    element = makeElement()
    element["commands"] = "EVENT_AWAIT_INPUT"
    element["args"] = {
        "input": input,
    }
    return element

def text(text = "'push", avatarId = ""):
    element = makeElement()
    element["commands"] = "EVENT_TEXT"
    element["args"] = {
        "text": text,
        "avatarId": avatarId,
    }
    return element

def textSetAnimationSpeed(speedIn = "1", speedOut = "1", speed = "1"):
    element = makeElement()
    element["commands"] = "EVENT_TEXT_SET_ANIMATION_SPEED"
    element["args"] = {
        "speedIn": speedIn,
        "speedOut": speedOut,
        "speed": speed,
    }
    return element

def actorSetDirection(actorId = "player", direction = "up"):
    element = makeElement()
    element["commands"] = "EVENT_ACTOR_SET_DIRECTION"
    element["args"] = {
        "actorId": actorId,
        "direction": direction,
    }
    return element

def actorSetDirectionToValue(actorId = "player", variable = "L0"):
    element = makeElement()
    element["commands"] = "EVENT_ACTOR_SET_DIRECTION_TO_VALUE"
    element["args"] = {
        "actorId": actorId,
        "variable": variable,
    }
    return element

def actorSetPosition(actorId = "player", x = "0", y = "0"):
    element = makeElement()
    element["commands"] = "EVENT_ACTOR_SET_POSITION"
    element["args"] = {
        "actorId": actorId,
        "x": x,
        "y": y,
    }
    return element

def actorSetPositionRelative(actorId = "player", x = "0", y = "0"):
    element = makeElement()
    element["commands"] = "EVENT_ACTOR_SET_POSITION_RELATIVE"
    element["args"] = {
        "actorId": actorId,
        "x": x,
        "y": y,
    }
    return element

def actorMoveRelative(actorId = "player", x = "0", y = "0"):
    element = makeElement()
    element["commands"] = "EVENT_ACTOR_MOVE_RELATIVE"
    element["args"] = {
        "actorId": actorId,
        "x": x,
        "y": y,
    }
    return element

def actorMoveTo():
    element = makeElement()
    element["commands"] = "EVENT_ACTOR_MOVE_TO"
    element["args"] = {
    }
    return element

def actorPush(doContinue = "False"):
    element = makeElement()
    element["commands"] = "EVENT_ACTOR_PUSH"
    element["args"] = {
        "continue": doContinue,
    }
    return element

def actorSetAnimationSpeed(actorId = "player", speed = "3"):
    element = makeElement()
    element["commands"] = "EVENT_ACTOR_SET_ANIMATION_SPEED"
    element["args"] = {
        "actorId": actorId,
        "speed": speed,
    }
    return element

def actorSetMovementSpeed(actorId = "player", speed = "1"):
    element = makeElement()
    element["commands"] = "EVENT_ACTOR_SET_MOVEMENT_SPEED"
    element["args"] = {
        "actorId": actorId,
        "speed": speed,
    }
    return element

def actorEmote(actorId = "player", emoteId = "0"):
    element = makeElement()
    element["commands"] = "EVENT_ACTOR_EMOTE"
    element["args"] = {
        "actorId": actorId,
        "emoteId": emoteId,
    }
    return element

def playerSetSprite(spriteSheetId = "468ef314-e09e-42e2-8778-99e1331e8beb"):
    element = makeElement()
    element["commands"] = "EVENT_PLAYER_SET_SPRITE"
    element["args"] = {
        "spriteSheetId": spriteSheetId,
    }
    return element

def actorGetPosition(actorId = "player", vectorX = "L0", vectorY = "L0"):
    element = makeElement()
    element["commands"] = "EVENT_ACTOR_GET_POSITION"
    element["args"] = {
        "actorId": actorId,
        "vectorX": vectorX,
        "vectorY": vectorY,
    }
    return element

def actorGetDirection(actorId = "player", direction = "L0"):
    element = makeElement()
    element["commands"] = "EVENT_ACTOR_GET_DIRECTION"
    element["args"] = {
        "actorId": actorId,
        "direction": direction,
    }
    return element

def actorSetPositionToValue(actorId = "player", vectorX = "L0", vectorY = "L0"):
    element = makeElement()
    element["commands"] = "EVENT_ACTOR_SET_POSITION_TO_VALUE"
    element["args"] = {
        "actorId": actorId,
        "vectorX": vectorX,
        "vectorY": vectorY,
    }
    return element

def actorMoveToValue(actorId = "player", vectorX = "L0", vectorY = "L0"):
    element = makeElement()
    element["commands"] = "EVENT_ACTOR_MOVE_TO_VALUE"
    element["args"] = {
        "actorId": actorId,
        "vectorX": vectorX,
        "vectorY": vectorY,
    }
    return element

def actorInvoke(actorId = "82444b20-65df-436a-b1c1-191aacf2258d"):
    element = makeElement()
    element["commands"] = "EVENT_ACTOR_INVOKE"
    element["args"] = {
        "actorId": actorId,
    }
    return element

def actorSetFrame(actorId = "82444b20-65df-436a-b1c1-191aacf2258d", frame = "0"):
    element = makeElement()
    element["commands"] = "EVENT_ACTOR_SET_FRAME"
    element["args"] = {
        "actorId": actorId,
        "frame": frame,
    }
    return element

def actorSetFrameToValue(actorId = "82444b20-65df-436a-b1c1-191aacf2258d", variable = "L0"):
    element = makeElement()
    element["commands"] = "EVENT_ACTOR_SET_FRAME_TO_VALUE"
    element["args"] = {
        "actorId": actorId,
        "variable": variable,
    }
    return element

def cameraMoveTo(x = "0", y = "0", speed = "0"):
    element = makeElement()
    element["commands"] = "EVENT_CAMERA_MOVE_TO"
    element["args"] = {
        "x": x,
        "y": y,
        "speed": speed,
    }
    return element

def cameraLock(speed = "0"):
    element = makeElement()
    element["commands"] = "EVENT_CAMERA_LOCK"
    element["args"] = {
        "speed": speed,
    }
    return element

def cameraShake(time = "0.5"):
    element = makeElement()
    element["commands"] = "EVENT_CAMERA_SHAKE"
    element["args"] = {
        "time": time,
    }
    return element

def fadeOut(speed = "2"):
    element = makeElement()
    element["commands"] = "EVENT_FADE_OUT"
    element["args"] = {
        "speed": speed,
    }
    return element

def fadeIn(speed = "2"):
    element = makeElement()
    element["commands"] = "EVENT_FADE_IN"
    element["args"] = {
        "speed": speed,
    }
    return element

def showSprites():
    element = makeElement()
    element["commands"] = "EVENT_SHOW_SPRITES"
    element["args"] = {
    }
    return element

def hideSprites():
    element = makeElement()
    element["commands"] = "EVENT_HIDE_SPRITES"
    element["args"] = {
    }
    return element

def actorShow(actorId = "player"):
    element = makeElement()
    element["commands"] = "EVENT_ACTOR_SHOW"
    element["args"] = {
        "actorId": actorId,
    }
    return element

def actorHide(actorId = "player"):
    element = makeElement()
    element["commands"] = "EVENT_ACTOR_HIDE"
    element["args"] = {
        "actorId": actorId,
    }
    return element

def overlayShow(color = "black", x = "0", y = "0"):
    element = makeElement()
    element["commands"] = "EVENT_OVERLAY_SHOW"
    element["args"] = {
        "color": color,
        "x": x,
        "y": y,
    }
    return element

def overlayHide():
    element = makeElement()
    element["commands"] = "EVENT_OVERLAY_HIDE"
    element["args"] = {
    }
    return element

def overlayMoveTo(x = "0", y = "0", speed = "1"):
    element = makeElement()
    element["commands"] = "EVENT_OVERLAY_MOVE_TO"
    element["args"] = {
        "x": x,
        "y": y,
        "speed": speed,
    }
    return element

def musicPlay(musicId = "56622189-8327-4a64-bd29-2fbcf243c97e", loop = "True"):
    element = makeElement()
    element["commands"] = "EVENT_MUSIC_PLAY"
    element["args"] = {
        "musicId": musicId,
        "loop": loop,
    }
    return element

def musicStop():
    element = makeElement()
    element["commands"] = "EVENT_MUSIC_STOP"
    element["args"] = {
    }
    return element

def soundPlayBeep():
    element = makeElement()
    element["commands"] = "EVENT_SOUND_PLAY_BEEP"
    element["args"] = {
    }
    return element

def callCustomEvent(customEventId = "4bf11658-2bb2-4e79-ad96-22577c9a8353", __name = "Custom Event 1"):
    element = makeElement()
    element["commands"] = "EVENT_CALL_CUSTOM_EVENT"
    element["args"] = {
        "customEventId": customEventId,
        "__name": __name,
    }
    return element