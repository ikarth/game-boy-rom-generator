# Generated Scene Functions
# SaveTheWorld_2.py

from rom_generator import generator
from rom_generator import script_functions as script

test_generation_destination_path = "../gbprojects/generated_export_test_SaveTheWorld_2/"

def scene_generation():
    sprite_sheet_data = [
        generator.makeSpriteSheet('actor.png', name='actor', type='actor', frames=3),
        generator.makeSpriteSheet('actor_animated.png', name='actor_animated', type='actor_animated', frames=6),
        generator.makeSpriteSheet('cat.png', name='cat', type='static', frames=1),
        generator.makeSpriteSheet('closed_sewer_door.png', name='closed_sewer_door', type='static', frames=1),
        generator.makeSpriteSheet('key_00.png', name='key_00', type='static', frames=1),
        generator.makeSpriteSheet('ladder.png', name='ladder', type='static', frames=1),
        generator.makeSpriteSheet('npc001.png', name='npc001', type='actor', frames=3),
        generator.makeSpriteSheet('npc002.png', name='npc002', type='actor', frames=3),
        generator.makeSpriteSheet('sage.png', name='sage', type='static', frames=1),
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
    
    def scene_gen_TheMentor_00001(callback):
        actor_name_table = {}
        actor_00 = generator.makeActor(None, 9, 7, 'static', moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('sage')['id'], name='actor_f55fdfb8-e456-456a-babb-d3bd1d3e0846')
        actor_name_table.update({'actor_f55fdfb8-e456-456a-babb-d3bd1d3e0846': actor_00})
        actor_00['script'] = [
                script.soundPlayEffect(type='tone', pitch=4, frequency=200, duration=0.5),
                script.text(text=['You must find the\nMacGuffin and save\nthe world!'], avatarId=''),
                script.end()
            ]
        actor_list = [actor_00]
        trigger_00 = generator.makeTrigger('trigger_00', 9, 16, 2, 2)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 63, 0, 192, 3, 0, 60, 0, 192, 3, 0, 60, 0, 192, 3, 0, 60, 0, 192, 3, 0, 60, 0, 192, 3, 0, 60, 0, 192, 255, 249, 255, 159, 255]
        gen_scene_bkg = generator.makeBackground("cave.png")

        gen_scene_scn = generator.makeScene("_gen_TheMentor", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_TheMentor_00001")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (9, 15), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (9, 16), 'entrance_size': (2, 2)  } }

        gen_scene_connections = [connection_00]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_SceneWithLock_00002(callback):
        actor_name_table = {}
        actor_00 = generator.makeActor(None, 18, 6, 'static', animate=True, moveSpeed=1, animSpeed=1, direction='down', script=[], sprite_id=findSpriteByName('npc001')['id'], name='actor_3441e071-25bd-4096-93a2-007278e59755')
        actor_name_table.update({'actor_3441e071-25bd-4096-93a2-007278e59755': actor_00})
        actor_00['script'] = [
                script.ifTrue(variable='1', children = {
                    'true': [script.text(text=['Oh, you have the\nkey! Go on in.'], avatarId=''), script.actorMoveTo(actorId='♔REFERENCE_TO_ACTORS_<3441e071-25bd-4096-93a2-007278e59755>♔', x=16, y=8), script.end()],
                    'false': [script.text(text=["You're going to\nneed to give me\nthe key."], avatarId=''), script.end()]
                }),
                script.end()
            ]
        actor_list = [actor_00]
        trigger_00 = generator.makeTrigger('trigger_00', 18, 4, 2, 2)
        trigger_01 = generator.makeTrigger('trigger_01', 0, 8, 1, 8)
        trigger_02 = generator.makeTrigger('trigger_02', 29, 8, 1, 8)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 243, 255, 255, 255, 252, 255, 255, 63, 255, 255, 255, 207, 255, 192, 192, 192, 0, 48, 48, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 192, 204, 204, 204, 48, 51, 51, 51, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 63]
        gen_scene_bkg = generator.makeBackground("corridors_04.png")

        gen_scene_scn = generator.makeScene("_gen_SceneWithLock", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_SceneWithLock_00002")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (18, 7), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (18, 4), 'entrance_size': (2, 2)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (1, 11), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 8), 'entrance_size': (1, 8)  } }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (27, 11), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (29, 8), 'entrance_size': (1, 8)  } }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_SceneWithKey_00003(callback):
        actor_name_table = {}
        actor_00 = generator.makeActor(None, 16, 11, 'static', moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('key_00')['id'], name='actor_121f7aa5-6dc4-47d2-939c-b5bd8204e506')
        actor_name_table.update({'actor_121f7aa5-6dc4-47d2-939c-b5bd8204e506': actor_00})
        actor_00['script'] = [
                script.text(text=['You have the key!'], avatarId=''),
                script.setTrue(variable='1'),
                script.end()
            ]
        actor_list = [actor_00]
        trigger_00 = generator.makeTrigger('trigger_00', 19, 6, 1, 13)
        trigger_01 = generator.makeTrigger('trigger_01', 0, 6, 1, 13)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 128, 31, 0, 248, 1, 128, 31, 0, 248, 1, 128, 31, 0, 248, 1, 128, 31, 0, 248, 1, 128, 31, 0, 248, 1, 128, 31, 0, 248, 1, 128, 31, 240, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
        gen_scene_bkg = generator.makeBackground("corridors_06.png")

        gen_scene_scn = generator.makeScene("_gen_SceneWithKey", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_SceneWithKey_00003")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (17, 17), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 6), 'entrance_size': (1, 13)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (1, 17), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 6), 'entrance_size': (1, 13)  } }

        gen_scene_connections = [connection_00, connection_01]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_SceneWithLock_00004(callback):
        actor_name_table = {}
        actor_00 = generator.makeActor(None, 12, 1, 'static', animate=True, moveSpeed=1, animSpeed=1, direction='down', script=[], sprite_id=findSpriteByName('npc001')['id'], name='actor_d3476f1b-276a-4da7-914d-ea6184aa8f3c')
        actor_name_table.update({'actor_d3476f1b-276a-4da7-914d-ea6184aa8f3c': actor_00})
        actor_00['script'] = [
                script.ifTrue(variable='1', children = {
                    'true': [script.text(text=['Oh, you have the\nkey! Go on in.'], avatarId=''), script.actorMoveTo(actorId='♔REFERENCE_TO_ACTORS_<d3476f1b-276a-4da7-914d-ea6184aa8f3c>♔', x=16, y=8), script.end()],
                    'false': [script.text(text=["You're going to\nneed to give me\nthe key."], avatarId=''), script.end()]
                }),
                script.end()
            ]
        actor_list = [actor_00]
        trigger_00 = generator.makeTrigger('trigger_00', 18, 4, 2, 2)
        trigger_01 = generator.makeTrigger('trigger_01', 0, 1, 1, 8)
        trigger_02 = generator.makeTrigger('trigger_02', 25, 1, 1, 8)
        trigger_list = []
        collision_data_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        gen_scene_bkg = generator.makeBackground("sewer_03.png")

        gen_scene_scn = generator.makeScene("_gen_SceneWithLock", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_SceneWithLock_00004")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (18, 3), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (18, 4), 'entrance_size': (2, 2)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (1, 5), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 1), 'entrance_size': (1, 8)  } }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (23, 5), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (25, 1), 'entrance_size': (1, 8)  } }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_stw_01_00005(callback):
        actor_name_table = {}
        actor_00 = generator.makeActor(None, 9, 6, 'static', animate=False, moveSpeed=1, animSpeed=1, direction='down', script=[], sprite_id=findSpriteByName('closed_sewer_door')['id'], name='actor_ba218b25-1f93-4421-a90f-8947df40d558')
        actor_name_table.update({'actor_ba218b25-1f93-4421-a90f-8947df40d558': actor_00})
        actor_00['script'] = [
                script.ifTrue(variable='1', children = {
                    'true': [script.text(text=['You open the\ndoor.'], avatarId=''), script.actorHide(actorId='♔REFERENCE_TO_ACTORS_<$self$>♔'), script.actorMoveTo(actorId='♔REFERENCE_TO_ACTORS_<$self$>♔', x=0, y=0), script.end()],
                    'false': [script.text(text=['The door is\nlocked. You need a\nkey.'], avatarId=''), script.end()]
                }),
                script.end()
            ]
        actor_list = [actor_00]
        trigger_00 = generator.makeTrigger('trigger_00', 0, 7, 1, 6)
        trigger_01 = generator.makeTrigger('trigger_01', 9, 5, 2, 2)
        trigger_02 = generator.makeTrigger('trigger_02', 19, 7, 1, 6)
        trigger_03 = generator.makeTrigger('trigger_03', 9, 17, 2, 1)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 249, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 240, 159, 255, 255, 249, 255, 159, 255, 255, 249, 255, 159, 255]
        gen_scene_bkg = generator.makeBackground("savetheworld_01.png")

        gen_scene_scn = generator.makeScene("_gen_stw_01", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_stw_01_00005")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (1, 11), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 7), 'entrance_size': (1, 6)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (9, 7), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (9, 5), 'entrance_size': (2, 2)  } }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (17, 11), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 7), 'entrance_size': (1, 6)  } }

        def addConnection_03(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_03 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_03['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_03
        connection_03 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_03, 'args': { 'exit_location': (9, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (9, 17), 'entrance_size': (2, 1)  } }

        gen_scene_connections = [connection_00, connection_01, connection_02, connection_03]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_stw_02_00006(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 0, 8, 1, 3)
        trigger_01 = generator.makeTrigger('trigger_01', 19, 8, 1, 3)
        trigger_02 = generator.makeTrigger('trigger_02', 8, 8, 1, 3)
        trigger_02['script'] = [
                script.ifTrue(variable='23', children = {
                    'true': [script.actorMoveTo(actorId='♔REFERENCE_TO_ACTORS_<player>♔', x=12, y=9), script.end()],
                    'false': [script.text(text=["You can't cross\nwithout a ladder."], avatarId=''), script.end()]
                }),
                script.end()
            ]
        trigger_03 = generator.makeTrigger('trigger_03', 11, 8, 1, 3)
        trigger_03['script'] = [
                script.ifTrue(variable='23', children = {
                    'true': [script.actorMoveTo(actorId='♔REFERENCE_TO_ACTORS_<player>♔', x=6, y=9), script.end()],
                    'false': [script.text(text=["You can't cross\nwithout a ladder."], avatarId=''), script.end()]
                }),
                script.end()
            ]
        trigger_list = [trigger_02, trigger_03]
        collision_data_list = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 0, 6, 0, 96, 0, 0, 6, 240, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
        gen_scene_bkg = generator.makeBackground("save_the_world_02.png")

        gen_scene_scn = generator.makeScene("_gen_stw_02", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_stw_02_00006")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (1, 9), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 8), 'entrance_size': (1, 3)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (17, 9), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 8), 'entrance_size': (1, 3)  } }

        gen_scene_connections = [connection_00, connection_01]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_stw_03_upper_00007(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 0, 4, 1, 2)
        trigger_01 = generator.makeTrigger('trigger_01', 19, 4, 1, 2)
        trigger_02 = generator.makeTrigger('trigger_02', 8, 0, 4, 4)
        trigger_list = []
        collision_data_list = [255, 240, 255, 15, 255, 255, 240, 255, 15, 255, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 48, 252, 255, 195, 255, 63, 252, 255, 195, 255, 63, 252, 255, 195, 255, 63, 252, 255]
        gen_scene_bkg = generator.makeBackground("save_the_world_03.png")

        gen_scene_scn = generator.makeScene("_gen_stw_03_upper", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_stw_03_upper_00007")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (1, 5), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 4), 'entrance_size': (1, 2)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (17, 5), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 4), 'entrance_size': (1, 2)  } }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.ifTrue(variable='1', children = {
                            'true': [script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'), script.end()],
                            'false': [script.text(text=['The door is\nlocked.'], avatarId=''), script.end()]
                        }),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (9, 4), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (8, 0), 'entrance_size': (4, 4)  } }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Scene_8_00008(callback):
        actor_name_table = {}
        actor_00 = generator.makeActor(None, 5, 7, 'static', moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('cat')['id'], name='actor_d3787eee-51ee-455a-a446-280e29e9c80d')
        actor_name_table.update({'actor_d3787eee-51ee-455a-a446-280e29e9c80d': actor_00})
        actor_00['script'] = [
                script.text(text=['Meow!'], avatarId=''),
                script.end()
            ]
        actor_01 = generator.makeActor(None, 0, 4, 'static', moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('ladder')['id'], name='actor_74ec84d0-260b-4c64-9921-8167b98d31bc')
        actor_name_table.update({'actor_74ec84d0-260b-4c64-9921-8167b98d31bc': actor_01})
        actor_01['script'] = [
                script.text(text=['You have the\nladder!'], avatarId=''),
                script.setTrue(variable='23'),
                script.end()
            ]
        actor_list = [actor_00, actor_01]
        trigger_00 = generator.makeTrigger('trigger_00', 19, 12, 1, 5)
        trigger_01 = generator.makeTrigger('trigger_01', 19, 6, 1, 2)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 240, 255, 15, 255, 255, 112, 0, 0, 7, 0, 240, 0, 15, 15, 240, 240, 195, 15, 63, 252, 0, 195, 0, 48, 12, 0, 0, 0, 0, 0, 0, 0, 240, 255, 255]
        gen_scene_bkg = generator.makeBackground("save_the_world_04.png")

        gen_scene_scn = generator.makeScene("_gen_Scene_8", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Scene_8_00008")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (17, 15), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 12), 'entrance_size': (1, 5)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (17, 7), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 6), 'entrance_size': (1, 2)  } }

        gen_scene_connections = [connection_00, connection_01]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_stw_03_lower_00009(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 2, 17, 4, 1)
        trigger_01 = generator.makeTrigger('trigger_01', 0, 8, 1, 3)
        trigger_02 = generator.makeTrigger('trigger_02', 19, 8, 1, 3)
        trigger_list = []
        collision_data_list = [255, 240, 255, 15, 255, 255, 240, 255, 15, 255, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 48, 252, 255, 195, 255, 63, 252, 255, 195, 255, 63, 252, 255, 195, 255, 63, 252, 255]
        gen_scene_bkg = generator.makeBackground("save_the_world_03.png")

        gen_scene_scn = generator.makeScene("_gen_stw_03_lower", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_stw_03_lower_00009")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (3, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (2, 17), 'entrance_size': (4, 1)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (1, 9), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 8), 'entrance_size': (1, 3)  } }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (17, 9), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 8), 'entrance_size': (1, 3)  } }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def catalog():
        """
        Returns a list of scene functions from this part of the library.
        """
        return [scene_gen_TheMentor_00001,
            scene_gen_SceneWithLock_00002,
            scene_gen_SceneWithKey_00003,
            scene_gen_SceneWithLock_00004,
            scene_gen_stw_01_00005,
            scene_gen_stw_02_00006,
            scene_gen_stw_03_upper_00007,
            scene_gen_Scene_8_00008,
            scene_gen_stw_03_lower_00009]

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

