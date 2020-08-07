import argparse
import copy
import random
from datetime import datetime
from generator import makeBasicProject, makeElement, makeColBorder, makeCol, genQuestions, addSpriteSheet, makeBackground, makeScene, makeActor, addSymmetricSceneConnections, makeMusic, reverse_direction, initializeGenerator, writeProjectToDisk

def vijayaGame():

    # Set up a barebones project
    project = makeBasicProject()

    # Create sprite sheet for the player sprite
    player_sprite_sheet = addSpriteSheet(
        project, "player.png", "player", "player")
    project.settings["playerSpriteSheetId"] = player_sprite_sheet["id"]

    # add sprites
    a_rock_sprite = addSpriteSheet(project, "rock.png", "rock", "static")
    doorway_sprite = addSpriteSheet(project, "tower.png", "tower", "static")
    duck_sprite = addSpriteSheet(project, "duck.png", "duck", "animated", 2)
    a_dog_sprite = addSpriteSheet(project, "dog.png", "dog", "static")

    # Adding actors
    actor = makeActor(a_rock_sprite, 9, 8)
    actor2 = makeActor(a_rock_sprite, 2, 3)
    actor3 = makeActor(duck_sprite, 9, 10, "animated", True)

    # Testing genQuestions with dog actor
    dog_actor = makeActor(a_dog_sprite, 7, 8)
    dog_script = []
    genQuestions('mc.txt', dog_script)
    dog_actor["script"] = dog_script

    # Add a background image
    default_bkg = makeBackground("placeholder.png", "placeholder")
    project.backgrounds.append(default_bkg)

    # Add scenes with some actors
    a_scene2 = copy.deepcopy(makeScene(f"Scene", default_bkg))
    a_scene2["actors"].append(dog_actor)
    project.scenes.append(copy.deepcopy(a_scene2))
    
    # Randomly generate num of scenes
    random.seed(datetime.now())
    num = random.randint(1, 20)
    for y in range(num):
        a_scene = copy.deepcopy(makeScene(f"Scene", default_bkg))   
        makeColBorder(a_scene)    
        if y%2 == 0:
            a_scene["actors"].append(actor)
        if y%3 == 0:
            a_scene["actors"].append(actor3)
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
                    addSymmetricSceneConnections(project, project.scenes[y], project.scenes[other_scene], chosen_direction, doorway_sprite)
                    break

    # Get information about the background
    bkg_x = default_bkg["imageWidth"]
    bkg_y = default_bkg["imageHeight"]
    bkg_width = default_bkg["width"]
    bkg_height = default_bkg["height"]

    # add a sprite to indicate the location of a doorway
    # a better way to do this in the actual levels is to alter the background image instead
    doorway_sprite = addSpriteSheet(project, "tower.png", "tower", "static")

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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate a Game Boy ROM via a GB Studio project file.")
    parser.add_argument('--destination', '-d', type=str, help="destination folder name", default="../../gbprojects/projects/")
    parser.add_argument('--assets', '-a', type=str, help="asset folder name", default="../assets/")
    parser.add_argument('--subfolder', '-s', type=bool, help="asset folder name", default=False)
    args = parser.parse_args()
    initializeGenerator(asset_folder=args.assets)
    project = vijayaGame()
    writeProjectToDisk(project, output_path = args.destination)

    if args.destination == "../gbprojects/projects/":
        print(f"{bcolors.WARNING}NOTE: Used default output directory, change with the -d flag{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}See generate.py --help for more options{bcolors.ENDC}")
