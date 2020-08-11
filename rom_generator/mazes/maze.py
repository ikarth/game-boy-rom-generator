import argparse
import copy
import random
from rom_generator.generator import makeSpriteSheet, makeBasicProject, addSpriteSheet, makeBackground, makeScene, makeActor, addSymmetricSceneConnections, makeMusic, reverse_direction, initializeGenerator, writeProjectToDisk, addActor, makeCol, makeLock, makeKey
import rom_generator.background as background
import numpy
from rom_generator.mazes.mazeGen import run, getList
import rom_generator.spriteSheetManager as manager


index = 0

class pair():
    def __init__(self, aa, bb, cc):
        self.x = aa
        self.y = bb
        self.counter = cc 


def dfs(x, y, counter, mazeArray):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = []
    queue.append(pair(0, 0, 1))

    while len(queue) > 0:
        x = queue[0].x
        y = queue[0].y
        counter = queue[0].counter
        mazeArray[x][y] = counter
        queue.pop(0)
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if xx >= 0 and xx < len(mazeArray) and yy >= 0 and yy < len(mazeArray[0]) and mazeArray[xx][yy] == 0:
                queue.append(pair(xx, yy, counter + 1))

def generateKruskalMaze(size_x, size_y, num_lock, keySprite, lockSprite):
    

      # Add a background image
    #default_bkg = makeBackground("placeholder.png", "placeholder")
    #project.backgrounds.append(default_bkg)
    #a_scene = makeScene("Scene", default_bkg)
    #project.scenes.append(a_scene)

    #size_x, size_y = (8, 8)
    maze_tile_names = ["GreenBlock8.png","MazeBlock8.png"]
    maze_tile_list = background.getTileList(maze_tile_names)
    maze_tile_array = [[0 for n in range(size_y * 3)] for m in range(size_x * 3)]
    maze_collisions = [[0 for n in range(size_y * 3)] for m in range(size_x * 3)]
    def addBackgroundTile(tile_num, x, y):
        #print(x,y)
        maze_tile_array[x][y] = tile_num
        maze_collisions[x][y] = 1
        return maze_tile_array
    #print(maze_tile_list)

    maze_wall_tile = maze_tile_names.index("MazeBlock8.png")

    run(size_x)

    array = getList()

    #print("lengt " + str(len(array)))

    mazeArray = [[0 for a in range(size_y * 3)] for b in range(size_x * 3)]
    sizey = size_y * 2
    sizex = size_x * 3
    
    #print("SETTING THE TILES")
    counter = 0
    for i in range(len(array)):
        for j in range(len(array)):
            #print("Index " + str(i) + " " + str(j))
            temp = array[i][j]
            if temp.ar[1] == False:
                mazeArray[2*i+1][3*j+1] = -1
                mazeArray[2*i+1][3*j] = -1
                addBackgroundTile(maze_wall_tile, 2 * i + 1, 3 * j + 1)
                addBackgroundTile(maze_wall_tile, 2 * i + 1, 3 * j)
            if temp.ar[0] == False:
                mazeArray[2*i][3*j+2] = -1
                addBackgroundTile(maze_wall_tile, 2 * i, 3 * j + 2)
            mazeArray[2*i+1][3*j+2] = -1
            addBackgroundTile(maze_wall_tile, 2 * i + 1, 3 * j + 2)
            #print(counter)
            counter += 1


    dfs(0, 0, 1, mazeArray) #this is bfs now

    #print("Maze is")
    #print(mazeArray)

    flat = numpy.array(mazeArray).flatten(order='C').tolist()
    # for y in range(numpy.array(mazeArray).shape[1]):
    #     print()
    #     for x in range(numpy.array(mazeArray).shape[0]):
    #         print(flat[x + (y * numpy.array(mazeArray).shape[0])], end='')
    # print()

    global index
    maze_background_image_path = background.generateBackgroundImageFromTiles(maze_tile_array, maze_tile_list)
    maze_background = makeBackground(maze_background_image_path, "maze_background")
    nameBackground = "maze_background" + str(index)
    manager.addBackgroundSpriteSheet(nameBackground, maze_background)
    manager.addInConnections(nameBackground, [[0, 0]])
    manager.addOutConnections(nameBackground, [[sizex - 2, sizey - 2]])
    index+=1
    a_scene = makeScene(f"Scene" + str(index), maze_background)

    #flat_maze_collisions = numpy.rot90(numpy.array(maze_collisions), 2, axes=(0,1)).flatten(order='C').tolist()
    flat_maze_collisions = numpy.array(maze_collisions).flatten(order='C').tolist()
    # for y in range(numpy.array(maze_collisions).shape[1]):
    #     print()
    #     for x in range(numpy.array(maze_collisions).shape[0]):
    #         print(flat_maze_collisions[x + (y * numpy.array(maze_collisions).shape[0])], end='')
    # print()

    makeCol(flat_maze_collisions, a_scene)
    #print(maze_background)

    #print(a_scene)
    sizex -= 1
    sizey -=1
    for i in range(num_lock):
        intx = random.randint(0, sizex)
        inty = random.randint(0, sizey)
        while(mazeArray[inty][intx] == -1 or (intx + 1 > sizex and mazeArray[inty][intx+1] == -1)):
            intx = random.randint(0, sizex)
            inty = random.randint(0, sizey)

        intx2 = random.randint(0, sizex)
        inty2 = random.randint(0, sizey)
        while(mazeArray[inty2][intx2] == -1 or (intx2+1>sizex and mazeArray[inty2][intx2+1]==-1)):
            intx2 = random.randint(0, sizex)
            inty2 = random.randint(0, sizey)

        if(mazeArray[inty][intx] > mazeArray[inty2][intx2]):
            inttemp = intx
            intx = intx2
            intx2 = inttemp
            inttemp = inty
            inty = inty2
            inty2 = inttemp

        # print("coords")
        # print(intx)
        # print(inty)
        # print(intx2)
        # print(inty2)
        # print("MAZE DEPTH COMP")
        # print(mazeArray[inty][intx])
        # print(mazeArray[inty2][intx2])
        a_scene["actors"].append(makeKey(keySprite, intx, inty))
        a_scene["actors"].append(makeLock(lockSprite, intx2, inty2))

        

        
    return [nameBackground, a_scene]


def generatemaze():
    project = makeBasicProject()

      # Add a background image
    #default_bkg = makeBackground("placeholder.png", "placeholder")
    #project.backgrounds.append(default_bkg)
    #a_scene = makeScene("Scene", default_bkg)
    #project.scenes.append(a_scene)

    size_x, size_y = (19, 19)
    maze_tile_names = ["GreenBlock8.png","MazeBlock8.png"]
    maze_tile_list = background.getTileList(maze_tile_names)
    maze_tile_array = [[0 for n in range(size_y)] for m in range(size_x) ]
    maze_collisions = [[0 for n in range(size_y)] for m in range(size_x)]
    def addBackgroundTile(tile_num, x, y):
        #print(x,y)
        maze_tile_array[x][y] = tile_num
        maze_collisions[x][y] = 1
        return maze_tile_array
    #print(maze_tile_list)

    maze_wall_tile = maze_tile_names.index("MazeBlock8.png")
    tile_placement_list = [(1, 2), (1, 9), (1, 16),(2, 2),(2, 9),(2, 10),(2, 11),(2, 12),(2, 13),(2, 14),(2, 16),(3, 6),(3, 9),(3, 16),(4, 6),(4, 16),(5, 1),(5, 2),(5, 3),(5, 4),(5, 5),(5, 6),(5, 16),(6, 2),(6, 6),(6, 10),(6, 11),(6, 12),(6, 13), (6, 14), (6, 15), (6, 16), (7, 2), (7, 6), (7, 16), (8, 2), (8, 12), (8, 13), (8, 14), (8, 16), (9, 8), (9, 10), (9, 16), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 10), (10, 16), (11, 4), (11, 8), (11, 10), (11, 13), (11, 14), (11, 15), (11, 16), (12, 4), (12, 7), (12, 8), (12, 16), (13, 4), (13, 12), (13, 16), (14, 4), (14, 12), (14, 16), (15, 1), (15, 2), (15, 3), (15, 4), (15, 12), (15, 16), (16, 12), (16, 13), (16, 14), (16, 15), (16, 16)]
    for x,y in tile_placement_list:
        addBackgroundTile(maze_wall_tile, x, y)

    maze_background_image_path = background.generateBackgroundImageFromTiles(maze_tile_array, maze_tile_list)
    maze_background = makeBackground(maze_background_image_path, "maze_background")
    project.backgrounds.append(maze_background)
    a_scene = makeScene(f"Scene", maze_background)

    #flat_maze_collisions = numpy.rot90(numpy.array(maze_collisions), 2, axes=(0,1)).flatten(order='C').tolist()
    flat_maze_collisions = numpy.array(maze_collisions).flatten(order='C').tolist()
    for y in range(numpy.array(maze_collisions).shape[1]):
        print()
        for x in range(numpy.array(maze_collisions).shape[0]):
            print(flat_maze_collisions[x + (y * numpy.array(maze_collisions).shape[0])], end='')
    print()

    makeCol(flat_maze_collisions, a_scene)
    print(maze_background)
    project.scenes.append(a_scene)
    print(a_scene)

    player_sprite_sheet = addSpriteSheet(project, "actor_animated.png", "actor_animated", "actor_animated")
    project.settings["playerSpriteSheetId"] = player_sprite_sheet["id"]

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
    parser.add_argument('--destination', '-d', type=str, help="destination folder name", default="../gbprojects/projects_maze2/")
    parser.add_argument('--assets', '-a', type=str, help="asset folder name", default="assets/")
    args = parser.parse_args()
    initializeGenerator()
    project = makeBasicProject()
    a_rock_sprite = addSpriteSheet(project, "rock.png", "rock", "static")
    doorway_sprite = addSpriteSheet(project, "tower.png", "tower", "static")
    l = generateKruskalMaze(8, 8, 2, a_rock_sprite, doorway_sprite)
    project.scenes.append(l[1])
    manager.submitBackgroundSpriteSheets(project)
    player_sprite_sheet = addSpriteSheet(project, "actor_animated.png", "actor_animated", "actor_animated")
    project.settings["playerSpriteSheetId"] = player_sprite_sheet["id"]

    # Add some music
    project.music.append(makeMusic("template", "template.mod"))

    # Set the starting scene
    project.settings["startSceneId"] = project.scenes[0]["id"]

    writeProjectToDisk(project, output_path = args.destination)
    if args.destination == "../gbprojects/projects/":
        print(f"{bcolors.WARNING}NOTE: Used default output directory, change with the -d flag{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}See generate.py --help for more options{bcolors.ENDC}")
