import rom_generator.generator as gen

sceneNum = 1
def start(project):
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
    sceneNum+=1

    project["scene"].append(a_scene)
    #ADD CONNECTIONS

def makeRooms(project):
    pass

def spawnEnemy(project, scene, weapon, playerID, num):
    pass

def hallway(project, scene, weapon, playerID):
    pass

def endBoss(project):
    pass

def endRoom(project):

def makeGame():
    project = makeBasicProject()

    # Create sprite sheet for the player sprite
    player_sprite_sheet = addSpriteSheet(
        project, "actor_animated.png", "actor_animated", "actor_animated")
    project.settings["playerSpriteSheetId"] = player_sprite_sheet["id"]

    project.music.append(makeMusic("template", "template.mod"))
    project.settings["startSceneId"] = project.scenes[0]["id"]
    return project

    