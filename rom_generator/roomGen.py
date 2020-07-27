import generator as gen
import random
import combat as combat

sceneNum = 0
connection = []


def createConnection(scene, x, y):
    connections.append(scene)
    connections.append(x)
    connections.append(y)


def finishConnection(scene, x, y):
    gen.makeTriggerAndSwitchScene(
        connections[0], scene, connections[1], connections[2], x, y)
    connections = []


def createScene(project):
    global sceneNum

    default_bkg = makeBackground("placeholder.png", "placeholder")
    project.backgrounds.append(default_bkg)

    # Get information about the background
    bkg_x = default_bkg["imageWidth"]
    bkg_y = default_bkg["imageHeight"]
    bkg_width = default_bkg["width"]
    bkg_height = default_bkg["height"]

    a_scene = copy.deepcopy(
        makeScene(f"Scene {sceneNum}", default_bkg))
    sceneNum += 1
    return a_scene




def start(project):
    a_scene = createScene(project)  # creates the scene
    project["scene"].append(a_scene)

    # sets up the scene
    project.settings["startSceneId"] = project.scenes[0]["id"]
    # ADD CONNECTIONS
    createConnection(a_scene, 2, 2)


def makeRooms(project):
    a = random.randint(1, 2)
    if(a == 1):
        a_scene = createScene(project)  # creates the scene
        finishConnection(a_scene, 3, 3)
        # Spawns in the weapon
        a_rock_sprite = addSpriteSheet(project, "rock.png", "rock", "static")
        a_rock = makeKey(a_rock_sprite, 5, 6)
        a_scene["actor"].append(a_rock)

        # spawns inthe enemies + combat system (max of 8 enemies)
        spawnEnemy(
            a_scene, a_rock, project.settings["playerSpriteSheetId"], random.randint(1, 8))

        # adds the scene to project
        project["scene"].append(a_scene)

        # Add Connections

        createConnections(a_scene, 2, 2)


def spawnEnemy(scene, weapon, playerID, num):
    enemyList = []
    for i in num:  # spawns in the enemies
        doorway_sprite = addSpriteSheet(
            project, "tower.png", "tower", "static")
        actor_x = random.randint(1, (scene["width"]-3))
        actor_y = random.randint(2, scene["height"]-2)
        a_enemy = makeActor(a_rock_sprite, actor_x, actor_y)
        enemyList.append(a_enemy)

    # creates the combat system
    combat.setUpScene(scene, weapon, playerID, enemyList)


def hallway(project):
    # creates the scene
    scene = createScene(project)
    finishConnection(scene, 3, 3)

    # creates hte weapon
    a_rock_sprite = addSpriteSheet(project, "rock.png", "rock", "static")
    a_rock = makeKey(a_rock_sprite, 5, 6)
    a_scene["actor"].append(a_rock)

    # spawns in the enemies + combat
    spawnEnemy(scene, a_rock, project.settings["playerSpriteSheetId"], 1)

    # adds scene to project
    project["scene"].append(scene)

    # Add connection
    createConnection(scene, 2, 2)


def endBoss(project):
    hallway(project)
    endRoom(project)


def endRoom(project):
    # creates hte scene
    scene = createScene(project)
    finishConnection(scene, 3, 3)

    # creates hte weapon
    a_rock_sprite = addSpriteSheet(project, "rock.png", "rock", "static")
    a_rock = makeKey(a_rock_sprite, 5, 6)
    a_scene["actor"].append(a_rock)

    # spawns in the enemies + combat
    spawnEnemy(scene, a_rock, project.settings["playerSpriteSheetId"], 1)

    # puts scene in project
    project["scene"].append(scene)


def makeGame():
    project = makeBasicProject()

    # Create sprite sheet for the player sprite
    player_sprite_sheet = addSpriteSheet(
        project, "actor_animated.png", "actor_animated", "actor_animated")
    project.settings["playerSpriteSheetId"] = player_sprite_sheet["id"]

    project.music.append(makeMusic("template", "template.mod"))
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
    parser = argparse.ArgumentParser(
        description="Generate a Game Boy ROM via a GB Studio project file.")
    parser.add_argument('--destination', '-d', type=str,
                        help="destination folder name", default="../gbprojects/projects2/")
    args = parser.parse_args()

    initializeGenerator()
    project = makeGame()
    writeProjectToDisk(project, output_path=args.destination)

    if args.destination == "../gbprojects/projects/":
        print(f"{bcolors.WARNING}NOTE: Used default output directory, change with the -d flag{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}See generate.py --help for more options{bcolors.ENDC}")
