import argparse
import copy
import random
from rom_generator.generator import makeBasicProject, addSpriteSheet, makeBackground, makeScene, makeActor, addSymmetricSceneConnections, makeMusic, reverse_direction, initializeGenerator, writeProjectToDisk, makeKey, makeLock
from rom_generator.script_functions import actorHide, end
import rom_generator.combat as combat
import rom_generator.roomGen as roomGen
def AnikaProject123():
    """
    This is my change
    """
    pass


def SachitasGame():
    pass


def Harvin():
    pass


def createVijayaWorld():
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

    a_scene = makeScene(f"Scene Zero", default_bkg)
    # Add scene to project
    project.scenes.append(a_scene)

    # Add some music
    project.music.append(makeMusic("template", "template.mod"))
    project.settings["startSceneId"] = project.scenes[0]["id"]
    return project

def aaronTest():
    project = makeBasicProject()

    # Create sprite sheet for the player sprite
    player_sprite_sheet = addSpriteSheet(
        project, "actor_animated.png", "actor_animated", "actor_animated")
    project.settings["playerSpriteSheetId"] = player_sprite_sheet["id"]

    # add a sprite we can use for the rocks
    a_rock_sprite = addSpriteSheet(project, "rock.png", "rock", "static")

    doorway_sprite = addSpriteSheet(project, "tower.png", "tower", "static")

    # Add a background image
    default_bkg = makeBackground("placeholder.png", "placeholder")
    project.backgrounds.append(default_bkg)

    # Get information about the background
    bkg_x = default_bkg["imageWidth"]
    bkg_y = default_bkg["imageHeight"]
    bkg_width = default_bkg["width"]
    bkg_height = default_bkg["height"]

    a_scene = copy.deepcopy(
            makeScene(f"Scene {1}", default_bkg))

    key = makeActor(a_rock_sprite, 2, 2)
    key2 = makeActor(a_rock_sprite, 3, 3)
    key3 = makeActor(a_rock_sprite, 7, 7)

    weapon = makeActor(doorway_sprite, 5, 5)

    combat.setUpScene(a_scene, weapon, player_sprite_sheet["id"], [key, key2, key3])

    a_scene["actors"].append(key)
    a_scene["actors"].append(key2)
    a_scene["actors"].append(key3)
    a_scene["actors"].append(weapon)

    project.scenes.append(copy.deepcopy(a_scene))

    project.music.append(makeMusic("template", "template.mod"))

    # Set the starting scene
    project.settings["startSceneId"] = project.scenes[0]["id"]

    return project

def createAaronGame():
    project = makeBasicProject()

    # Create sprite sheet for the player sprite
    player_sprite_sheet = addSpriteSheet(
        project, "actor_animated.png", "actor_animated", "actor_animated")
    project.settings["playerSpriteSheetId"] = player_sprite_sheet["id"]

    # add a sprite we can use for the rocks
    a_rock_sprite = addSpriteSheet(project, "rock.png", "rock", "static")

    doorway_sprite = addSpriteSheet(project, "tower.png", "tower", "static")

    # Add a background image
    default_bkg = makeBackground("placeholder.png", "placeholder")
    project.backgrounds.append(default_bkg)

    # Get information about the background
    bkg_x = default_bkg["imageWidth"]
    bkg_y = default_bkg["imageHeight"]
    bkg_width = default_bkg["width"]
    bkg_height = default_bkg["height"]

    a_scene = copy.deepcopy(
            makeScene(f"Scene {1}", default_bkg))

    key = makeKey(a_rock_sprite, 2, 2)
    a_scene["actors"].append(key)
    lock = makeLock(doorway_sprite, 4, 5)
    a_scene["actors"].append(lock)

    key2 = makeKey(a_rock_sprite, 6, 6)
    a_scene["actors"].append(key2)

    lock2= makeLock(doorway_sprite, 7, 7)
    a_scene["actors"].append(lock2)


    project.scenes.append(copy.deepcopy(a_scene))

    project.music.append(makeMusic("template", "template.mod"))

    # Set the starting scene
    project.settings["startSceneId"] = project.scenes[0]["id"]

    return project


def createRockWorld():
        # Set up a barebones project
    project = makeBasicProject()

    # Create sprite sheet for the player sprite
    player_sprite_sheet = addSpriteSheet(
        project, "actor_animated.png", "actor_animated", "actor_animated")
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
        a_scene = copy.deepcopy(
            makeScene(f"Scene {make_scene_num}", default_bkg))
        # Create an actor
        for x in range(2): # Maximum number of actors in GB Studio is 9
            actor_x = random.randint(1,(bkg_width-3)) # Second value subtracted by 1 to keep sprite within bounds of the screen
            actor_y = random.randint(2,bkg_height-2) # First value added by 1 to keep sprite within bounds of the screen
            a_rock = makeKey(a_rock_sprite, 5, 6)
            a_scene["actors"].append(a_rock)
        # Add scene to project
        project.scenes.append(copy.deepcopy(a_scene))

    # Add some connections between the scenes.
    # This just throws down a bunch of random connections and tries to
    # make sure that they don't overlap
    scene_connections_translations = {
        "right": 0, "left": 1, "up": 2, "down": 3}
    scene_connections = [[True, True, True, True]
                         for n in range(number_of_scenes_to_make)]
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
                    addSymmetricSceneConnections(
                        project, project.scenes[y], project.scenes[other_scene], chosen_direction, doorway_sprite)
                    break

    # Add some music
    project.music.append(makeMusic("template", "template.mod"))

    # Set the starting scene
    project.settings["startSceneId"] = project.scenes[0]["id"]
    return project

def grammarTest():
    return roomGen.makeGame()
    


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
    parser = argparse.ArgumentParser(
        description="Generate a Game Boy ROM via a GB Studio project file.")
    parser.add_argument('--destination', '-d', type=str,
                        help="destination folder name", default="../gbprojects/projects2/")
    args = parser.parse_args()

    initializeGenerator()
    project = grammarTest()
    writeProjectToDisk(project, output_path=args.destination)

    if args.destination == "../gbprojects/projects/":
        print(f"{bcolors.WARNING}NOTE: Used default output directory, change with the -d flag{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}See generate.py --help for more options{bcolors.ENDC}")


