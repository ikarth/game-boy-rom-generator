import random
import copy

from rom_generator import generator
from rom_generator import script_functions as script
from rom_generator.scenes import title
from rom_generator.scenes import scene_library
from rom_generator.scenes.imported import VictoryScreen
from rom_generator.scenes.imported import SaveTheWorld


def createExampleProject(proj_title="generated", macguffin_title="MacGuffin"):
    """
    Demonstration of how the scene generators in this file can be used.
    """
    project = generator.makeBasicProject()
    project.name = proj_title

    # Create sprite sheet for the player sprite
    player_sprite_sheet = generator.addSpriteSheet(project, "actor_animated.png", "actor_animated", "actor_animated")
    project.settings["playerSpriteSheetId"] = player_sprite_sheet["id"]

    scene_data_list = []

    # Add title screen
    catalog, sprites = title.title_scene_generation(proj_title)
    for scn_func in catalog():
        scene_data_list.append(scn_func(None))
    for element_sprite in sprites:
        project.spriteSheets.append(element_sprite)

    # Add victory screen
    win_catalog, win_sprites = VictoryScreen.scene_generation(proj_title, macguffin_title)
    for scn_func in win_catalog():
        scene_data_list.append(scn_func(None))
    for element_sprite in win_sprites:
        project.spriteSheets.append(element_sprite)

    world_catalog, world_sprites = SaveTheWorld.scene_generation(proj_title, macguffin_title)
    for scn_func in world_catalog():
        scene_data_list.append(scn_func(None))
    for element_sprite in world_sprites:
        project.spriteSheets.append(element_sprite)

    scn_library, spr_library = scene_library.getLibrary()
    for scn_func in scn_library:
        scene_data_list.append(scn_func(None))
    for element_sprite in spr_library:
        project.spriteSheets.append(element_sprite)

    # Hack to try to make sure the game is able to be completed...
    current_scene_data_list = copy.deepcopy(scene_data_list)
    for n in range(15):
        print(n)
        generator.connectScenesRandomlySymmetric(scene_data_list)
        steps_to_solve = generator.testConnections(scene_data_list)
        print(steps_to_solve)
        steps_to_key = generator.testConnections(scene_data_list, "_gen_SceneWithKey_real")
        print(steps_to_key)
        if (steps_to_solve < 0) or (steps_to_key < 0):
            print("Solve failed. Trying again...")
            scene_data_list = copy.deepcopy(current_scene_data_list)
            continue
        else:
            print("Scenes connected.")
            current_scene_data_list = copy.deepcopy(scene_data_list)
            break
    scene_data_list = copy.deepcopy(current_scene_data_list)
    print("### ### ###")

    # actually add the scenes to the project
    for sdata in scene_data_list:
        generator.addSceneData(project, generator.translateReferences(sdata, scene_data_list))

    # Add some music
    project.music.append(generator.makeMusic("template", "template.mod"))

    # Set the starting scene
    project.settings["startSceneId"] = project.scenes[0]["id"] # Assumes that the logo is the first scene
    project.settings["startX"] = 0
    project.settings["startY"] = 0

    return project


if __name__ == '__main__':
    import subprocess
    import pathlib
    import os
    root_path = pathlib.Path(__file__).parent.absolute()
    print(root_path)
    number_of_roms_to_generate = 1
    for n in range(number_of_roms_to_generate):
        random.seed(None)
        proj_title, macguffin_title = title.generateTitle()
        print(proj_title)
        print(macguffin_title)
        if macguffin_title == "":
            macguffin_title = "MacGuffin"

        title_munged = proj_title.replace(" ", "").replace(":", "_").replace("'", "_").replace("&", "and").replace("]|[","3").replace("]","I").replace("|","I").replace("[","I")
        destination = f"../gbprojects/generated/{title_munged}"
        generator.initializeGenerator()
        project = createExampleProject(proj_title, macguffin_title)
        generator.writeProjectToDisk(project, filename=f"{title_munged[:28]}.gbsproj", output_path = destination)
        print("Invoking compile for " + os.path.abspath(r'.\compile_rom.bat') + ' ' + os.path.abspath(destination + "/" + f"{title_munged[:28]}.gbsproj"))
        subprocess.call([os.path.abspath(r'.\compile_rom.bat'), os.path.abspath(destination + "/" + f"{title_munged[:28]}.gbsproj")])
