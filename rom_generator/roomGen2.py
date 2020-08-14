import argparse
import copy
import rom_generator.generator as gen
from rom_generator.generator import makeBasicProject, addSpriteSheet, makeBackground, makeScene, makeActor, addSymmetricSceneConnections, makeMusic, reverse_direction, initializeGenerator, writeProjectToDisk, makeKey, makeLock
import random
import rom_generator.combat as combat
import rom_generator.scriptFunctions2 as script2
import rom_generator.spriteSheetManager as manager
import rom_generator.mazes.maze as maze
import rom_generator.scenes.scene_gen_halls as sceneMethods

maxNumberOfEnemies = 7
maxSizeofASmallMaze = 4
maxNumOfLocksForSmallMaze = 1
maxNumOfLocksForABigMaze = 2
minNumOfLocksForABigMaze = 2
#Constants


sceneNum = 0
sceneA = gen.makeElement()
x2 = 0
y2 = 0
sceneList = []
backgroundNameList = []

def createConnection(scene, x, y):
    '''this creates a connection and a link at position x, y with the scene'''
    global connections, sceneA, x2, y2
    scene["actors"].append(gen.makeConnectionSprite(manager.findSpriteSheet("connectionSprite"), x, y))
    sceneA = scene
    x2 = x
    y2 = y

def finishConenctionBiDirectional(scene, x, y):
    pass

def finishConnection(scene, x, y):
    '''this finishes the connection from one scene to this scene at x, y'''
    global connections, sceneA, x2, y2
    gen.makeTriggerAndSwitchScene(
        sceneA, scene, x2, y2, x, y)


def createScene(sceneName = ""):
    '''This creates a scene with the background which has a name of sceneName'''
    global sceneNum
    scene = copy.deepcopy(
        gen.makeScene(f"Scene {sceneNum}", manager.findBackgroundSpriteSheet(sceneName), triggers = []))
    sceneNum += 1
    return scene

def start():
    '''This creates the start scene'''
    scene = createScene("startScene")
    connectionOut = manager.findOutConnection("startScene")
    index = random.randint(0, len(connectionOut) - 1)
    createConnection(scene, connectionOut[index][0], connectionOut[index][1])
    sceneList.append(scene)

def spawnEnemy(scene, index = 1):
    '''Spawns in index amount of enemies'''
    enemyList = []
    for i in range(index):  # spawns in the enemies
        x = random.randint(1, (scene["width"]-3))
        y = random.randint(2, scene["height"]-2)
        enemy = gen.makeActor(manager.findSpriteSheet("enemy"), x, y)
        enemyList.append(enemy)
        scene["actors"].append(enemy)

    '''

    ADD RANDOM WALK TO THE ENEMy

    '''

    weapon = gen.makeActor(manager.findSpriteSheet("weapon"), 0, 0)
    scene["actors"].append(weapon)
    # creates the combat system
    combat.setUpScene(scene, weapon, manager.findSpriteSheet("player")["id"], enemyList)

def room():
    '''This creates a room scene'''
    global backgroundNameList, maxNumberOfEnemies
    index = random.randint(0, len(backgroundNameList) - 1)
    sceneName = backgroundNameList[index]
    scene = createScene(sceneName)
    #creates the scene from a list of backgrounds

    connectionIn = manager.findInConnections(sceneName)
    index = random.randint(0, len(connectionIn) - 1)
    finishConnection(scene, connectionIn[index][0], connectionIn[index][1])
    #connections this scene 

    numEnemies = random.randint(1, maxNumberOfEnemies)
    spawnEnemy(scene, numEnemies)
    #spawns in the enemies

    connectionOut = manager.findOutConnection(sceneName)
    index = random.randint(0, len(connectionOut) - 1)
    createConnection(scene, connectionOut[index][0], connectionOut[index][1])
    #connections from this scene to another

    sceneList.append(scene)
    #adds scene to sceeList

def autoGeneration():
    '''this will be taking in the rooms from isaccs room genereator'''
    listAr = sceneMethods.sceneGenHallGrammar()
    #generates the maze
    
    connectionIn = manager.findInConnections(listAr[0])
    index = random.randint(0, len(connectionIn) - 1)

    finishConnection(listAr[1], connectionIn[index][0], connectionIn[index][1])
    #generates the connections into it

    connectionOut = manager.findOutConnection(listAr[0])
    index = random.randint(0, len(connectionOut) - 1)
    createConnection(listAr[1], connectionOut[index][0], connectionOut[index][1])
    #generates the out connection

    sceneList.append(listAr[1])

def smallMaze():
    '''This creates a small maze'''
    global maxSizeofASmallMaze, maxNumOfLocksForSmallMaze
    listAr = maze.generateKruskalMaze(maxSizeofASmallMaze, maxSizeofASmallMaze, random.randint(0, maxNumOfLocksForSmallMaze), manager.findSpriteSheet("key"), manager.findSpriteSheet("lock"))
    #generates the maze

    connectionIn = manager.findInConnections(listAr[0])
    index = random.randint(0, len(connectionIn) - 1)
    finishConnection(listAr[1], connectionIn[index][0], connectionIn[index][1])
    #generates the connections into it

    connectionOut = manager.findOutConnection(listAr[0])
    index = random.randint(0, len(connectionOut) - 1)
    createConnection(listAr[1], connectionOut[index][0], connectionOut[index][1])
    #generates the out connection

    sceneList.append(listAr[1])
    #adds the scene to overall sceneList



def makeRooms():
    '''Makes the rooms'''
    index = random.randint(0, 5)
    #probabilitie sto be changed
    if(index <= 1):
        room()
        makeRooms()
    elif(index <= 3):
        autoGeneration()
        makeRooms()
    elif(index == 4):
        smallMaze()

def makeMaze():
    '''This makes a big maze'''
    random.seed()
    global minNumOfLocksForABigMaze, maxNumOfLocksForABigMaze
    sizeOfMaze = random.randint(1, 1) * 8
    #make sure size 16 is possible
    listAr = maze.generateKruskalMaze(sizeOfMaze, sizeOfMaze, random.randint(minNumOfLocksForABigMaze, maxNumOfLocksForABigMaze), manager.findSpriteSheet("key"), manager.findSpriteSheet("lock"))

    connectionIn = manager.findInConnections(listAr[0])
    index = random.randint(0, len(connectionIn) - 1)
    finishConnection(listAr[1], connectionIn[index][0], connectionIn[index][1])
    #generates the connections into it

    connectionOut = manager.findOutConnection(listAr[0])
    index = random.randint(0, len(connectionOut) - 1)
    createConnection(listAr[1], connectionOut[index][0], connectionOut[index][1])
    #generates the out connection

    sceneList.append(listAr[1])
    #adds the scene to overall sceneList


def boss():
    '''TO BE UPDATED WITH A BOSS LEVEL'''
    autoGeneration()

def setUp(project):
    '''Sets up the games files'''
    global backgroundNameList
    random.seed()

    #these are the spriteSheets 2d Array (name, image, image, animation)
    #make sure hte player is in the firstbox
    #loss stands for "list of sprite sheet"
    loss = [
        ["player","actor_animated.png", "actor_animated", "actor_animated"],
        ["lock", "ice.png", "lock", "static"],
        ["key", "cat.png", "key", "static"],
        ["connectionSprite", "radio.png", "connection", "static"],
        ["enemy", "dog.png", "enemy", "static"],
        ["weapon", "torch.png", "weapon", "static"]
    ]

    for i in loss:
        a = gen.addSpriteSheet(project, i[1], i[2], i[3])
        manager.addSpriteSheet(i[0], a)
    #adds in the sprite sheet

    p = loss[0]
    project.settings["playerSpriteSheetId"] = manager.findSpriteSheet("player")["id"]
    #sets the player sprite sheet


    #sets up the background
    #lob stand for list of backgrounds, (name, spriteSheet)
    
    startScene = gen.makeBackground("placeholder.png", "placeholder")
    manager.addBackgroundSpriteSheet("startScene", startScene)
    manager.addInConnections("startScene", [[2, 5]])
    manager.addOutConnections("startScene", [[17, 15]])
    backgroundNameList.append("startScene")

    otherScene = gen.makeBackground("underground.png", "underground")
    name = "underground"
    manager.addBackgroundSpriteSheet(name, otherScene)
    manager.addInConnections(name, [[2, 5]])
    manager.addOutConnections(name, [[17, 15]])
    backgroundNameList.append(name)

    sceneMethods.setUpGenHallScenes()
    


def wrapUp(project):
    '''Wraps up the project'''
    manager.submitBackgroundSpriteSheets(project)
    #puts the backgrounds into the projcet

    for scene in sceneList:
        project.scenes.append(scene)
    #puts the scenes into hte project

    project.settings["startSceneId"] = project.scenes[0]["id"]
    #sets the starting scene loc

    project.music.append(gen.makeMusic("template", "template.mod"))
    #adds in music

def makeGame():
    '''Makes a game from grammar'''
    project = gen.makeBasicProject()
    #creates the project

    setUp(project)
    #sets up all neccessary projcet stuff

    start()
    makeRooms()
    makeMaze()
    boss()
    #creates the project from the grammar

    wrapUp(project)
    #wraps up any loose ends if required
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
    project = makeGame()
    writeProjectToDisk(project, output_path = args.destination)
    if args.destination == "../gbprojects/projects/":
        print(f"{bcolors.WARNING}NOTE: Used default output directory, change with the -d flag{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}See generate.py --help for more options{bcolors.ENDC}")
