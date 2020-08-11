# Generate some basic example scenes

from rom_generator import generator
from rom_generator import script_functions as script
from rom_generator import spriteSheetManager as manager
import random

index = 0

def setUpGenHallScenes():
    backgroundNames = []
    backgroundNames.append(createGenHall_04Grammar())
    backgroundNames.append(createGenHall_03Grammar())

    return backgroundNames

def createGenHall_03Grammar():
    hall_bkg = generator.makeBackground("halls_03.png")

    sceneName = "halls_03"
    manager.addBackgroundSpriteSheet("halls_03", hall_bkg)


    manager.addOutConnections(sceneName, [[11, 24],[20, 19],[14, 7]])
    manager.addInConnections(sceneName, [[11, 23], [20, 20], [14, 8]])

    connections = [{"out": (11, 24, 2, 1), "in": (11, 23)},
                   {"out": (20, 19, 2, 1), "in": (20, 20)},
                   {"out": (14,  7, 2, 1), "in": (14,  8)}]
    return "halls_03"

def createGenHall_04Grammar():
    hall_bkg = generator.makeBackground("halls_04.png")
    sceneName = "halls_04"
    manager.addBackgroundSpriteSheet("halls_04", hall_bkg)


    manager.addOutConnections(sceneName, [[18, 15],[2,1],[13,26],[4,11]])
    manager.addInConnections(sceneName, [[18, 16], [13, 25], [4, 12]])
    return "halls_04"

def sceneGenHallGrammar():
    index = random.randint(0, 1)
    if(index == 0):
        return sceneGenHall_03Grammar()
    return sceneGenHall_04Grammar()

def sceneGenHall_03Grammar():
    actor_list = []

    collision_string_03 = [ 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 243, 255, 255, 63, 255, 255, 255, 243, 255, 255, 63, 255, 255, 255, 243, 255, 255, 63, 255, 255, 255, 243, 255, 255, 63, 252, 255, 255, 195, 255, 255, 63, 252, 255, 255, 195, 255, 255, 63, 252, 255, 255, 195, 252, 63, 0, 0, 255, 3, 0, 240, 63, 0, 0, 255, 127, 254, 255, 255, 231, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255 ]
    hall_bkg = manager.findBackgroundSpriteSheet("halls_03")
    hall = generator.makeScene("_gen_hall_03", hall_bkg, collisions=collision_string_03, actors=actor_list)

    # 3
    connections = [{"out": (11, 24, 2, 1), "in": (11, 23)},
                   {"out": (20, 19, 2, 1), "in": (20, 20)},
                   {"out": (14,  7, 2, 1), "in": (14,  8)}]

    return ["halls_03", hall]

def sceneGenHall_04Grammar():
    '''This is sceneGenHall_04 room converted to fit with the grammar generator of roomGen2'''
    global index
    actor_list = []
    sceneName = "hall_04"
    collision_string_04 = [ 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 252, 255, 255, 207, 255, 255, 255, 252, 255, 255, 207, 255, 255, 255, 252, 63, 255, 207, 255, 192, 255, 252, 15, 252, 207, 255, 192, 255, 252, 207, 255, 15, 0, 252, 255, 0, 192, 255, 15, 0, 252, 255, 0, 192, 255, 15, 0, 252, 255, 255, 249, 255, 255, 159, 255, 255, 255, 255, 255 ]
    hall_bkg = manager.findBackgroundSpriteSheet("halls_04")

    hall = generator.makeScene(sceneName, hall_bkg, collisions=collision_string_04, actors=actor_list)

    return ["halls_04", hall]


def sceneGenHall_04():
    actor_list = []

    collision_string_04 = [ 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 252, 255, 255, 207, 255, 255, 255, 252, 255, 255, 207, 255, 255, 255, 252, 63, 255, 207, 255, 192, 255, 252, 15, 252, 207, 255, 192, 255, 252, 207, 255, 15, 0, 252, 255, 0, 192, 255, 15, 0, 252, 255, 0, 192, 255, 15, 0, 252, 255, 255, 249, 255, 255, 159, 255, 255, 255, 255, 255 ]
    hall_bkg = generator.makeBackground("halls_04.png")
    hall = generator.makeScene("_gen_hall_04", hall_bkg, collisions=collision_string_04, actors=actor_list)

    # 4
    connections = [{"out": (18, 15, 2, 1), "in": (18, 16)},
                   {"out": (13, 26, 2, 1), "in": (13, 25)},
                   {"out": ( 4, 11, 2, 1), "in": ( 4, 12)}]

    scene_data = {"scene": hall, "background": hall_bkg, "sprites": [], "connections": connections, "tags": []}
    return scene_data

def sceneGenHall_03():
    actor_list = []

    collision_string_03 = [ 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 243, 255, 255, 63, 255, 255, 255, 243, 255, 255, 63, 255, 255, 255, 243, 255, 255, 63, 255, 255, 255, 243, 255, 255, 63, 252, 255, 255, 195, 255, 255, 63, 252, 255, 255, 195, 255, 255, 63, 252, 255, 255, 195, 252, 63, 0, 0, 255, 3, 0, 240, 63, 0, 0, 255, 127, 254, 255, 255, 231, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255 ]
    hall_bkg = generator.makeBackground("halls_03.png")
    hall = generator.makeScene("_gen_hall_03", hall_bkg, collisions=collision_string_03, actors=actor_list)

    # 3
    connections = [{"out": (11, 24, 2, 1), "in": (11, 23)},
                   {"out": (20, 19, 2, 1), "in": (20, 20)},
                   {"out": (14,  7, 2, 1), "in": (14,  8)}]

    scene_data = {"scene": hall, "background": hall_bkg, "sprites": [], "connections": connections, "tags": []}
    return scene_data

def sceneGenHall_02():
    actor_list = []

    key_location = (6, 11)
    key_sprite = generator.makeSpriteSheet("key_00.png")
    key_actor = generator.makeActor(key_sprite, x=key_location[0], y=key_location[1])

    key_script_flag_variable = str(25) # TODO: make this dynamic
    # TODO: also add information about the key to an inventory system

    self_id = key_actor["id"]
    key_script_pickup = [script.actorHide(actorId="$self$"),
                        script.setTrue(key_script_flag_variable),
                        script.text("You picked up the key."),
                        script.end()]
    key_script_hide_on_init = [script.ifTrue(key_script_flag_variable, trueCommands=[script.actorHide(actorId="$self$"), script.end()], falseCommands=[script.end()]), script.end()]

    key_actor["script"] = key_script_pickup
    key_actor["startScript"] = key_script_hide_on_init
    actor_list.append(key_actor)

    collision_string_02 = [ 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 207, 255, 255, 255, 240, 255, 255, 15, 255, 252, 3, 240, 207, 63, 0, 255, 252, 1, 240, 207, 31, 0, 255, 252, 3, 240, 207, 63, 0, 255, 252, 3, 240, 207, 255, 63, 255, 252, 255, 243, 207, 255, 63, 255, 252, 255, 243, 207, 255, 63, 255, 252, 63, 240, 207, 255, 3, 255, 252, 63, 0, 0, 252, 63, 0, 192, 255, 3, 0, 252, 255, 195, 255, 255, 63, 252, 255, 255, 231, 255 ]
    hall_bkg = generator.makeBackground("halls_02.png")
    hall = generator.makeScene("_gen_hall_02", hall_bkg, collisions=collision_string_02, actors=actor_list)

    connections = [{"out": (15, 27, 2, 1), "in": (15, 26)},
                   {"out": ( 8,  5, 2, 1), "in": ( 8,  6)},
                   {"out": (20,  7, 2, 1), "in": (20,  8)},
                   {"out": ( 1, 10, 1, 2), "in": ( 2, 11)}]

    scene_data = {"scene": hall, "background": hall_bkg, "sprites": [key_sprite], "connections": connections, "tags": []}
    return scene_data


def catalog():
    """
    Returns a list of scene functions from this part of the library.
    """
    scene_library = []
    scene_library.append({"scene_func": sceneGenHall_02})
    scene_library.append({"scene_func": sceneGenHall_03})
    scene_library.append({"scene_func": sceneGenHall_04})
    return scene_library

def createExampleProject():
    """
    Demonstration of how the scene generators in this file can be used.
    """
    project = generator.makeBasicProject()

    # Create sprite sheet for the player sprite
    player_sprite_sheet = generator.addSpriteSheet(project, "actor_animated.png", "actor_animated", "actor_animated")
    project.settings["playerSpriteSheetId"] = player_sprite_sheet["id"]

    scene_data_list = []
    scene_data_list.append(sceneGenHall_02())
    scene_data_list.append(sceneGenHall_03())
    scene_data_list.append(sceneGenHall_04())

    generator.connectScenesRandomlySymmetric(scene_data_list)

    for sdata in scene_data_list:
        generator.addSceneData(project, sdata)

    # Add some music
    project.music.append(generator.makeMusic("template", "template.mod"))

    # Set the starting scene
    project.settings["startSceneId"] = project.scenes[0]["id"]
    project.settings["startX"] = 7
    project.settings["startY"] = 21

    return project

# test creating scenes...
if __name__ == '__main__':
    destination = "../gbprojects/scene_gen_halls/"
    generator.initializeGenerator()
    project = createExampleProject()
    generator.writeProjectToDisk(project, output_path = destination)
