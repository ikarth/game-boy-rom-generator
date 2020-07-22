##### Scene Library #####

import scene_gen_halls


def getLibrary():
  scene_library = []
  scene_library + scene_gen_halls.catalog()

def createExampleProject():
    """
    Demonstration of how the scene generators in this file can be used.
    """
    project = generator.makeBasicProject()

    # Create sprite sheet for the player sprite
    player_sprite_sheet = generator.addSpriteSheet(project, "actor_animated.png", "actor_animated", "actor_animated")
    project.settings["playerSpriteSheetId"] = player_sprite_sheet["id"]

    # TODO: Add support for partial functions or callbacks or something that
    # will allow for more interesting initialization options.
    scene_catalog = getLibrary()
    scene_data_list = []
    for s_func in scene_catalog:
        scene_data_list.append(s_func["scene_func"]())
        
    generator.connectScenesRandomlySymmetric(scene_data_list)

    for sdata in scene_data_list:
        generator.addSceneData(project, sdata)

    # Add some music
    project.music.append(generator.makeMusic("template", "template.mod"))

    # Set the starting scene
    project.settings["startSceneId"] = project.scenes[0]["id"]
    project.settings["startX"] = 7
    project.settings["startY"] = 21
    # TODO: implement a way to pick a starting point within a scene that
    # doesn't overlap with any collision tiles or triggers.

    return project

# test creating scenes...
if __name__ == '__main__':
    destination = "../gbprojects/scene_gen_halls/"
    generator.initializeGenerator()
    project = createExampleProject()
    generator.writeProjectToDisk(project, output_path = destination)
