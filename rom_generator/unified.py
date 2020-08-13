import random

from rom_generator import generator
from rom_generator import script_functions as script
from rom_generator.scenes import title
from rom_generator.scenes import scene_library


def createExampleProject(proj_title="generated"):
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

    scn_library, spr_library = scene_library.getLibrary()
    for scn_func in scn_library:
        scene_data_list.append(scn_func(None))
    for element_sprite in spr_library:
        project.spriteSheets.append(element_sprite)


    generator.connectScenesRandomlySymmetric(scene_data_list)

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
    for n in range(4):
        random.seed(None)
        proj_title = title.generateTitle()
        title_munged = proj_title.replace(" ", "").replace(":", "_").replace("'", "_").replace("&", "and")
        destination = f"../gbprojects/generated/{title_munged}"
        generator.initializeGenerator()
        project = createExampleProject(proj_title)
        generator.writeProjectToDisk(project, filename=f"{title_munged[:28]}.gbsproj", output_path = destination)
