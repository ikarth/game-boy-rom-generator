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





def makeProject(project_output_path="../gbprojects/projects/", asset_folder="../assets/"):

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

    ### Create a basic GBS element, with a unique ID

    def makeElement():
        element = {}
        element["id"] = str(uuid.uuid4())
        return element.copy()

    def makeMusic(name, filename):
        element = makeElement()
        element["name"] = name
        element["filename"] = filename
        element["_v"] = int(round(time.time() * 1000.0)) # set creation time (for versioning?)
        return element

    def getImageInfo(image_filename, image_type="sprites"):
        im = Image.open(Path(asset_folder).joinpath(image_type, image_filename))
        return {"pixel_width": im.size[0], "pixel_height": im.size[1], "image_format": im.format, "image_mode": im.mode}

    def makeSpriteSheet(name, frames, type, filename):
        element = makeElement()
        element["name"] = name
        element["frames"] = frames
        element["type"] = type
        element["filename"] = filename
        element["_v"] = int(round(time.time() * 1000.0)) # set creation time (for versioning?)
        element["_generator_metadata"] = getImageInfo(filename)
        return element

    def makeBackground(name, filename, width=None, height=None, imageWidth=None, imageHeight=None):
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

    def makeActor(sprite_id, x, y, movementType="static"):
        element = makeElement()
        element["spriteSheetId"] = sprite_id
        element["movementType"] = movementType
        element["moveSpeed"] = "1"
        element["animSpeed"] = "3"
        element["x"] = x
        element["y"] = y
        return element

    def makeScene(name, background, width, height, x, y, collisions=[], actors=[], triggers=[]):
        element = makeElement()
        element["name"] = name
        element["backgroundId"] = background
        element["width"] = width
        element["height"] = height
        element["x"] = x
        element["y"] = y
        element["collisions"] = collisions
        element["actors"] = actors
        element["triggers"] = triggers
        return element

    ### Writing the project to disk

    def write_ui_assets(ui_asset_array, asset_path):
        ui_assets = []
        for ui_asset in ui_asset_array:
            temp_file = Path("assets/ui/" + ui_asset["filename"])
            try:
                copy_path = os.path.abspath(Path(asset_path).joinpath(ui_asset["asset_file_name"]))
                shutil.copy2(copy_path, temp_file)
                ui_assets.append({"filename": ui_asset["filename"]})
            except FileNotFoundError as err:
                print(f"Asset File Missing: {err}")
        return ui_assets


    def write_assets(asset_array, output_path, asset_path):
        Path(output_path + "assets/temp/").mkdir(parents=True, exist_ok=True)
        Path(output_path).joinpath(asset_path).mkdir(parents=True, exist_ok=True)
        for element in asset_array:
            f_name = element["filename"]
            print(f_name)
            temp_file = os.path.abspath(Path(output_path + "assets/temp/scratch.file"))
            try:
                copy_path = os.path.abspath(Path(asset_path).joinpath(f_name))
                destination_path = Path(output_path).joinpath(asset_path, f_name)
                shutil.copy2(copy_path, temp_file)
                os.replace(Path(temp_file), destination_path)
                logging.info(f"Wrote {destination_path}")
            except FileNotFoundError as err:
                print(f"Asset File Missing: {err}")
                logging.warning(f"Asset File Missing: {err}")
        if not shutil.rmtree.avoids_symlink_attacks:
            logging.info("Temp directory deletion potentially vulerable to symlink attacks.")
        shutil.rmtree(Path(output_path + "assets/temp/"))

    def write_project_to_disk(gb_project, filename="test.gbsproj", output_path="../gbprojects/projects/"):
        # Write project to JSON
        logging.info(f"Writing {filename} project file...")
        gb_project_without_ui_elements = copy.deepcopy(gb_project)
        gb_project_without_ui_elements.ui = None
        generated_project = json.dumps(gb_project_without_ui_elements.__dict__, indent=4)
        print(generated_project)
        Path(output_path).mkdir(parents=True, exist_ok=True)
        with open(f"{output_path}{filename}", "w") as wfile:
            wfile.write(generated_project)

        # Copy assets to projects
        print("*** Writing assets ***")
        write_assets(gb_project.spriteSheets, output_path, Path(asset_folder + "sprites/"))
        write_assets(gb_project.music, output_path, Path(asset_folder + "music/"))
        write_assets(gb_project.backgrounds, output_path, Path(asset_folder + "backgrounds/"))
        ui_asset_array = write_ui_assets(gb_project.ui, Path(asset_folder +"ui/"))
        write_assets(ui_asset_array, output_path, Path(asset_folder + "ui/"))

    def makeBasicProject():
        project = types.SimpleNamespace(**base_gb_project)
        project.settings = default_project_settings.copy()
        project.ui = [
        {"filename": "ascii.png", "asset_file_name": "original/ascii.png"},
        {"filename": "cursor.png", "asset_file_name": "original/cursor.png"},
        {"filename": "emotes.png", "asset_file_name": "original/emotes.png"},
        {"filename": "frame.png", "asset_file_name": "original/frame.png"}]
        return project


    def create():
        # Set up a barebones project
        project = makeBasicProject()

        # Create sprite sheets
        player_sprite_sheet = makeSpriteSheet("actor_animated", 6, "actor_animated", "actor_animated.png")
        project.spriteSheets.append(player_sprite_sheet)
        a_rock_sprite = makeSpriteSheet("rock", 1, "static", "rock.png")
        project.spriteSheets.append(a_rock_sprite)

        # Add a background image
        default_bkg = makeBackground("placeholder", "placeholder.png")
        project.backgrounds.append(default_bkg)
        bkg_x = default_bkg["imageWidth"]
        bkg_y = default_bkg["imageHeight"]
        bkg_width = default_bkg["width"]
        bkg_height = default_bkg["height"]

        # Create a scene
        a_scene = makeScene("Scene 0", default_bkg["id"], 20, 18, 228, 172)
        # Create an actor
        for x in range(9): # Maximum number of actors in GB Studio is 9
            actor_x = random.randint(0,(bkg_width-2)) # Second value subtracted by 1 to keep sprite within bounds of the screen
            actor_y = random.randint(1,bkg_height-1) # First value added by 1 to keep sprite within bounds of the screen
            example_rock = makeActor(a_rock_sprite["id"], actor_x, actor_y)
            a_scene["actors"].append(example_rock)
        # Add scene to project
        project.scenes.append(a_scene)

        # Add some music
        project.music.append(makeMusic("template", "template.mod"))

        # Set the starting scene and player sprite
        project.settings["startSceneId"] = a_scene["id"]
        project.settings["playerSpriteSheetId"] = player_sprite_sheet["id"]

        write_project_to_disk(project, output_path=project_output_path)

    create()

### Run the generator
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate a Game Boy ROM via a GB Studio project file.")
    parser.add_argument('--destination', '-d', type=str, help="destination folder name", default="../gbprojects/projects/")
    parser.add_argument('--assets', '-a', type=str, help="asset folder name", default="assets/")
    args = parser.parse_args()
    makeProject(project_output_path=args.destination, asset_folder = args.assets)
