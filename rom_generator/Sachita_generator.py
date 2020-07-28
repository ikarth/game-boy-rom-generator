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

 duck_sprite = addSpriteSheet(project, "duck.png", "duck", "animated", 2)
 actor2 = makeActor(duck_sprite, 1, 30, "animated")
 doorway_sprite = addSpriteSheet(project, "tower.png", "tower", "static")
 actor3 = makeActor(doorway_sprite, 29, 2)
 a_rock_sprite = addSpriteSheet(project, "rock.png", "rock", "static")
 actor4 = makeActor(a_rock_sprite, 15, 30)
 
 a_rock_sprite = addSpriteSheet(project, "rock.png", "rock", "static")

  # Add a background image
 default_bkg = makeBackground("stars.png", "stars")
 project.backgrounds.append(default_bkg)
 a_scene = copy.deepcopy(makeScene(f"Scene", default_bkg))
 project.scenes.append(a_scene)
 #make a function for collisions
 
 # Get information about the background
 bkg_x = default_bkg["imageWidth"]
 bkg_y = default_bkg["imageHeight"]
 bkg_width = default_bkg["width"]
 bkg_height = default_bkg["height"]
 actor = makeActor(a_rock_sprite, 1, 1)
 actor2 = makeActor(duck_sprite, 5,5)
 a_scene['actors'].append(actor3)

 amount = random.randint(1, 5) 
 arr = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
 increment = 0
 #for x in range(amount): #choosing a random point and making a line of sprites. The amount is the loop #
  # increment = increment + 2
   #actor = makeActor(a_rock_sprite, xPos, increment, "static")
   #a_scene['actors'].append(actor)
 #amount = random.randint(1, 10)
 
 for i in range(1, 20):
   amount = random.randint(3, 5)
   xPos = random.randint(1, 30)
   yPos = random.randint(1, 30)
   increment = 0
   edgeBlock = 0
   while xPos == 31 or xPos == 30 or xPos == 29: 
    if arr[0][xPos-1] == 1:
      xPos = random.randint(3, 29)
      edgeBlock = 1
    else:
      edgeBlock = 1
      break
   while yPos == 31 or yPos == 30 or yPos == 29:
    if arr[1][yPos-1] == 1:
      yPos = random.randint(3, 29)
      edgeBlock = 1
    else: 
      edgeBlock = 1
      break
      #avoiding out of bounds error
    if edgeBlock == 1:
      actor = makeActor(a_rock_sprite, xPos - increment, yPos - increment, "static")
      a_scene['actors'].append(actor)
      increment = increment + 2

   while arr[0][xPos-1] == 1 or arr[0][xPos + 1] == 1 or arr[0][ xPos - 3] == 1:
      xPos = random.randint(3, 29)
   while arr[1][yPos-1] == 1 or arr[1][yPos + 1] == 1 or arr[1][yPos - 3] == 1:
      yPos = random.randint(3, 29)

   if(0 <= xPos <= 15) and (0 <= yPos <= 15): 
    choose = random.randint(1,2)
    if(choose == 1):
      for a in range (amount):
        increment = increment + 2
        actor = makeActor(a_rock_sprite, xPos, yPos + increment, "static")
        a_scene['actors'].append(actor)
        arr[0][ xPos-1] = 1
        arr[1][ yPos-1 + increment] = 1
    if(choose == 2):
      for b in range (amount):
        increment = increment + 2
        actor = makeActor(a_rock_sprite, xPos + increment, yPos, "static")
        a_scene['actors'].append(actor)
        arr[0][xPos-1 + increment] = 1
        arr[1][yPos-1] = 1

   if(0 <= xPos <= 15) and (15 <= yPos <= 28): 
      choose = random.randint(1,2)
      if(choose == 1):
        for c in range (amount):
          increment = increment + 2
          actor = makeActor(a_rock_sprite, xPos + increment, yPos, "static")
          a_scene['actors'].append(actor)
          arr[0][xPos -1 + increment] = 1
          arr[1][yPos-1] = 1
      if(choose == 2):
        for d in range (amount):
          increment = increment + 2
          actor = makeActor(a_rock_sprite, xPos, yPos - increment, "static")
          a_scene['actors'].append(actor)
          arr[0][xPos-1] = 1
          arr[1][yPos-1 + increment] = 1
          
   if(15 <= xPos <= 28) and (15 <= yPos <= 28): 
    choose = random.randint(1,2)
    if(choose == 1):
      for e in range (1, amount):
            actor = makeActor(a_rock_sprite, xPos, yPos - increment, "static")
            a_scene['actors'].append(actor)
            arr[0][xPos-1] = 1
            arr[1][yPos-1 - increment] = 1
    if(choose == 2):
      for f in range (1, amount):
        increment = increment + 2
        actor = makeActor(a_rock_sprite, xPos - increment, yPos, "static")
        a_scene['actors'].append(actor)
        arr[0][xPos-1 - increment] = 1
        arr[1][yPos-1] = 1
        increment = increment + 2

   if(15 <= xPos <= 28) and (0 <= yPos <= 15): 
    choose = random.randint(1,2)
    if(choose == 1):
      for g in range (1, amount):
        actor = makeActor(a_rock_sprite, xPos, yPos + increment, "static")
        a_scene['actors'].append(actor)
        arr[0][xPos-1] = 1
        arr[1][yPos -1 - increment] = 1
        increment = increment + 2
    if(choose == 2):
      for h in range (1, amount):
        actor = makeActor(a_rock_sprite, xPos - increment, yPos, "static")
        a_scene['actors'].append(actor)
        arr[0][xPos -1 + increment] = 1
        arr[1][yPos-1] = 1
        increment = increment + 2
 
 #import pdb; pdb.set_trace()
 # add a sprite to indicate the location of a doorway
 # a better way to do this in the actual levels is to alter the background image instead
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
  writeProjectToDisk(project, output_path = args.destination, assets_path="assets/") 
  if args.destination == "../gbprojects/projects/":
   print(f"{bcolors.WARNING}NOTE: Used default output directory, change with the -d flag{bcolors.ENDC}")
   print(f"{bcolors.OKBLUE}See generate.py --help for more options{bcolors.ENDC}")
