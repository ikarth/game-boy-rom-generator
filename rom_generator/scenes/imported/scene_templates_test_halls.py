# Generated Scene Functions
# scene_templates_test_halls.py

from rom_generator import generator

def scene_gen_template_hall_02_00001(callback):
   actor_list = []
   collision_data_list = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 207, 255, 255, 255, 240, 255, 255, 15, 255, 252, 3, 240, 207, 63, 0, 255, 252, 1, 240, 207, 31, 0, 255, 252, 3, 240, 207, 63, 0, 255, 252, 3, 240, 207, 255, 63, 255, 252, 255, 243, 207, 255, 63, 255, 252, 255, 243, 207, 255, 63, 255, 252, 63, 240, 207, 255, 3, 255, 252, 63, 0, 0, 252, 63, 0, 192, 255, 3, 0, 252, 255, 195, 255, 255, 63, 252, 255, 255, 231, 255]
   gen_scene_bkg = generator.makeBackground("halls_02.png")
   gen_scene_scn = generator.makeScene("_gen_template_hall_02", gen_scene_bkg, collisions=collision_data_list)
   gen_scene_connections = []
   scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "tags": []}
   return scene_data


def scene_gen_template_hall_03_00002(callback):
   actor_list = []
   collision_data_list = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 243, 255, 255, 63, 255, 255, 255, 243, 255, 255, 63, 255, 255, 255, 243, 255, 255, 63, 255, 255, 255, 243, 255, 255, 63, 252, 255, 255, 195, 255, 255, 63, 252, 255, 255, 195, 255, 255, 63, 252, 255, 255, 195, 252, 63, 0, 0, 255, 3, 0, 240, 63, 0, 0, 255, 127, 254, 255, 255, 231, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
   gen_scene_bkg = generator.makeBackground("halls_03.png")
   gen_scene_scn = generator.makeScene("_gen_template_hall_03", gen_scene_bkg, collisions=collision_data_list)
   gen_scene_connections = []
   scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "tags": []}
   return scene_data


def scene_gen_template_hall_04_00003(callback):
   actor_list = []
   collision_data_list = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 252, 255, 255, 207, 255, 255, 255, 252, 255, 255, 207, 255, 255, 255, 252, 63, 255, 207, 255, 192, 255, 252, 15, 252, 207, 255, 192, 255, 252, 207, 255, 15, 0, 252, 255, 0, 192, 255, 15, 0, 252, 255, 0, 192, 255, 15, 0, 252, 255, 255, 249, 255, 255, 159, 255, 255, 255, 255, 255]
   gen_scene_bkg = generator.makeBackground("halls_04.png")
   gen_scene_scn = generator.makeScene("_gen_template_hall_04", gen_scene_bkg, collisions=collision_data_list)
   gen_scene_connections = []
   scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "tags": []}
   return scene_data


def catalog():
   """
   Returns a list of scene functions from this part of the library.
   """
   return [scene_gen_template_hall_02_00001,
      scene_gen_template_hall_03_00002,
      scene_gen_template_hall_04_00003]




def createExampleProject():
    """
    Demonstration of how the scene generators in this file can be used.
    """
    project = generator.makeBasicProject()

    # Create sprite sheet for the player sprite
    player_sprite_sheet = generator.addSpriteSheet(project, "actor_animated.png", "actor_animated", "actor_animated")
    project.settings["playerSpriteSheetId"] = player_sprite_sheet["id"]

    scene_data_list = []
    for s in catalog():
        scene_data_list.append(s(None))

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
    destination = "../gbprojects/generated_export_test/"
    generator.initializeGenerator()
    project = createExampleProject()
    generator.writeProjectToDisk(project, output_path = destination)

