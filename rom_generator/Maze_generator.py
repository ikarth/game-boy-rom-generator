import argparse
import copy
import random
from generator import makeSpriteSheet, makeBasicProject, addSpriteSheet, makeBackground, makeScene, makeActor, addSymmetricSceneConnections, makeMusic, reverse_direction, initializeGenerator, writeProjectToDisk

def generatemaze():
    project = makeBasicProject()

    a_border_sprite = addSpriteSheet(project, "GreenBlock.png", "GreenBlock", "static", "none")
    border = makeActor(a_border_sprite, 1, 2, "static")
    border = makeActor(a_border_sprite, 1, 9, "static")
    border = makeActor(a_border_sprite, 1, 16, "static")
    border = makeActor(a_border_sprite, 2, 2, "static")
    border = makeActor(a_border_sprite, 2, 9, "static")
    border = makeActor(a_border_sprite, 2, 10, "static")
    border = makeActor(a_border_sprite, 2, 11, "static")
    border = makeActor(a_border_sprite, 2, 12, "static")
    border = makeActor(a_border_sprite, 2, 13, "static")
    border = makeActor(a_border_sprite, 2, 14, "static")
    border = makeActor(a_border_sprite, 2, 16, "static")
    border = makeActor(a_border_sprite, 3, 6, "static")
    border = makeActor(a_border_sprite, 3, 9, "static")
    border = makeActor(a_border_sprite, 3, 16, "static")
    border = makeActor(a_border_sprite, 4, 6, "static")
    border = makeActor(a_border_sprite, 4, 16, "static")
    border = makeActor(a_border_sprite, 5, 1, "static")
    border = makeActor(a_border_sprite, 5, 2, "static")
    border = makeActor(a_border_sprite, 5, 3, "static")
    border = makeActor(a_border_sprite, 5, 4, "static")
    border = makeActor(a_border_sprite, 5, 5, "static")
    border = makeActor(a_border_sprite, 5, 6, "static")
    border = makeActor(a_border_sprite, 5, 16, "static")
    border = makeActor(a_border_sprite, 6, 2, "static")
    border = makeActor(a_border_sprite, 6, 6, "static")
    border = makeActor(a_border_sprite, 6, 10, "static")
    border = makeActor(a_border_sprite, 6, 11, "static")
    border = makeActor(a_border_sprite, 6, 12, "static")
    border = makeActor(a_border_sprite, 6, 13, "static")
    border = makeActor(a_border_sprite, 6, 14, "static")
    border = makeActor(a_border_sprite, 6, 15, "static")
    border = makeActor(a_border_sprite, 6, 16, "static")
    border = makeActor(a_border_sprite, 7, 2, "static")
    border = makeActor(a_border_sprite, 7, 6, "static")
    border = makeActor(a_border_sprite, 7, 16, "static")
    border = makeActor(a_border_sprite, 8, 2, "static")
    border = makeActor(a_border_sprite, 8, 12, "static")
    border = makeActor(a_border_sprite, 8, 13, "static")
    border = makeActor(a_border_sprite, 8, 14, "static")
    border = makeActor(a_border_sprite, 8, 16, "static")
    border = makeActor(a_border_sprite, 9, 8, "static")
    border = makeActor(a_border_sprite, 9, 10, "static")
    border = makeActor(a_border_sprite, 9, 16, "static")
    border = makeActor(a_border_sprite, 10, 4, "static")
    border = makeActor(a_border_sprite, 10, 5, "static")
    border = makeActor(a_border_sprite, 10, 6, "static")
    border = makeActor(a_border_sprite, 10, 7, "static")
    border = makeActor(a_border_sprite, 10, 8, "static")
    border = makeActor(a_border_sprite, 10, 10, "static")
    border = makeActor(a_border_sprite, 10, 16, "static")
    border = makeActor(a_border_sprite, 11, 4, "static")
    border = makeActor(a_border_sprite, 11, 8, "static")
    border = makeActor(a_border_sprite, 11, 10, "static")
    border = makeActor(a_border_sprite, 11, 13, "static")
    border = makeActor(a_border_sprite, 11, 14, "static")
    border = makeActor(a_border_sprite, 11, 15, "static")
    border = makeActor(a_border_sprite, 11, 16, "static")
    border = makeActor(a_border_sprite, 12, 4, "static")
    border = makeActor(a_border_sprite, 12, 7, "static")
    border = makeActor(a_border_sprite, 12, 8, "static")
    border = makeActor(a_border_sprite, 12, 16, "static")
    border = makeActor(a_border_sprite, 13, 4, "static")
    border = makeActor(a_border_sprite, 13, 12, "static")
    border = makeActor(a_border_sprite, 13, 16, "static")
    border = makeActor(a_border_sprite, 14, 4, "static")
    border = makeActor(a_border_sprite, 14, 12, "static")
    border = makeActor(a_border_sprite, 14, 16, "static")
    border = makeActor(a_border_sprite, 15, 1, "static")
    border = makeActor(a_border_sprite, 15, 2, "static")
    border = makeActor(a_border_sprite, 15, 3, "static")
    border = makeActor(a_border_sprite, 15, 4, "static")
    border = makeActor(a_border_sprite, 15, 12, "static")
    border = makeActor(a_border_sprite, 15, 16, "static")
    border = makeActor(a_border_sprite, 16, 12, "static")
    border = makeActor(a_border_sprite, 16, 13, "static")
    border = makeActor(a_border_sprite, 16, 14, "static")
    border = makeActor(a_border_sprite, 16, 15, "static")
    border = makeActor(a_border_sprite, 16, 16, "static")
    project.settings["playerSpriteSheetId"] = a_border_sprite["id"]

   # Add a background image
    default_bkg = makeBackground("placeholder.png", "placeholder")
    project.backgrounds.append(default_bkg) 
    a_scene = copy.deepcopy(makeScene("Scene", default_bkg))
    project.scenes.append(a_scene)

    # Get information about the background
    bkg_x = default_bkg["imageWidth"]
    bkg_y = default_bkg["imageHeight"]
    bkg_width = default_bkg["width"]
    bkg_height = default_bkg["height"]

    actor = makeActor(a_border_sprite, 9, 8)
    a_scene['actors'].append(actor)
    #import pdb; pdb.set_trace()

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

### Run the generator
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate a Game Boy ROM via a GB Studio project file.")
    parser.add_argument('--destination', '-d', type=str, help="destination folder name", default="../gbprojects/projects/")
    parser.add_argument('--assets', '-a', type=str, help="asset folder name", default="assets/")
    args = parser.parse_args()
    initializeGenerator(asset_folder = args.assets)
    project = generatemaze()
    writeProjectToDisk(project, output_path = args.destination)
    if args.destination == "../gbprojects/projects/":
        print(f"{bcolors.WARNING}NOTE: Used default output directory, change with the -d flag{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}See generate.py --help for more options{bcolors.ENDC}")


