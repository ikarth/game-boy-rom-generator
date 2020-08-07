import argparse
import copy
import random
from generator import makeElement, makeBasicProject, addSpriteSheet, makeBackground, makeScene, makeActor, addSymmetricSceneConnections, makeMusic, reverse_direction, initializeGenerator, writeProjectToDisk, addSceneBackground
from background import getTileList, makeCheckerboardArray, generateBackgroundImageFromTiles, generateBackground, makeBackgroundCollisions

def createYourNameWorld():
    """
    Create an empty world as an example to build future projects from.
    """
    # Set up a barebones project
    project = makeBasicProject()

    # Create sprite sheet for the player sprite
    player_sprite_sheet = addSpriteSheet(project, "actor_animated.png", "actor_animated", "actor_animated")
    project.settings["playerSpriteSheetId"] = player_sprite_sheet["id"]

    # add a sprite we can use for the rocks
    a_rock_sprite = addSpriteSheet(project, "rock.png", "rock", "static")
    a_dog_sprite = addSpriteSheet(project, "dog.png", "dog", "static")

    # Add a background image
    default_bkg = makeBackground("placeholder.png", "placeholder")
    project.backgrounds.append(default_bkg)

    #a_scene = makeScene(f"Scene", default_bkg)
    #project.scenes.append(a_scene)

    checker_background_tile_list = getTileList(["black_tile.png", "white_tile.png"])
    checker_background_tile_array = makeCheckerboardArray(14, 14)
    checker_background_collisions = makeBackgroundCollisions(checker_background_tile_array)
    checker_background_image_path = generateBackgroundImageFromTiles(checker_background_tile_array, checker_background_tile_list)
    checker_background = makeBackground(checker_background_image_path, "checker_background")
    project.backgrounds.append(checker_background)
    a_scene = makeScene(f"Scene", checker_background)
    project.scenes.append(a_scene)

    checker_background = generateBackground("checker_background", checker_background_tile_array, checker_background_tile_list)
    print(checker_background)
    b_scene = makeScene(f"Scene", checker_background, collisions=checker_background_collisions)
    project.scenes.append(b_scene)

    actor = makeActor(a_rock_sprite, 9, 8)
    a_scene['actors'].append(actor)

    dog_actor = makeActor(a_dog_sprite, 5, 5)

    dog_script = []
    element = makeElement()
    element["command"] = "EVENT_ACTOR_EMOTE"
    element["args"] = {
      "actorId": "player",
      "emoteId": "1"
    }
    dog_script.append(element)
    element = makeElement()
    element["command"] = "EVENT_END"
    dog_script.append(element)
    dog_actor["script"] = dog_script


    a_scene['actors'].append(dog_actor)

    # Add some music
    project.music.append(makeMusic("template", "template.mod"))

    # Set the starting scene
    project.settings["startSceneId"] = project.scenes[0]["id"]
    return project

# Utilities
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

### Run the generator
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate a Game Boy ROM via a GB Studio project file.")
    parser.add_argument('--destination', '-d', type=str, help="destination folder name", default="../../gbprojects/projects_yourname/")
    args = parser.parse_args()
    initializeGenerator()
    project = createYourNameWorld()
    writeProjectToDisk(project, output_path = args.destination)
    if args.destination == "../gbprojects/projects/":
        print(f"{bcolors.WARNING}NOTE: Used default output directory, change with the -d flag{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}See generate.py --help for more options{bcolors.ENDC}")
