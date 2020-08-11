import assets
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
import re
import collections
from datetime import datetime
from contextlib import contextmanager
from pathlib import Path
from PIL import Image
from rom_generator import script_functions as scripts
from rom_generator.utilities import makeElement
import rom_generator.scriptFunctions2 as scripts2
try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources
from rom_generator.utilities import bcolors

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



# Template Slots

# def makeConnection(source_location, source_size, destination_scene, destination_location, destination_direction):
#     trigger_00 = generator.makeTrigger('trigger_00', source_location[0], source_location[1], source_size[0], source_size[1])
#     trigger_00['script'] = [
#         script.switchScene(sceneId=destination_scene["id"], x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
#         script.end()
#     ]
#     return trigger_00

# Make Project
curKeyNumber = 511
scene_count = 0
generator_seed = "game boy generator"

def initializeGenerator(new_seed=None):
    global scene_count
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
scene_spacing = 400

def assignSceneLocation(scene_number):
    x = (scene_number % scene_columns) * scene_spacing
    y = (scene_number // scene_columns) * scene_spacing
    return (x, y)

### Create a music element
def makeMusic(name, filename):
    element = makeElement()
    element["name"] = name
    element["filename"] = filename
    #element["_v"] = int(round(time.time() * 1000.0)) # set creation time (for versioning?)
    return element

def getAssetFolder():
    with pkg_resources.path('assets', 'assets.txt') as asset_filename:
        return os.path.dirname(Path(asset_filename))
    raise FileNotFoundError("Asset folder not found")

def getImage(image_filename, image_type="sprites"):
    if os.path.basename(image_filename) != image_filename:
        dir_path = os.path.basename(os.path.dirname(image_filename))
        parent_dir = os.path.basename(os.path.dirname(os.path.dirname(image_filename)))
        if "assets" != parent_dir:
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

record_of_sprites = []
def recordSprite(sprite):
    """
    Check to see if this sprite already exists in this run.
    If so, return the first instance of it.
    """
    global record_of_sprites

    if (len(record_of_sprites)) > 0:
        found = [sp for sp in record_of_sprites if ((sp["filename"] == sprite["filename"]) and (sp["type"] == sprite["type"]) and(sp["frames"] == sprite["frames"]))]
        if (len(found) > 0):
            return found[0]
    # this is a new sprite
    record_of_sprites.append(sprite)
    return None

### A sprite sheet is a collection of images to display at the location of an actor or player.
### A sprite sheet can be one 16x16 static image...
### ...or can be animated by connecting multiple 16x16 frames horizontally in a single image.
def makeSpriteSheet(filename, name=None, type="static", frames=None):
    """
    Create a sprite sheet.

    A sprite sheet is a collection of images to display at the location of an actor or player.
    A sprite sheet can be one 16x16 static image...
    ...or can be animated by connecting multiple 16x16 frames horizontally in a single image.
    """
    if name is None:
        name = filename
    element = makeElement()
    element["name"] = name
    element["type"] = type
    element["filename"] = filename
    # element["_v"] = int(round(time.time() * 1000.0)) # set creation time (for versioning?)
    element["_generator_metadata"] = getImageInfo(filename)
    width = element["_generator_metadata"]["pixel_width"]
    height = element["_generator_metadata"]["pixel_height"]
    if (width % 16 != 0) or (height % 16 != 0):
        logging.warning(f"Sprite sheet {name} is not a multiple of 16: ({width},{height})")
    if frames is None:
        element["frames"] = width // 16
    else:
        element["frames"] = frames
    assert(isinstance(element, dict))
    record = recordSprite(copy.deepcopy(element))
    if None != record:
        return record
    return copy.deepcopy(element)

def addSpriteSheet(project, filename, name=None, type="static", frames=None):
    """Create a sprite sheet and add it to the project."""
    element = makeSpriteSheet(filename, name, type, frames)
    project.spriteSheets.append(element)
    return element


record_of_backgrounds = []
def recordBackground(sprite):
    """
    Check to see if this sprite already exists in this run.
    If so, return the first instance of it.
    """
    global record_of_backgrounds
    found = [sp for sp in record_of_backgrounds if ((sp["filename"] == sprite["filename"]) and (sp["width"] == sprite["width"]) and(sp["height"] == sprite["height"]))]
    if (len(found) > 0):
        return found[0]
    # this is a new sprite
    record_of_backgrounds.append(sprite)
    return sprite

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
    #element["_v"] = int(round(time.time() * 1000.0))
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
    return copy.deepcopy(recordBackground(element))

### An actor is an object on the screen that the player can interact with.
def makeActor(sprite, x, y, movementType="static", animate=True, moveSpeed="1", animSpeed="3", script=[], sprite_id=None, direction=None):
    element = makeElement()
    if sprite == None:
        element["spriteSheetId"] = sprite_id
    else:
        element["spriteSheetId"] = sprite["id"]
    element["movementType"] = movementType
    if not moveSpeed is None:
        element["moveSpeed"] = moveSpeed
    element["animSpeed"] = animSpeed
    if not direction is None:
        element["direction"] = direction
    element["x"] = x
    element["y"] = y
    element["animate"] = animate
    element["script"] = []
    element["startScript"] = []
    return copy.deepcopy(element)

def addActor(scene, sprite, x, y, movementType="static", animate=True):
    """
    Creates an actor and adds it to the scene it is given.
    """
    element = makeActor(sprite, x, y, movementType, animate)
    scene["actors"].append(element)
    return element

### A trigger causes a script to play when the player reaches the trigger's location.
def makeTrigger(trigger_name, x, y, width, height, script=[]):
  element = makeElement()
  element["trigger"] = trigger_name
  element["x"] = x
  element["y"] = y
  element["width"] = width
  element["height"] = height
  element["script"] = script
  return copy.deepcopy(element)

def addSceneBackground(project, scene, background):
    print(scene)
    print(background)
    scene["backgroundId"] = background["id"]
    scene["width"] = background["width"]
    scene["height"] = background["height"]
    [print(s) for s in project.scenes if s["id"] == scene["id"]]
    return scene

record_of_scenes = []
def recordScene(scene, scene_label):
    """
    Record the scenes that have been created so far this session.
    """
    global record_of_scenes
    record_of_scenes.append((scene_label, scene))

def getSceneIdByLabel(scene_label):
    scene_iter = (rs[1] for rs in record_of_scenes if rs[0] == scene_label)
    found_scene = next(scene_iter, None)
    if found_scene is None:
        return None
    return found_scene['id']

def makeScene(name, background, width=None, height=None, x=None, y=None, collisions=[], actors=[], triggers=[], scene_label="Scene"):
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
        element["name"] = f"{scene_label}_{scene_count:04}"
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
    record_scene = copy.deepcopy(element)
    recordScene(record_scene, scene_label)
    return record_scene

def addSceneData(project, scene_data):
    """
    Given a data structure containing a scene and its referenced elements,
    insert them into the project.

    Expects that scene_data is a dictionary with the following elements:
    - "scene": the generated scene itself
    - "background": the background image
    - "sprites": list of spriteSheets
    - "connections": list of connection slots
    - "tags": list of tags for this scene
    """
    project.scenes.append(scene_data["scene"])
    # TODO: Check for existing assets and don't re-add duplicates
    project.backgrounds.append(scene_data["background"])
    for sprite_sheet in scene_data["sprites"]:
        project.spriteSheets.append(sprite_sheet)

# def connectScenesRandomly(scene_data_list):
#     """
#     Connect scenes in the scene data list at random, using the connection slots.
#     """
#     connections_to_make_in = []
#     connections_to_make_out = []
#     for scene_num, scene in enumerate(scene_data_list):
#         #other_scene_list = [s for s in scene_data_list if s["id"] != scene["id"]]
#         #other_scene = random.choice(other_scene_list)
#         for con_num, con in enumerate(scene["connections"]):
#             connections_to_make_in.append([scene["scene"]["id"], con_num, con])
#             connections_to_make_out.append([scene["scene"]["id"], con_num, con])
#
#     connections_made = []
#     while len(connections_to_make_out) > 0:
#         current_connection = connections_to_make_out.pop()
#         filtered_other_connections = [c for c in connections_to_make_in if c[0] != current_connection[0]]
#         try:
#             other_connection = random.choice(filtered_other_connections)
#             if other_connection in connections_to_make_in:
#                 connections_to_make_in.remove(other_connection)
#             con_data = {"in": other_connection, "out": current_connection}
#             connections_made.append(con_data)
#         except IndexError as e:
#             pass
#
#     for c in connections_made:
#         source_scene = [s for s in scene_data_list if s["scene"]["id"] == c["out"][0]][0]
#         out_position = (c["out"][2]["out"][0], c["out"][2]["out"][1])
#         trigger_size = (c["out"][2]["out"][2], c["out"][2]["out"][3])
#         destination_scene = [s for s in scene_data_list if s["scene"]["id"] == c["in"][0]][0]
#         destination_position = (c["in"][2]["in"][0], c["in"][2]["in"][1])
#         # print("out:", source_scene['scene']['id'], source_scene['scene']['name'], out_position, trigger_size, "\tin:", destination_scene['scene']['id'], destination_scene['scene']['name'], destination_position)
#         makeTriggerConnectionToScene(source_scene, out_position, trigger_size, destination_scene, destination_position)

import pprint
def connectScenesRandomlySymmetric(scene_data_list):
    """
    Connect scenes in the scene data list at random, using the connection slots.
    Connections should be symmetric
    """

    # Get connections
    connections_to_make = []
    for scene_num, scene in enumerate(scene_data_list):
        for con_num, con in enumerate(scene["connections"]):
            connections_to_make.append([scene["scene"]["id"], con_num, con])

    # pick which connections link with which other connections
    connections_made = []
    while len(connections_to_make) > 0:
        current_connection = connections_to_make.pop()
        filtered_other_connections = [c for c in connections_to_make if c[0] != current_connection[0]]
        if len(filtered_other_connections) == 0:
            filtered_other_connections = connections_to_make
        try:
            other_connection = random.choice(filtered_other_connections)
            if other_connection in connections_to_make:
                connections_to_make.remove(other_connection)
            con_data = {"in": other_connection, "out": current_connection}
            con_data_two = {"in": current_connection, "out": other_connection}
            print(f"Connecting\n\t{current_connection}\n\tto\n\t{other_connection}\n")
            connections_made.append(con_data)
            connections_made.append(con_data_two)
        except IndexError as e:
            break

    # make the connections
    for connection in connections_made:
        source_scene = [s for s in scene_data_list if s["scene"]["id"] == connection["in"][0]][0]
        creator_func = connection["in"][2]["creator"]
        trigger = creator_func(source_location=connection["in"][2]["args"]["entrance_location"],
                                source_size=connection["in"][2]["args"]["entrance_size"],
                                destination_scene_id=connection["out"][0],
                                destination_location=connection["out"][2]["args"]["exit_location"],
                                destination_direction=connection["out"][2]["args"]["exit_direction"])
        source_scene["scene"]["triggers"].append(trigger)



### Adds trigger for scene connection.
def makeTriggerConnectionToScene(scene, out_position, trigger_size, destination_scene, destination_position, destination_direction="up"):
    trigger_script = [scripts.switchScene(sceneId = destination_scene,
                                x = destination_position[0],
                                y = destination_position[1],
                                direction = destination_direction)]
    trigger_connection = makeTrigger(f"walkTo{destination_scene}",
                                    out_position[0],
                                    out_position[1],
                                    trigger_size[0],
                                    trigger_size[1],
                                    trigger_script)
    scene['scene']["triggers"].append(trigger_connection)


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



def makeTriggerAndSwitchScene(scene1, scene2, x, y, x1, y2):
    scene1["triggers"].append(makeTrigger(scene1, x, y, 2, 1, [scripts.switchScene(sceneId = scene2["id"], x = x1, y = y2)]))




# Adds trigger for scene connection.
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

### creates a key to a lock
def makeKey(sprite, x, y):
    global curKeyNumber
    key = makeActor(sprite, x, y, animate = False)
    key["startScript"].append(scripts2.disableCollisions("$self$"))
    key["script"].append(scripts.actorHide(actorId = "$self$"))
    key["script"].append(scripts.setTrue(variable = curKeyNumber))
    key["script"].append(scripts.end())
    return key

### creates a lock for the key (This must be created directly after the key creation to work)
def makeLock(sprite, x, y):
    global curKeyNumber
    lock = makeActor(sprite, x, y, animate = False)
    trueCommands = [
        scripts.setFalse(variable = curKeyNumber),
        scripts.actorHide(actorId = "$self$")
    ]
    lock["script"].append(scripts.ifTrue(variable = curKeyNumber, trueCommands = trueCommands))
    curKeyNumber = curKeyNumber - 1
    return lock

#this makes a connection sprite
def makeConnectionSprite(sprite, x, y):
    con = makeActor(sprite, x, y, animate = False)
    con["startScript"] = [scripts2.disableCollisions("$self$"), scripts.end()]
    return con


### Writing the project to disk ###

def writeUIAssets(ui_asset_array, asset_path):
    """
    Return the paths to the UI assets, because they're a somewhat special case.
    """
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


def writeAssets(asset_array, output_path, sub_asset_path):
    """
    Take the assets referenced by the project and write them to the project.
    """
    check_for_duplicates = set()
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
        if f_name in check_for_duplicates:
            logging.warning(f"Duplicate {f_name} found.")
        check_for_duplicates.add(f_name)
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
            shutil.copy2(copy_path, temp_file)
            os.replace(Path(temp_file), destination_path)
            logging.info(f"Wrote {destination_path}")
        except FileNotFoundError as err:
            print(f"Asset File Missing for writeAssets(): {err}")
            logging.warning(f"Asset File Missing: {err}")
            raise
    if not shutil.rmtree.avoids_symlink_attacks:
        logging.info("Temp directory deletion potentially vulnerable to symlink attacks.")
    shutil.rmtree(Path(output_path).joinpath("assets/temp/"))

def uniques(list_of_elements):
    """
    Returns the argument, filtered to remove duplicates
    """
    seen = set()
    dedupe = []
    for element in list_of_elements:
        e_tup = json.dumps(element, sort_keys=True)
        if e_tup not in seen:
            seen.add(e_tup)
            dedupe.append(element)
    return dedupe

def getRefInScenes(ref_match_object, list_of_scenes):
    ref_target_name = ref_match_object.groups()[0]
    ref_target_name = re.sub(" ", "_", ref_target_name)
    for s_num, s_data in enumerate(list_of_scenes):
        if ref_target_name in s_data["scene"]["name"]:
            return s_data["scene"]["id"]
    return "NO_REF"

def translateReferences(data, list_of_scenes):
    """
    Translate the unbound references in the scene by referring to the other scenes.

    Call it after all of the scenes have been created.
    """
    if isinstance(data, str):
        while ("♔" in data):
            if data.startswith("♔REFERENCE_TO_SCENES_"):
                ref_match = re.search(r'♔REFERENCE_TO_SCENES_\<(.*?)\>', data)
                if None != ref_match:
                    data = getRefInScenes(ref_match, list_of_scenes)
            else:
                data = "♔UNBOUND_REF♔"
    if (isinstance(data, list)):
        for data_key, data_val in enumerate(data):
            data[data_key] = translateReferences(data_val, list_of_scenes)
    if (isinstance(data, collections.abc.Mapping)):
        for data_key, data_val in data.items():
            data[data_key] = translateReferences(data_val, list_of_scenes)
    if (isinstance(data, types.SimpleNamespace)):
        for data_key, data_val in data.__dict__.items():
            data[data_key] = translateReferences(data_val, list_of_scenes)
    return data

# def attachReferences(proj_as_json, proj_as_data):
#     """
#     Take a JSON-ified version of the project, look for reference strings that still need to be replaced, replace them.
#     Reference strings are in the format '♔REFERENCE_TO_SCENES_<>♔'.
#     Returns the JSON with the newly-remapped references.
#     """
#     some_references_remain = True
#     while some_references_remain:
#         if "♔" in proj_as_json:
#             search_pattern = r"♔REFERENCE_TO_SCENES_\<(.*?<ref>)\>"
#             match = re.search(search_pattern)
#             found_id = "XXXXXXXXXXXXXXXXXX"
#             new_json = re.sub(search_pattern, found_id, proj_as_json, count=1)
#             console.log(match)
#             proj_as_json = new_json
#         some_references_remain = False
#     return proj_as_json

def writeProjectToDisk(gb_project, filename="test.gbsproj", output_path="gbprojects/projects/"):
    """
     Write project to JSON

     Writes out a GBStudio project file at the output_path folder, with the filename.
     Also copies over the relevant images and other assets that the project uses.
    """
    output_path = os.path.abspath(Path(os.path.dirname(__file__)).joinpath('..').joinpath(output_path))
    logging.info(f"writeProjectToDisk: {bcolors.OKGREEN}{os.path.abspath(output_path)}{bcolors.ENDC}")
    logging.info(f"Writing {filename} project file...")
    gb_project_without_ui_elements = copy.deepcopy(gb_project)
    if "ui" in gb_project_without_ui_elements.__dict__.keys():
        gb_project_without_ui_elements.ui = None

    # TODO: duplicates need to be unified in ID values as well, so we don't end up with missing images...
    # gb_project_without_ui_elements.spriteSheets = uniques(gb_project_without_ui_elements.spriteSheets)
    # gb_project_without_ui_elements.backgrounds = uniques(gb_project_without_ui_elements.backgrounds)

    DEBUG_TEST_TYPES = False
    if DEBUG_TEST_TYPES:
        import collections.abc
        import pprint
        def recursivePrintType(data, func):
            length = ""
            try:
                length = str(len(data))
            except:
                pass
            if isinstance(data, int) or isinstance(data, str):
                pass
            else:
                print(f"{func(data)}\t{length}")
            if (isinstance(data, set)):
                pprint.pprint(data)
                breakpoint()
            if (isinstance(data, list)):
                for data_key, data_val in enumerate(data):
                    recursivePrintType(data_val, func)
            if (isinstance(data, collections.abc.Mapping)):
                for data_key, data_val in data.items():
                    recursivePrintType(data_val, func)
            if (isinstance(data, types.SimpleNamespace)):
                for data_key, data_val in data.__dict__.items():
                    recursivePrintType(data_val, func)
        recursivePrintType(gb_project_without_ui_elements, type)

    generated_project = json.dumps(gb_project_without_ui_elements.__dict__, indent=4)

    #generated_project = attachReferences(generated_project, gb_project_without_ui_elements)

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
    """
    Make a basic, barebones project that our code can start to add to.
    """
    project = types.SimpleNamespace(**base_gb_project)
    project.settings = default_project_settings.copy()
    project.ui = [
    {"filename": "ascii.png",  "asset_file_name": "original/ascii.png"},
    {"filename": "cursor.png", "asset_file_name": "original/cursor.png"},
    {"filename": "emotes.png", "asset_file_name": "original/emotes.png"},
    {"filename": "frame.png",  "asset_file_name": "original/frame.png"}]

    # TODO: these being globals is causing issues, these should be project specific
    global record_of_sprites
    global record_of_scenes
    record_of_sprites = []
    record_of_scenes = []
    return copy.deepcopy(project)

# makes a border of collisions around a scene
def makeColBorder(scenex):
    """
    Makes a border of collisions around a scene.
    """
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
        cc.insert(0, jnum[::-1])
    scenex["collisions"] = cc

def toByteStrings(grid):
    """
    Take a nested array of 0/1 or T/F values and translates into bit strings.

    Should be functionally equivalent to the string-making behavior in makeCol.
    """
    print(grid)
    byte_strings_array = []
    byte_consumer = ""
    def consume():
        nonlocal byte_consumer, byte_strings_array
        byte_strings_array.append(int(byte_consumer[::-1], 2))
        byte_consumer = ""

    for row_num, row in enumerate(grid):
        for col_num, column in enumerate(row):
            truth_val = 0
            if (column == True) or (column != 0):
                truth_val = 1
            byte_consumer += str(truth_val)
            if len(byte_consumer) >= 8:
                consume()
    if len(byte_consumer) > 0:
        while len(byte_consumer) < 8:
            byte_consumer += "0"
    consume()

    return byte_strings_array

def makeCol(array01, scene01):
    """
    Takes in 1D array of 0s and 1s, puts in collisions accordingly

    Specifically, translates a 1D array of collision bits that represents
    the 2d collision data into a list of strings, with each string as the
    bitfield that holds the on/off collision data for 8 tiles.
    """
    wid = scene01["width"]
    hei = scene01["height"]
    cc = []
    max = 0
    total_collision_spaces = ((wid * hei - 1) % 8) + (wid * hei - 1)
    while max < wid * hei - 1:
        j = " "
        g = 1
        while g < 9:
            if array01[max] == 1:
                j = j + "1"
            elif array01[max] == 0:
                j = j + "0"
            max = max + 1
            g = g + 1
        jnum = int(j[::-1], 2) # reverse the string because the collision data is big-endian
        cc.insert(0, jnum)
    # Need to add this in case the total number of collision tiles isn't evenly
    # divisible by 8
    if max <= total_collision_spaces:
        cc.insert(0, 0)
    scene01["collisions"] = cc[::-1]

def genQuestions(txtfile, scriptt):
    #counting number of lines in txt file
    count = 0
    with open(txtfile, 'r') as f:
        for line in f:
            count += 1
    #generating random line number
    random.seed(datetime.now())
    numz = random.randint(0, (count / 3) - 1) * 3
    #reading file
    f = open(txtfile, 'r')
    file_contents = f.readlines()
    #elements
    element = makeElement()
    element["command"] = "EVENT_TEXT"
    element["args"] = {
        "text": [file_contents[numz]],
        "avatarId": ""
    }
    scriptt.append(element)
    element = makeElement()
    element["command"] = "EVENT_CHOICE"
    element["args"] = {
        "variable": "L0",
        "trueText": [file_contents[numz + 1].strip()],
        "falseText": [file_contents[numz + 2].strip()]
    }
    scriptt.append(element)

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

    c_bkg = makeBackground("c_test_3.png", "c_test")
    project.backgrounds.append(c_bkg)
    c_scene = makeScene("c_scene", c_bkg)
    collisions = [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    makeCol(collisions, c_scene)
    print(c_scene["collisions"])
    project.scenes.append(c_scene)
    d_scene = makeScene("d_scene", c_bkg)
    collisions = [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    collision_string = toByteStrings(collisions)
    d_scene["collisions"] = collision_string
    project.scenes.append(d_scene)
    print(collision_string)



    # We want to create a bunch of scenes.
    # Here I'm just creating them randomly.
    prior_scenes = len(project.scenes)
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
                    addSymmetricSceneConnections(project, project.scenes[y + prior_scenes], project.scenes[other_scene + prior_scenes], chosen_direction, doorway_sprite)
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
