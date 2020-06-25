import argparse
import copy
import random
from generator import makeBasicProject, addSpriteSheet, makeBackground, makeScene, makeActor, addSymmetricSceneConnections, makeMusic, reverse_direction, initializeGenerator, writeProjectToDisk

def createRockWorld():
    # Set up a barebones project
    project = makeBasicProject()

    # Create sprite sheet for the player sprite
    player_sprite_sheet = addSpriteSheet(project, "actor_animated.png", "actor_animated", "actor_animated")
    project.settings["playerSpriteSheetId"] = player_sprite_sheet["id"]

    # add a sprite we can use for the rocks
    a_rock_sprite = addSpriteSheet(project, "rock.png", "rock", "static")

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
    doorway_sprite = addSpriteSheet(project, "tower.png", "tower", "static")

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
    parser.add_argument('--destination', '-d', type=str, help="destination folder name", default="../gbprojects/projects/")
    parser.add_argument('--assets', '-a', type=str, help="asset folder name", default="assets/")
    args = parser.parse_args()
    initializeGenerator(asset_folder = args.assets)
    project = createRockWorld()
    writeProjectToDisk(project, output_path = args.destination)
    if args.destination == "../gbprojects/projects/":
        print(f"{bcolors.WARNING}NOTE: Used default output directory, change with the -d flag{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}See generate.py --help for more options{bcolors.ENDC}")
