import argparse
import copy
import random
from generator import makeElement, makeBasicProject, addSpriteSheet, makeBackground, makeScene, makeActor, addSymmetricSceneConnections, makeMusic, reverse_direction, initializeGenerator, writeProjectToDisk, addSceneBackground, makeCol, makeColBorder
from background import getTileList, makeCheckerboardArray, generateBackgroundImageFromTiles, generateBackground, makeBackgroundCollisions


def spriteChangeHarvin():

    # Set up a barebones project
    project = makeBasicProject()

    # Create sprite sheet for the player sprite
    player_sprite_sheet = addSpriteSheet(
        project, "player.png", "player", "player")
    project.settings["playerSpriteSheetId"] = player_sprite_sheet["id"]

    # add sprites
    a_rock_sprite = addSpriteSheet(project, "rock.png", "rock", "static")
    a_dog_sprite = addSpriteSheet(project, "dog.png", "dog", "static")

    # Adding actors
    actor = makeActor(a_rock_sprite, 9, 8)
    rock_script = []
    element = makeElement()
    element["command"] = "EVENT_PLAYER_SET_SPRITE"
    element["args"] = {
        "spriteSheetId": "7f5d7c09-6fca-4107-a6fe-cd370e64e667",
        "__collapse": True
    }
    rock_script.append(element)
    element = makeElement()
    element["command"] = "EVENT_END"
    rock_script.append(element)
    actor["script"] = rock_script
   
    #dog script
    dog_actor = makeActor(a_dog_sprite, 5, 6)
    dog_script = []
    element = makeElement()
    element["command"] = "EVENT_PLAYER_SET_SPRITE"
    element["args"] = {
        "spriteSheetId": "7f5d7c09-6fca-4107-a6fe-cd370e64e667",
        "__collapse": True
    }
    dog_script.append(element)
    element = makeElement()
    element["command"] = "EVENT_END"
    dog_script.append(element)
    dog_actor["script"] = dog_script

    # Add a background image
    default_bkg = makeBackground("placeholder.png", "placeholder")
    project.backgrounds.append(default_bkg)

    # Add scenes with some actors
    a_scene2 = copy.deepcopy(makeScene(f"Scene", default_bkg))
    a_scene2["actors"].append(dog_actor)
    scene2_script = []
    element = makeElement()
    project.scenes.append(copy.deepcopy(a_scene2))
    random.seed(1)
    num = random.randint(1, 20)
    print ("this is num: ")
    print (num)
    for y in range(num):
        a_scene = copy.deepcopy(makeScene(f"Scene", default_bkg))
     #   makeColBorder(a_scene)
        if y%2 == 0:
            a_scene["actors"].append(actor)
        project.scenes.append(copy.deepcopy(a_scene))

    # Adding connections
    scene_connections_translations = {"right":0, "left":1, "up":2, "down":3}
    scene_connections = [[True, True, True, True] for n in range(num)]
    for y in range(num):
        for attempts in range(num):
            other_scene = random.randint(0, num - 2)
            if other_scene >= y:
                other_scene += 1
            chosen_direction = random.choice(["right", "left", "up", "down"])
            if scene_connections[y][scene_connections_translations[chosen_direction]]:
                if scene_connections[other_scene][scene_connections_translations[reverse_direction[chosen_direction]]]:
                    scene_connections[y][scene_connections_translations[chosen_direction]] = False
                    scene_connections[other_scene][scene_connections_translations[reverse_direction[chosen_direction]]] = False
              #      addSymmetricSceneConnections(project, project.scenes[y], project.scenes[other_scene], chosen_direction, doorway_sprite)
                    break

    # Get information about the background
    bkg_x = default_bkg["imageWidth"]
    bkg_y = default_bkg["imageHeight"]
    bkg_width = default_bkg["width"]
    bkg_height = default_bkg["height"]


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


# Run the generator
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate a Game Boy ROM via a GB Studio project file.")
    parser.add_argument('--destination', '-d', type=str, help="destination folder name", default="../gbprojects/projects3/")
    args = parser.parse_args()
    initializeGenerator()
    project = spriteChangeHarvin()
    writeProjectToDisk(project, output_path = args.destination)

    if args.destination == "../gbprojects/projects/":
        print(f"{bcolors.WARNING}NOTE: Used default output directory, change with the -d flag{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}See generate.py --help for more options{bcolors.ENDC}")