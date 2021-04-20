# Generated Scene Functions
# Forest_collsions.py

from rom_generator import generator
from rom_generator import script_functions as script

test_generation_destination_path = "../gbprojects/generated_export_test_Forest_collsions/"

def scene_generation():
    sprite_sheet_data = [
        generator.makeSpriteSheet('actor.png', name='actor', type='actor', frames=3),
        generator.makeSpriteSheet('actor_animated.png', name='actor_animated', type='actor_animated', frames=6),
        generator.makeSpriteSheet('hatch.png', name='hatch', type='static', frames=1),
        generator.makeSpriteSheet('invisible.png', name='invisible', type='static', frames=1),
        generator.makeSpriteSheet('shovel.png', name='shovel', type='static', frames=1),
        generator.makeSpriteSheet('stairsdown.png', name='stairsdown', type='static', frames=1),
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
    
    def scene_gen_Forest1_00001(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 0, 12, 1, 2)
        trigger_01 = generator.makeTrigger('trigger_01', 9, 7, 2, 1)
        trigger_02 = generator.makeTrigger('trigger_02', 16, 17, 2, 1)
        trigger_list = []
        collision_data_list = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 124, 0, 192, 7, 0, 70, 30, 96, 156, 7, 2, 192, 48, 0, 124, 225, 1, 22, 26, 96, 48, 255, 4, 1, 204, 31, 64, 24, 0, 132, 0, 192, 12, 0, 200]
        gen_scene_bkg = generator.makeBackground("Forest_01_2a.png")

        gen_scene_scn = generator.makeScene("_gen_Forest1", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Forest1_00001")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (1, 12), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 12), 'entrance_size': (1, 2)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (9, 8), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (9, 7), 'entrance_size': (2, 1)  } }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (16, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (16, 17), 'entrance_size': (2, 1)  } }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Forest2_00002(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 6, 17, 2, 1)
        trigger_01 = generator.makeTrigger('trigger_01', 6, 0, 2, 1)
        trigger_02 = generator.makeTrigger('trigger_02', 19, 6, 1, 4)
        trigger_list = []
        collision_data_list = [32, 1, 0, 34, 0, 96, 2, 0, 34, 0, 32, 3, 0, 226, 254, 96, 248, 1, 132, 31, 192, 3, 0, 16, 0, 0, 249, 15, 136, 0, 128, 12, 0, 68, 0, 64, 6, 0, 34, 0, 32, 3, 0, 18, 0]
        gen_scene_bkg = generator.makeBackground("Forest_01_2b.png")

        gen_scene_scn = generator.makeScene("_gen_Forest2", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Forest2_00002")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (6, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (6, 17), 'entrance_size': (2, 1)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (7, 2), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (6, 0), 'entrance_size': (2, 1)  } }

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


    def scene_gen_Forest3_00003(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 0, 14, 1, 2)
        trigger_01 = generator.makeTrigger('trigger_01', 19, 10, 1, 4)
        trigger_02 = generator.makeTrigger('trigger_02', 9, 6, 2, 2)
        trigger_list = []
        collision_data_list = [193, 0, 0, 252, 3, 64, 32, 0, 6, 4, 32, 207, 128, 243, 28, 16, 137, 0, 145, 24, 48, 0, 3, 2, 240, 96, 126, 224, 67, 4, 2, 199, 48, 96, 8, 128, 135, 15, 112, 128, 255, 7, 248, 255, 255]
        gen_scene_bkg = generator.makeBackground("Forest_01_2c.png")

        gen_scene_scn = generator.makeScene("_gen_Forest3", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Forest3_00003")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (1, 14), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 14), 'entrance_size': (1, 2)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (17, 11), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 10), 'entrance_size': (1, 4)  } }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (9, 8), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (9, 6), 'entrance_size': (2, 2)  } }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Forest4_00004(callback):
        actor_name_table = {}
        actor_00 = generator.makeActor(None, 14, 9, 'static', moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('hatch')['id'], name='actor_8d4b2968-7f8c-430e-a48d-a255880b0607')
        actor_name_table.update({'actor_8d4b2968-7f8c-430e-a48d-a255880b0607': actor_00})
        actor_00['script'] = [
                script.text(text=['You move the\nhatch.'], avatarId=''),
                script.actorSetPosition(actorId='♔REFERENCE_TO_ACTORS_<$self$>♔', x=16, y=9),
                script.end()
            ]
        actor_list = [actor_00]
        trigger_00 = generator.makeTrigger('trigger_00', 0, 8, 1, 2)
        trigger_01 = generator.makeTrigger('trigger_01', 8, 0, 4, 1)
        trigger_02 = generator.makeTrigger('trigger_02', 14, 8, 2, 2)
        trigger_list = []
        collision_data_list = [255, 48, 16, 4, 2, 193, 97, 48, 12, 4, 195, 195, 240, 31, 8, 231, 231, 112, 54, 28, 64, 195, 1, 40, 48, 159, 6, 146, 112, 32, 56, 15, 131, 97, 16, 114, 224, 49, 3, 2, 193, 63, 0, 0, 0]
        gen_scene_bkg = generator.makeBackground("Forest_01_2d.png")

        gen_scene_scn = generator.makeScene("_gen_Forest4", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Forest4_00004")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (1, 9), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 8), 'entrance_size': (1, 2)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (10, 1), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (8, 0), 'entrance_size': (4, 1)  } }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (14, 10), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (14, 8), 'entrance_size': (2, 2)  } }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Forest5_00005(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 8, 0, 4, 1)
        trigger_01 = generator.makeTrigger('trigger_01', 0, 12, 1, 2)
        trigger_02 = generator.makeTrigger('trigger_02', 10, 17, 2, 1)
        trigger_list = []
        collision_data_list = [128, 112, 0, 8, 7, 128, 249, 0, 158, 31, 32, 192, 1, 1, 28, 16, 143, 129, 240, 24, 12, 207, 113, 240, 24, 1, 143, 17, 0, 24, 240, 192, 1, 6, 12, 255, 225, 0, 12, 6, 128, 115, 0, 56, 7]
        gen_scene_bkg = generator.makeBackground("Forest_01_2e.png")

        gen_scene_scn = generator.makeScene("_gen_Forest5", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Forest5_00005")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (9, 1), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (8, 0), 'entrance_size': (4, 1)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (1, 12), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 12), 'entrance_size': (1, 2)  } }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (10, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (10, 17), 'entrance_size': (2, 1)  } }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Forest6_00006(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 8, 17, 2, 1)
        trigger_01 = generator.makeTrigger('trigger_01', 9, 6, 2, 1)
        trigger_list = []
        collision_data_list = [1, 0, 0, 0, 0, 128, 15, 0, 248, 0, 192, 27, 0, 254, 1, 224, 121, 0, 158, 7, 240, 80, 0, 15, 7, 240, 57, 128, 15, 3, 248, 60, 128, 135, 3, 120, 120, 128, 3, 7, 248, 124, 128, 207, 7]
        gen_scene_bkg = generator.makeBackground("Forest_01_2f.png")

        gen_scene_scn = generator.makeScene("_gen_Forest6", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Forest6_00006")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (8, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (8, 17), 'entrance_size': (2, 1)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (9, 7), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (9, 6), 'entrance_size': (2, 1)  } }

        gen_scene_connections = [connection_00, connection_01]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Forest7_00007(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 8, 17, 4, 1)
        trigger_list = []
        collision_data_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 224, 255, 1, 254, 31, 224, 225, 1, 12, 60, 192, 204, 3, 204, 124, 192, 225, 7, 28, 126, 192, 243, 7, 28, 126, 192, 225, 7, 14, 124, 224, 240, 15, 14, 255]
        gen_scene_bkg = generator.makeBackground("Forest_01_2g.png")

        gen_scene_scn = generator.makeScene("_gen_Forest7", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Forest7_00007")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (10, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (8, 17), 'entrance_size': (4, 1)  } }

        gen_scene_connections = [connection_00]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Forest8_00008(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 10, 17, 3, 1)
        trigger_01 = generator.makeTrigger('trigger_01', 4, 0, 2, 1)
        trigger_02 = generator.makeTrigger('trigger_02', 12, 0, 2, 1)
        trigger_list = []
        collision_data_list = [205, 207, 207, 120, 56, 144, 31, 6, 113, 64, 56, 15, 7, 113, 32, 144, 159, 3, 241, 16, 48, 207, 1, 98, 8, 96, 230, 0, 4, 4, 192, 112, 0, 8, 2, 128, 57, 0, 16, 1, 0, 51, 0, 32, 2]
        gen_scene_bkg = generator.makeBackground("Forest_01_2h.png")

        gen_scene_scn = generator.makeScene("_gen_Forest8", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Forest8_00008")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (10, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (10, 17), 'entrance_size': (3, 1)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (5, 2), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (4, 0), 'entrance_size': (2, 1)  } }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (13, 1), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (12, 0), 'entrance_size': (2, 1)  } }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Forest9_00009(callback):
        actor_name_table = {}
        actor_list = []
        trigger_list = []
        collision_data_list = []
        gen_scene_bkg = generator.makeBackground("Forest_01_2i.png")

        gen_scene_scn = generator.makeScene("_gen_Forest9", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Forest9_00009")

        gen_scene_connections = []
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Forest10_00010(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 2, 0, 2, 1)
        trigger_01 = generator.makeTrigger('trigger_01', 9, 6, 2, 2)
        trigger_list = []
        collision_data_list = [19, 0, 48, 3, 0, 33, 0, 16, 2, 0, 51, 0, 16, 242, 0, 39, 121, 48, 156, 7, 15, 112, 112, 0, 14, 30, 224, 224, 0, 12, 60, 252, 192, 129, 15, 252, 63, 0, 255, 3, 0, 0, 0, 0, 0]
        gen_scene_bkg = generator.makeBackground("Forest_01_2k.png")

        gen_scene_scn = generator.makeScene("_gen_Forest10", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Forest10_00010")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (2, 1), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (2, 0), 'entrance_size': (2, 1)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (9, 8), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (9, 6), 'entrance_size': (2, 2)  } }

        gen_scene_connections = [connection_00, connection_01]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Forest11_00011(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 0, 6, 1, 4)
        trigger_01 = generator.makeTrigger('trigger_01', 19, 6, 1, 2)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 159, 255, 255, 240, 255, 3, 255, 63, 224, 255, 96, 230, 1, 6, 14, 252, 192, 204, 7, 132, 127, 96, 254, 3, 192, 63, 0, 255, 1, 224, 127, 248, 255, 3, 255, 255, 255, 255, 255, 255]
        gen_scene_bkg = generator.makeBackground("Forest_01_2l.png")

        gen_scene_scn = generator.makeScene("_gen_Forest11", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Forest11_00011")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (1, 7), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 6), 'entrance_size': (1, 4)  } }

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


    def scene_gen_Forest12_00012(callback):
        actor_name_table = {}
        actor_00 = generator.makeActor(None, 12, 9, 'static', moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('shovel')['id'], name='actor_1699a77d-10d6-4e2f-941d-04cf112fba61')
        actor_name_table.update({'actor_1699a77d-10d6-4e2f-941d-04cf112fba61': actor_00})
        actor_00['startScript'] = [
                script.ifFlagsCompare(variable='27', flag='0', children = {
                    'true': [script.actorHide(actorId='♔REFERENCE_TO_ACTORS_<$self$>♔'), script.end()],
                    'false': [script.end()]
                }),
                script.end()
            ]
        actor_00['script'] = [
                script.actorHide(actorId='♔REFERENCE_TO_ACTORS_<$self$>♔'),
                script.text(text=['You picked up\nthe shovel'], avatarId='96894897-c21a-49b4-8d1e-214ba5735525'),
                script.addFlags(variable='27', flag1=True, flag2=False, flag3=False, flag4=False, flag5=False, flag6=False, flag7=False, flag8=False),
                script.end()
            ]
        actor_list = [actor_00]
        trigger_00 = generator.makeTrigger('trigger_00', 0, 7, 1, 3)
        trigger_01 = generator.makeTrigger('trigger_01', 8, 0, 4, 1)
        trigger_02 = generator.makeTrigger('trigger_02', 19, 12, 1, 2)
        trigger_list = []
        collision_data_list = [192, 240, 15, 4, 129, 96, 24, 8, 130, 128, 35, 207, 248, 241, 143, 129, 135, 8, 56, 144, 248, 3, 201, 32, 144, 7, 134, 9, 64, 240, 0, 12, 0, 128, 0, 0, 248, 15, 0, 255, 0, 0, 0, 0, 0]
        gen_scene_bkg = generator.makeBackground("Forest_01_2m.png")

        gen_scene_scn = generator.makeScene("_gen_Forest12", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Forest12_00012")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (1, 7), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 7), 'entrance_size': (1, 3)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (9, 1), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (8, 0), 'entrance_size': (4, 1)  } }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (17, 13), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 12), 'entrance_size': (1, 2)  } }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Forest13_00013(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 0, 4, 1, 2)
        trigger_01 = generator.makeTrigger('trigger_01', 10, 8, 2, 2)
        trigger_list = []
        collision_data_list = [1, 0, 0, 0, 0, 63, 0, 240, 3, 0, 240, 1, 0, 63, 0, 225, 63, 16, 254, 255, 243, 243, 31, 62, 255, 231, 1, 56, 28, 128, 15, 255, 124, 224, 71, 127, 0, 246, 7, 32, 255, 63, 243, 255, 51]
        gen_scene_bkg = generator.makeBackground("Forest_01_2n.png")

        gen_scene_scn = generator.makeScene("_gen_Forest13", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Forest13_00013")

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
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (10, 10), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (10, 8), 'entrance_size': (2, 2)  } }

        gen_scene_connections = [connection_00, connection_01]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Forest14_00014(callback):
        actor_name_table = {}
        actor_00 = generator.makeActor(None, 8, 8, 'static', moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('invisible')['id'], name='actor_f2e5a00f-cbf1-4d54-ae48-11b0ac1caf1d')
        actor_name_table.update({'actor_f2e5a00f-cbf1-4d54-ae48-11b0ac1caf1d': actor_00})
        actor_00['startScript'] = [
                script.ifFlagsCompare(variable='27', flag='0', children = {
                    'true': [script.actorHide(actorId='♔REFERENCE_TO_ACTORS_<$self$>♔'), script.end()],
                    'false': [script.end()]
                }),
                script.end()
            ]
        actor_00['script'] = [
                script.text(text=["There's something\nburied at the\nbottom of the well"], avatarId=''),
                script.end()
            ]
        actor_list = [actor_00]
        trigger_00 = generator.makeTrigger('trigger_00', 8, 8, 2, 1)
        trigger_01 = generator.makeTrigger('trigger_01', 12, 0, 2, 1)
        trigger_02 = generator.makeTrigger('trigger_02', 0, 12, 1, 2)
        trigger_list = []
        collision_data_list = [1, 200, 15, 128, 248, 0, 152, 15, 128, 241, 224, 63, 15, 254, 227, 112, 120, 14, 3, 199, 48, 240, 12, 51, 199, 126, 120, 254, 3, 227, 252, 51, 135, 31, 113, 1, 128, 19, 0, 48, 255, 255, 1, 0, 0]
        gen_scene_bkg = generator.makeBackground("Forest_01_2o.png")

        gen_scene_scn = generator.makeScene("_gen_Forest14", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Forest14_00014")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (8, 7), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (8, 8), 'entrance_size': (2, 1)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (13, 1), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (12, 0), 'entrance_size': (2, 1)  } }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (1, 13), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 12), 'entrance_size': (1, 2)  } }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def catalog():
        """
        Returns a list of scene functions from this part of the library.
        """
        return [scene_gen_Forest1_00001,
            scene_gen_Forest2_00002,
            scene_gen_Forest3_00003,
            scene_gen_Forest4_00004,
            scene_gen_Forest5_00005,
            scene_gen_Forest6_00006,
            scene_gen_Forest7_00007,
            scene_gen_Forest8_00008,
            scene_gen_Forest9_00009,
            scene_gen_Forest10_00010,
            scene_gen_Forest11_00011,
            scene_gen_Forest12_00012,
            scene_gen_Forest13_00013,
            scene_gen_Forest14_00014]

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

