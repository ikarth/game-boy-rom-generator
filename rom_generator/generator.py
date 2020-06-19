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
from pathlib import Path



def makeProject():

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

    def makeSpriteSheet(name, frames, type, filename):
        element = makeElement()
        element["name"] = name
        element["frames"] = frames
        element["type"] = type
        element["filename"] = filename
        element["_v"] = int(round(time.time() * 1000.0)) # set creation time (for versioning?)
        return element

    def makeBackground(name, filename, width, height, imageWidth, imageHeight):
        element = makeElement()
        element["name"] = name
        element["width"] = width
        element["height"] = height
        element["imageWidth"] = imageWidth
        element["imageHeight"] = imageHeight
        element["filename"] = filename
        element["_v"] = int(round(time.time() * 1000.0))
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
                shutil.copy2(asset_path + ui_asset["asset_file_name"], temp_file)
                ui_assets.append({"filename": ui_asset["filename"]})
            except FileNotFoundError as err:
                print(f"Asset File Missing: {err}")
        return ui_assets


    def write_assets(asset_array, output_path, asset_path):
        Path(output_path + "assets/temp/").mkdir(parents=True, exist_ok=True)
        Path(output_path + asset_path).mkdir(parents=True, exist_ok=True)
        for element in asset_array:
            f_name = element["filename"]
            print(f_name)
            temp_file = Path(output_path + "assets/temp/scratch.file")
            try:
                shutil.copy2(asset_path + f_name, temp_file)
                os.replace(Path(temp_file), Path(output_path + asset_path + f_name))
            except FileNotFoundError as err:
                print(f"Asset File Missing: {err}")
        if not shutil.rmtree.avoids_symlink_attacks:
            logging.info("Temp directory deletion potentially vulerable to symlink attacks.")
        shutil.rmtree(Path(output_path + "assets/temp/"))

    def write_project_to_disk(gb_project, filename="test.gbsproj", output_path="../gbprojects/projects/"):
        # Write project to JSON
        gb_project_without_ui_elements = copy.deepcopy(gb_project)
        gb_project_without_ui_elements.ui = None
        generated_project = json.dumps(gb_project_without_ui_elements.__dict__, indent=4)
        print(generated_project)
        Path(output_path).mkdir(parents=True, exist_ok=True)
        with open(f"{output_path}{filename}", "w") as wfile:
            wfile.write(generated_project)

        # Copy assets to projects
        write_assets(gb_project.spriteSheets, output_path, "assets/sprites/")
        write_assets(gb_project.music, output_path, "assets/music/")
        write_assets(gb_project.backgrounds, output_path, "assets/backgrounds/")
        ui_asset_array = write_ui_assets(gb_project.ui, "assets/ui/")
        write_assets(ui_asset_array, output_path, "assets/ui/")



    def create():
        # Set up a barebones project
        project = types.SimpleNamespace(**base_gb_project)
        project.settings = default_project_settings.copy()
        project.ui = [
        {"filename": "ascii.png", "asset_file_name": "original/ascii.png"},
        {"filename": "cursor.png", "asset_file_name": "original/cursor.png"},
        {"filename": "emotes.png", "asset_file_name": "original/emotes.png"},
        {"filename": "frame.png", "asset_file_name": "original/frame.png"}]

        # Create sprite sheets
        player_sprite_sheet = makeSpriteSheet("actor_animated", 6, "actor_animated", "actor_animated.png")
        project.spriteSheets.append(player_sprite_sheet)
        a_rock_sprite = makeSpriteSheet("rock", 1, "static", "rock.png")
        project.spriteSheets.append(a_rock_sprite)

        # Add a background image
        default_bkg = makeBackground("placeholder", "placeholder.png", 20, 18, 160, 144)
        project.backgrounds.append(default_bkg)

        # Create a scene
        a_scene = makeScene("Scene 0", default_bkg["id"], 20, 18, 228, 172)
        # Create an actor
        for x in range(9): # Maximum number of actors in GB Studio is 9
            actor_x = random.randint(0,18)
            actor_y = random.randint(1,17)
            example_rock = makeActor(a_rock_sprite["id"], actor_x, actor_y)
            a_scene["actors"].append(example_rock)
        # Add scene to project
        project.scenes.append(a_scene)

        # Add some music
        project.music.append(makeMusic("template", "template.mod"))

        # Set the starting scene and player sprite
        project.settings["startSceneId"] = a_scene["id"]
        project.settings["playerSpriteSheetId"] = player_sprite_sheet["id"]

        write_project_to_disk(project)

    create()

### Run the generator
if __name__ == '__main__':
    makeProject()
