import argparse
import copy
import rom_generator.generator as gen
import random
import rom_generator.combat as combat

sceneNum = 0
sceneA = gen.makeElement()
x2 = 0
y2 = 0
sceneList = []


default_bkg = gen.makeBackground("placeholder.png", "placeholder")
a_rock_sprite = {}
doorway_sprite = {}


def createConnection(scene, x, y):
    global connections, sceneA, x2, y2
    #scene["triggers"].append(gen.makeTrigger(scene, 3, 3, 2, 1, []))
    sceneA = scene
    x2 = x
    y2 = y


def finishConnection(scene, x, y):
    global connections, sceneA, x2, y2
    gen.makeTriggerAndSwitchScene(
        sceneA, scene, x2, y2, x, y)
    


def createScene(project):
    global sceneNum, default_bkg



    # Get information about the background
    bkg_x = default_bkg["imageWidth"]
    bkg_y = default_bkg["imageHeight"]
    bkg_width = default_bkg["width"]
    bkg_height = default_bkg["height"]

    a_scene = copy.deepcopy(
        gen.makeScene(f"Scene {sceneNum}", default_bkg, triggers = []))
    sceneNum += 1
    return copy.deepcopy( a_scene )




def start(project):
    a_scene = createScene(project)  # creates the scene

    #a_scene["triggers"].append(gen.makeTrigger(a_scene, 4, 4, 2, 1, []))
    # sets up the scene

    # ADD CONNECTIONS
    createConnection(a_scene, 2, 2)
    
    sceneList.append(a_scene)

    
    
    #project.settings["startSceneId"] = project.scenes[0]["id"]


def makeRooms(project):
    global a_rock_sprite
    a = random.randint(1, 4)
    if(a <= 3):
        a_scene = createScene(project)  # creates the scene
        finishConnection(a_scene, 3, 3)
        # Spawns in the weapon
        
        a_rock = gen.makeActor(a_rock_sprite, 5, 6)
        a_scene["actors"].append(a_rock)

        # spawns inthe enemies + combat system (max of 8 enemies)
        spawnEnemy(
            project, a_scene, a_rock, project.settings["playerSpriteSheetId"], random.randint(1, 8))

        # adds the scene to project
        sceneList.append(a_scene)

        # Add Connections

        createConnection(a_scene, 2, 2)
        makeRooms(project)


def spawnEnemy(project, scene, weapon, playerID, num):
    global doorway_sprite
    enemyList = []
    print(num)
    for i in range(num):  # spawns in the enemies
        actor_x = random.randint(1, (scene["width"]-3))
        actor_y = random.randint(2, scene["height"]-2)
        a_enemy = gen.makeActor(doorway_sprite, actor_x, actor_y)
        enemyList.append(a_enemy)
        scene["actors"].append(a_enemy)

    # creates the combat system
    combat.setUpScene(scene, weapon, playerID, enemyList)


def hallway(project):
    # creates the scene
    scene = createScene(project)
    global a_rock_sprite
    finishConnection(scene, 3, 3)

    # creates hte weapon
    #a_rock_sprite = gen.addSpriteSheet(project, "rock.png", "rock", "static")
    a_rock = gen.makeActor(a_rock_sprite, 5, 6)
    scene["actors"].append(a_rock)

    # spawns in the enemies + combat
    spawnEnemy(project, scene, a_rock, project.settings["playerSpriteSheetId"], 1)

    # adds scene to project
    sceneList.append(scene)

    # Add connection
    createConnection(scene, 2, 2)


def endBoss(project):
    hallway(project)
    endRoom(project)


def endRoom(project):
    # creates hte scene
    scene = createScene(project)
    global a_rock_sprite
    finishConnection(scene, 3, 3)

    # creates hte weapon
    #a_rock_sprite = gen.addSpriteSheet(project, "rock.png", "rock", "static")
    a_rock = gen.makeActor(a_rock_sprite, 5, 6)
    scene["actors"].append(a_rock)

    # spawns in the enemies + combat
    spawnEnemy(project, scene, a_rock, project.settings["playerSpriteSheetId"], 1)

    # puts scene in project
    sceneList.append(scene)


def makeGame():
    random.seed()
    project = gen.makeBasicProject()

    # Create sprite sheet for the player sprite
    player_sprite_sheet = gen.addSpriteSheet(
        project, "actor_animated.png", "actor_animated", "actor_animated")
    project.settings["playerSpriteSheetId"] = player_sprite_sheet["id"]

    global default_bkg, a_rock_sprite, doorway_sprite
    project.backgrounds.append(default_bkg)
    a_rock_sprite = gen.addSpriteSheet(project, "rock.png", "rock", "static")
    doorway_sprite = gen.addSpriteSheet(
            project, "tower.png", "tower", "static")

    start(project)
    makeRooms(project)
    endBoss(project)

    for scene in sceneList:
        project.scenes.append(scene)

    project.settings["startSceneId"] = project.scenes[0]["id"]
    project.music.append(gen.makeMusic("template", "template.mod"))
    return project


