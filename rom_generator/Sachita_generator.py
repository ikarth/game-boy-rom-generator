import argparse
import copy
import random
from generator import makeBasicProject, addSpriteSheet, makeBackground, makeScene, makeActor, addSymmetricSceneConnections, makeMusic, reverse_direction, initializeGenerator, writeProjectToDisk
 
def SachitasGame():
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
   actor1 = makeActor(a_rock_sprite, 3, 8)
   duck_sprite = addSpriteSheet(project, "duck.png", "duck", "animated", 2)
   actor2 = makeActor(duck_sprite, 9, 10, "animated")
  
   # Add a background image
   default_bkg = makeBackground("stars.png", "stars")
   project.backgrounds.append(default_bkg)
 
   num = random.randint(1,20)
   for y in range(num):
       a_scene = copy.deepcopy(makeScene(f"Scene", default_bkg))
   if y%2 == 0:
       a_scene["actors"].append(actor1)
   if y%3 == 0:
       a_scene["actors"].append(actor2)
   project.scenes.append(a_scene)
 
   # Get information about the background
   bkg_x = default_bkg["imageWidth"]
   bkg_y = default_bkg["imageHeight"]
   bkg_width = default_bkg["width"]
   bkg_height = default_bkg["height"]
 
   actor = makeActor(a_rock_sprite, 9, 8)
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
   parser.add_argument('--assets', '-a', type=str, help="asset folder name", default="../assets/")
   args = parser.parse_args()
   initializeGenerator(asset_folder = args.assets)
   project = SachitasGame()
   writeProjectToDisk(project, output_path = args.destination)
   if args.destination == "../gbprojects/projects/":
       print(f"{bcolors.WARNING}NOTE: Used default output directory, change with the -d flag{bcolors.ENDC}")
       print(f"{bcolors.OKBLUE}See generate.py --help for more options{bcolors.ENDC}")