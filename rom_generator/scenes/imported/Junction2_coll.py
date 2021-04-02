# Generated Scene Functions
# Junction2_coll.py

from rom_generator import generator
from rom_generator import script_functions as script

test_generation_destination_path = "../gbprojects/generated_export_test_Junction2_coll/"

def scene_generation():
    sprite_sheet_data = [
        generator.makeSpriteSheet('actor.png', name='actor', type='actor', frames=3),
        generator.makeSpriteSheet('actor_animated.png', name='actor_animated', type='actor_animated', frames=6),
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
    
    def scene_gen_Junction5A_00001(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 0, 5, 1, 2)
        trigger_01 = generator.makeTrigger('trigger_01', 0, 13, 1, 1)
        trigger_02 = generator.makeTrigger('trigger_02', 19, 9, 1, 3)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 15, 0, 240, 0, 0, 255, 0, 240, 15, 0, 255, 0, 0, 15, 0, 240, 0, 0, 15, 255, 15, 240, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
        gen_scene_bkg = generator.makeBackground("link_05a.png")

        gen_scene_scn = generator.makeScene("_gen_Junction5A", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Junction5A_00001")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (1, 6), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 5), 'entrance_size': (1, 2)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (1, 13), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 13), 'entrance_size': (1, 1)  } }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (17, 10), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 9), 'entrance_size': (1, 3)  } }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Junction5B_00002(callback):
        actor_name_table = {}
        actor_list = []
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 255, 255, 15, 0, 252, 0, 0, 15, 0, 240, 255, 3, 254, 255, 0, 255, 15, 240, 255, 0, 255, 3, 252, 15, 192, 0, 0, 12, 0, 192, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
        gen_scene_bkg = generator.makeBackground("link_05b.png")

        gen_scene_scn = generator.makeScene("_gen_Junction5B", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Junction5B_00002")

        gen_scene_connections = []
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Junction5C_00003(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 0, 6, 1, 5)
        trigger_01 = generator.makeTrigger('trigger_01', 19, 6, 1, 5)
        trigger_02 = generator.makeTrigger('trigger_02', 6, 0, 4, 1)
        trigger_03 = generator.makeTrigger('trigger_03', 8, 17, 6, 1)
        trigger_list = []
        collision_data_list = [63, 252, 255, 195, 255, 63, 252, 255, 195, 255, 63, 252, 255, 195, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 240, 15, 248, 255, 192, 255, 15, 252, 255, 192, 255, 15, 252, 255, 192, 255, 15, 252]
        gen_scene_bkg = generator.makeBackground("link_05c.png")

        gen_scene_scn = generator.makeScene("_gen_Junction5C", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Junction5C_00003")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (1, 9), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 6), 'entrance_size': (1, 5)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (17, 9), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 6), 'entrance_size': (1, 5)  } }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (7, 1), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (6, 0), 'entrance_size': (4, 1)  } }

        def addConnection_03(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_03 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_03['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_03
        connection_03 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_03, 'args': { 'exit_location': (10, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (8, 17), 'entrance_size': (6, 1)  } }

        gen_scene_connections = [connection_00, connection_01, connection_02, connection_03]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Junction5D_00004(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 13, 0, 4, 1)
        trigger_01 = generator.makeTrigger('trigger_01', 0, 5, 1, 4)
        trigger_02 = generator.makeTrigger('trigger_02', 0, 13, 1, 2)
        trigger_list = []
        collision_data_list = [255, 31, 254, 255, 225, 255, 31, 254, 255, 225, 255, 31, 14, 0, 224, 0, 0, 14, 0, 224, 0, 0, 254, 159, 255, 255, 249, 255, 159, 255, 255, 249, 15, 128, 255, 0, 248, 255, 199, 255, 255, 255, 255, 255, 255]
        gen_scene_bkg = generator.makeBackground("link_05d.png")

        gen_scene_scn = generator.makeScene("_gen_Junction5D", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Junction5D_00004")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (14, 1), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (13, 0), 'entrance_size': (4, 1)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (1, 6), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 5), 'entrance_size': (1, 4)  } }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (1, 14), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 13), 'entrance_size': (1, 2)  } }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Junction5E_00005(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 3, 6, 2, 1)
        trigger_01 = generator.makeTrigger('trigger_01', 7, 6, 2, 1)
        trigger_02 = generator.makeTrigger('trigger_02', 11, 6, 2, 1)
        trigger_03 = generator.makeTrigger('trigger_03', 15, 6, 2, 1)
        trigger_04 = generator.makeTrigger('trigger_04', 0, 7, 1, 6)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 103, 102, 14, 0, 128, 0, 0, 8, 0, 128, 0, 0, 14, 0, 248, 192, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
        gen_scene_bkg = generator.makeBackground("link_05e.png")

        gen_scene_scn = generator.makeScene("_gen_Junction5E", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Junction5E_00005")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (3, 7), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (3, 6), 'entrance_size': (2, 1)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (7, 7), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (7, 6), 'entrance_size': (2, 1)  } }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (11, 7), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (11, 6), 'entrance_size': (2, 1)  } }

        def addConnection_03(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_03 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_03['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_03
        connection_03 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_03, 'args': { 'exit_location': (15, 7), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (15, 6), 'entrance_size': (2, 1)  } }

        def addConnection_04(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_04 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_04['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_04
        connection_04 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_04, 'args': { 'exit_location': (1, 10), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 7), 'entrance_size': (1, 6)  } }

        gen_scene_connections = [connection_00, connection_01, connection_02, connection_03, connection_04]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_ForestA_00006(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 0, 6, 1, 2)
        trigger_01 = generator.makeTrigger('trigger_01', 19, 8, 1, 2)
        trigger_02 = generator.makeTrigger('trigger_02', 3, 2, 2, 2)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 231, 255, 127, 254, 255, 195, 255, 63, 252, 255, 224, 127, 14, 252, 231, 195, 15, 48, 248, 0, 31, 135, 255, 49, 248, 63, 224, 255, 3, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
        gen_scene_bkg = generator.makeBackground("Forest_01a.png")

        gen_scene_scn = generator.makeScene("_gen_ForestA", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_ForestA_00006")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (1, 7), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 6), 'entrance_size': (1, 2)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (17, 9), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 8), 'entrance_size': (1, 2)  } }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (3, 4), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (3, 2), 'entrance_size': (2, 2)  } }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_ForestB_00007(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 8, 0, 2, 1)
        trigger_01 = generator.makeTrigger('trigger_01', 8, 17, 2, 1)
        trigger_02 = generator.makeTrigger('trigger_02', 19, 6, 1, 2)
        trigger_list = []
        collision_data_list = [129, 252, 15, 204, 255, 64, 248, 15, 132, 255, 192, 240, 15, 8, 255, 128, 1, 0, 16, 0, 0, 3, 15, 60, 240, 64, 224, 15, 4, 254, 192, 240, 15, 12, 255, 64, 248, 15, 132, 255, 192, 252, 15, 200, 255]
        gen_scene_bkg = generator.makeBackground("Forest_01b.png")

        gen_scene_scn = generator.makeScene("_gen_ForestB", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_ForestB_00007")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (8, 1), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (8, 0), 'entrance_size': (2, 1)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (8, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (8, 17), 'entrance_size': (2, 1)  } }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (17, 7), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 6), 'entrance_size': (1, 2)  } }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_ForestC_00008(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 19, 8, 1, 2)
        trigger_01 = generator.makeTrigger('trigger_01', 8, 17, 4, 1)
        trigger_list = []
        collision_data_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 0, 248, 15, 224, 255, 0, 15, 0, 120, 0, 192, 135, 15, 62, 248, 224, 240, 15, 7, 255, 112, 248, 15, 135, 255, 240, 240, 15, 15, 255]
        gen_scene_bkg = generator.makeBackground("Forest_01c.png")

        gen_scene_scn = generator.makeScene("_gen_ForestC", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_ForestC_00008")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (17, 9), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 8), 'entrance_size': (1, 2)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (9, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (8, 17), 'entrance_size': (4, 1)  } }

        gen_scene_connections = [connection_00, connection_01]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_ForestC_00009(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 8, 0, 2, 1)
        trigger_01 = generator.makeTrigger('trigger_01', 0, 10, 1, 2)
        trigger_list = []
        collision_data_list = [255, 252, 255, 143, 128, 255, 8, 248, 143, 129, 255, 48, 248, 7, 131, 127, 56, 248, 131, 192, 15, 14, 124, 32, 192, 128, 3, 8, 56, 128, 255, 3, 8, 0, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        gen_scene_bkg = generator.makeBackground("Forest_01d.png")

        gen_scene_scn = generator.makeScene("_gen_ForestC", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_ForestC_00009")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (9, 2), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (8, 0), 'entrance_size': (2, 1)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (1, 11), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 10), 'entrance_size': (1, 2)  } }

        gen_scene_connections = [connection_00, connection_01]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_ForestC_00010(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 9, 6, 2, 2)
        trigger_01 = generator.makeTrigger('trigger_01', 7, 17, 8, 1)
        trigger_list = []
        collision_data_list = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 248, 63, 0, 255, 31, 176, 217, 131, 155, 125, 24, 128, 135, 1, 120, 14, 0, 247, 0, 112, 31, 0, 246, 1, 96, 63, 0, 247, 3, 112, 127, 128, 247, 7, 120]
        gen_scene_bkg = generator.makeBackground("Forest_01e.png")

        gen_scene_scn = generator.makeScene("_gen_ForestC", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_ForestC_00010")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (9, 8), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (9, 6), 'entrance_size': (2, 2)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (10, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (7, 17), 'entrance_size': (8, 1)  } }

        gen_scene_connections = [connection_00, connection_01]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_ForestJunction_00011(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 9, 16, 2, 2)
        trigger_01 = generator.makeTrigger('trigger_01', 9, 0, 2, 1)
        trigger_02 = generator.makeTrigger('trigger_02', 19, 6, 1, 4)
        trigger_list = []
        collision_data_list = [255, 249, 255, 159, 255, 255, 249, 255, 159, 255, 255, 249, 255, 159, 255, 255, 1, 240, 31, 0, 255, 1, 240, 31, 0, 255, 249, 255, 159, 255, 255, 249, 255, 159, 255, 255, 249, 255, 159, 255, 255, 249, 255, 159, 255]
        gen_scene_bkg = generator.makeBackground("link_05f.png")

        gen_scene_scn = generator.makeScene("_gen_ForestJunction", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_ForestJunction_00011")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (9, 15), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (9, 16), 'entrance_size': (2, 2)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (9, 1), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (9, 0), 'entrance_size': (2, 1)  } }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (17, 8), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 6), 'entrance_size': (1, 4)  } }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def catalog():
        """
        Returns a list of scene functions from this part of the library.
        """
        return [scene_gen_Junction5A_00001,
            scene_gen_Junction5B_00002,
            scene_gen_Junction5C_00003,
            scene_gen_Junction5D_00004,
            scene_gen_Junction5E_00005,
            scene_gen_ForestA_00006,
            scene_gen_ForestB_00007,
            scene_gen_ForestC_00008,
            scene_gen_ForestC_00009,
            scene_gen_ForestC_00010,
            scene_gen_ForestJunction_00011]

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

