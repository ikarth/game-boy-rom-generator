# Generate some basic example scenes

import sys
print(sys.path)
import generator
import scriptFunctions as script

def sceneGenHall_04():
    actor_list = []

    key_script_flag_variable = 25

    key_script_pickup = []
    key_script_hide_on_init = []

    key_location = (6, 11)
    key_sprite = generator.makeSpriteSheet("key_00.png")
    key_actor = generator.makeActor(x=key_location[0], y=key_location[1])

    collision_string = [ 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 207, 255, 255, 255, 240, 255, 255, 15, 255, 252, 3, 240, 207, 63, 0, 255, 252, 1, 240, 207, 31, 0, 255, 252, 3, 240, 207, 63, 0, 255, 252, 3, 240, 207, 255, 63, 255, 252, 255, 243, 207, 255, 63, 255, 252, 255, 243, 207, 255, 63, 255, 252, 63, 240, 207, 255, 3, 255, 252, 63, 0, 0, 252, 63, 0, 192, 255, 3, 0, 252, 255, 195, 255, 255, 63, 252, 255, 255, 231, 255]
    hall_bkg = makeBackground("halls_04.png")
    hall = generator.makeScene("_gen_hall_04", hall_bkg, collisions=collision_string, actors=actor_list)

    scene_data = {"scene": hall, "background": hall_bkg, "sprite": [key_sprite], "connections": [], "tags": []}
    return scene_data


def createExampleProject():
    """
    Demonstration of how the scene generators in this file can be used.
    """
    project = generator.makeBasicProject()

    # Create sprite sheet for the player sprite
    player_sprite_sheet = generator.addSpriteSheet(project, "actor_animated.png", "actor_animated", "actor_animated")
    project.settings["playerSpriteSheetId"] = player_sprite_sheet["id"]

    scenedata_h_04 = sceneGenHall_04()
    project.scenes.append(scenedata_h_04["scene"])
    project.backgrounds.append(scenedata_h_04["background"])
    for s_sheet in scenedata_h_04["sprite"]:
        project.spriteSheets.append(s_sheet)

    # Add some music
    project.music.append(makeMusic("template", "template.mod"))

    # Set the starting scene
    project.settings["startSceneId"] = project.scenes[0]["id"]
    project.settings["startX"] = 8
    project.settings["startY"] = 14

    return project

# test creating scenes...
if __name__ == '__main__':
    destination = "../../gbprojects/scene_gen_halls/"
    initializeGenerator()
    project = createExampleProject()
    writeProjectToDisk(project, output_path = destination)
