# Generated Scene Functions
# VictoryScreen.py

from rom_generator import generator
from rom_generator import script_functions as script

test_generation_destination_path = "../gbprojects/generated_export_test_VictoryScreen/"


def scene_generation(project_title="Quest for the MacGuffin", macguffin_name="MacGuffin"):

    macguffin_sprite = 'macguffin.png'

    sprite_sheet_data = [
        generator.makeSpriteSheet('actor.png', name='actor', type='actor', frames=3),
        generator.makeSpriteSheet('actor_animated.png', name='actor_animated', type='actor_animated', frames=6),
        generator.makeSpriteSheet(macguffin_sprite, name=macguffin_sprite, type='static', frames=1),
        generator.makeSpriteSheet('static.png', name='static', type='static', frames=1)]

    def findSpriteByName(sprite_name):
        '''
        Returns first sprite that matches the name given.
        '''
        try:
            return [s for s in sprite_sheet_data if (s['name'] == sprite_name)][0]
        except:
            return None

    def getBySceneLabel(scene_label):
        '''
        This is mostly here so we can get the matching scene from the original
        template data. As used here it just grabs the first scene that was made
        from that template, so if the template is used more than once it won't
        behave as expected and you should generate a proper relationship instad.
        '''
        s_id = generator.getSceneIdByLabel(scene_label)
        if s_id == None:
            return '<♔' + scene_label + '♔>'
        return s_id

    def scene_gen_MacGuiffinTemple_00001(callback):
        actor_name_table = {}
        actor_00 = generator.makeActor(None, 9, 8, 'static', moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName(macguffin_sprite)['id'], name='actor_92c78695-9b3e-45cf-8410-f991f2dc2fd6')
        actor_name_table.update({'actor_92c78695-9b3e-45cf-8410-f991f2dc2fd6': actor_00})
        actor_list = [actor_00]
        trigger_00 = generator.makeTrigger('trigger_00', 0, 30, 20, 2)
        trigger_01 = generator.makeTrigger('trigger_01', 7, 9, 6, 4)
        trigger_01['script'] = [
          script.switchScene(sceneId="♔REFERENCE_TO_SCENES_<YouWin>♔", x=0, y=0)
        ]
        trigger_list = [trigger_01]
        collision_data_list = [254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 191, 97, 216, 27, 134, 189, 1, 216, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 195, 0, 48, 12, 0, 195, 0, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        gen_scene_bkg = generator.makeBackground("victory.png")

        gen_scene_scn = generator.makeScene("_gen_MacGuiffinTemple", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_MacGuiffinTemple_00001")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_001 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_001['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_001
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (9, 28), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 30), 'entrance_size': (20, 2)  }, 'tags': ['B'] }

        gen_scene_connections = [connection_00]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_YouWin_00002(callback):
        actor_name_table = {}
        actor_list = []
        trigger_list = []
        collision_data_list = []
        gen_scene_bkg = generator.makeBackground("youwin.png")
        scene_script = [
        script.setFalse(variable='26'),
        script.actorHide(actorId='♔REFERENCE_TO_ACTORS_<player>♔'), script.fadeIn(speed='3'), script.text(text=[f'You found the\n{macguffin_name} and\nsaved the world!'], avatarId='0f94da55-8256-470a-9f22-0f54bbf75082'), script.switchScene(sceneId='♔REFERENCE_TO_SCENES_<Title Screen>♔', x=0, y=0, direction='', fadeSpeed='2'), script.end()
        ]

        gen_scene_scn = generator.makeScene("_gen_YouWin", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_YouWin")
        gen_scene_scn['script'] = scene_script
        gen_scene_connections = []
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def catalog():
        """
        Returns a list of scene functions from this part of the library.
        """
        return [scene_gen_MacGuiffinTemple_00001,
            scene_gen_YouWin_00002]

    return catalog, sprite_sheet_data



def createExampleProject():
    """
    Demonstration of how the scene generators in this file can be used.
    """
    project = generator.makeBasicProject()

    # Create sprite sheet for the player sprite
    player_sprite_sheet = generator.addSpriteSheet(project, "actor_animated.png", "actor_animated", "actor_animated")
    project.settings["playerSpriteSheetId"] = player_sprite_sheet["id"]

    scene_data_list = []
    catalog, sprites = scene_generation()
    for scn_func in catalog():
        scene_data_list.append(scn_func(None))
    for element_sprite in sprites:
        project.spriteSheets.append(element_sprite)

    generator.connectScenesRandomlySymmetric(scene_data_list)

    for sdata in scene_data_list:
        generator.addSceneData(project, generator.translateReferences(sdata, scene_data_list))

    # Add some music
    project.music.append(generator.makeMusic("template", "template.mod"))

    # Set the starting scene
    project.settings["startSceneId"] = project.scenes[0]["id"]
    project.settings["startX"] = 7
    project.settings["startY"] = 21

    return project

def runTest(test_dir):
    generator.initializeGenerator()
    project = createExampleProject()
    generator.writeProjectToDisk(project, output_path = test_dir)

# test creating scenes...
if __name__ == '__main__':
    destination = test_generation_destination_path
    runTest(destination)
