# Generated Scene Functions
# SewerArea.py

from rom_generator import generator
from rom_generator import script_functions as script
import random

test_generation_destination_path = "../gbprojects/generated_export_test_SewerArea/"

def scene_generation():
    sprite_sheet_data = [
        generator.makeSpriteSheet('actor.png', name='actor', type='actor', frames=3),
        generator.makeSpriteSheet('actor_animated.png', name='actor_animated', type='actor_animated', frames=6),
        generator.makeSpriteSheet('bubbles1.png', name='bubbles1', type='animated', frames=4),
        generator.makeSpriteSheet('bubbles2.png', name='bubbles2', type='animated', frames=4),
        generator.makeSpriteSheet('cat.png', name='cat', type='static', frames=1),
        generator.makeSpriteSheet('savepoint.png', name='savepoint', type='animated', frames=2),
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

    def scene_gen_Sewer01_00001(callback):
        actor_name_table = {}
        actor_00 = generator.makeActor(None, 9, 16, 'static', animate=True, moveSpeed=1, animSpeed=1, direction='down', script=[], sprite_id=findSpriteByName('bubbles1')['id'], name='actor_333a1e1d-5cd3-40c3-8057-8eb9575d5dbe')
        actor_name_table.update({'actor_333a1e1d-5cd3-40c3-8057-8eb9575d5dbe': actor_00})
        actor_list = [actor_00]
        trigger_00 = generator.makeTrigger('trigger_00', 0, 3, 1, 7)
        trigger_01 = generator.makeTrigger('trigger_01', 19, 3, 1, 7)
        trigger_02 = generator.makeTrigger('trigger_02', 19, 25, 1, 2)
        trigger_03 = generator.makeTrigger('trigger_03', 9, 31, 2, 1)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 255, 255, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 159, 255, 255, 249, 255, 255, 255, 255, 255, 255, 7, 254, 127, 224, 255, 7, 254, 127, 224, 255, 7, 252, 127, 128, 255, 7, 0, 127, 32, 240, 7, 254, 127, 224, 255, 7, 254, 255, 249, 255, 159, 255]
        gen_scene_bkg = generator.makeBackground("sewer_01.png")

        gen_scene_scn = generator.makeScene("_gen_Sewer01", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Sewer01_00001")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (1, 6), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 3), 'entrance_size': (1, 7)  }, 'tags': ['A']  }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (17, 7), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 3), 'entrance_size': (1, 7)  }, 'tags': ['A']  }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (17, 26), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 25), 'entrance_size': (1, 2)  }, 'tags': ['A']  }

        def addConnection_03(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_03 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_03['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_03
        connection_03 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_03, 'args': { 'exit_location': (9, 30), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (9, 31), 'entrance_size': (2, 1)  }, 'tags': ['A']  }

        gen_scene_connections = [connection_00, connection_01, connection_02, connection_03]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data

    def scene_gen_Sewer01_00001_upper(callback):
        actor_name_table = {}
        actor_00 = generator.makeActor(None, 9, 16, 'static', animate=True, moveSpeed=1, animSpeed=1, direction='down', script=[], sprite_id=findSpriteByName('bubbles1')['id'], name='actor_333a1e1d-5cd3-40c3-8057-8eb9575d5dbe')
        actor_name_table.update({'actor_333a1e1d-5cd3-40c3-8057-8eb9575d5dbe': actor_00})
        actor_list = [actor_00]
        trigger_00 = generator.makeTrigger('trigger_00', 0, 3, 1, 7)
        trigger_01 = generator.makeTrigger('trigger_01', 19, 3, 1, 7)
        trigger_02 = generator.makeTrigger('trigger_02', 19, 25, 1, 2)
        trigger_03 = generator.makeTrigger('trigger_03', 9, 31, 2, 1)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 255, 255, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 159, 255, 255, 249, 255, 255, 255, 255, 255, 255, 7, 254, 127, 224, 255, 7, 254, 127, 224, 255, 7, 252, 127, 128, 255, 7, 0, 127, 32, 240, 7, 254, 127, 224, 255, 7, 254, 255, 249, 255, 159, 255]
        gen_scene_bkg = generator.makeBackground("sewer_01.png")

        gen_scene_scn = generator.makeScene("_gen_Sewer01", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Sewer01_00001")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (1, 6), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 3), 'entrance_size': (1, 7)  }, 'tags': ['A']  }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (17, 7), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 3), 'entrance_size': (1, 7)  }, 'tags': ['A']  }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (17, 26), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 25), 'entrance_size': (1, 2)  }, 'tags': ['A']  }

        def addConnection_03(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_03 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_03['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_03
        connection_03 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_03, 'args': { 'exit_location': (9, 30), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (9, 31), 'entrance_size': (2, 1)  }, 'tags': ['A']  }

        gen_scene_connections = [connection_00, connection_01]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data

    def scene_gen_Sewer01_00001_lower(callback):
        actor_name_table = {}
        actor_00 = generator.makeActor(None, 9, 16, 'static', animate=True, moveSpeed=1, animSpeed=1, direction='down', script=[], sprite_id=findSpriteByName('bubbles1')['id'], name='actor_333a1e1d-5cd3-40c3-8057-8eb9575d5dbe')
        actor_name_table.update({'actor_333a1e1d-5cd3-40c3-8057-8eb9575d5dbe': actor_00})
        actor_list = [actor_00]
        trigger_00 = generator.makeTrigger('trigger_00', 0, 3, 1, 7)
        trigger_01 = generator.makeTrigger('trigger_01', 19, 3, 1, 7)
        trigger_02 = generator.makeTrigger('trigger_02', 19, 25, 1, 2)
        trigger_03 = generator.makeTrigger('trigger_03', 9, 31, 2, 1)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 255, 255, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 159, 255, 255, 249, 255, 255, 255, 255, 255, 255, 7, 254, 127, 224, 255, 7, 254, 127, 224, 255, 7, 252, 127, 128, 255, 7, 0, 127, 32, 240, 7, 254, 127, 224, 255, 7, 254, 255, 249, 255, 159, 255]
        gen_scene_bkg = generator.makeBackground("sewer_01.png")

        gen_scene_scn = generator.makeScene("_gen_Sewer01", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Sewer01_00001")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (1, 6), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 3), 'entrance_size': (1, 7)  }, 'tags': ['A']  }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (17, 7), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 3), 'entrance_size': (1, 7)  }, 'tags': ['A']  }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (17, 26), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 25), 'entrance_size': (1, 2)  }, 'tags': ['A']  }

        def addConnection_03(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_03 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_03['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_03
        connection_03 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_03, 'args': { 'exit_location': (9, 30), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (9, 31), 'entrance_size': (2, 1)  }, 'tags': ['A']  }

        gen_scene_connections = [connection_02, connection_03]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data

    def scene_gen_Sewer02_00002(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 0, 6, 1, 3)
        trigger_01 = generator.makeTrigger('trigger_01', 19, 6, 1, 3)
        trigger_02 = generator.makeTrigger('trigger_02', 9, 4, 2, 2)
        trigger_03 = generator.makeTrigger('trigger_03', 19, 21, 1, 5)
        trigger_04 = generator.makeTrigger('trigger_04', 0, 21, 1, 5)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 249, 255, 159, 255, 0, 0, 0, 0, 0, 0, 0, 240, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
        gen_scene_bkg = generator.makeBackground("sewer_02.png")

        gen_scene_scn = generator.makeScene("_gen_Sewer02", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Sewer02_00002")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (1, 8), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 6), 'entrance_size': (1, 3)  }, 'tags': ['A']  }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (17, 8), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 6), 'entrance_size': (1, 3)  }, 'tags': ['A']  }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (9, 6), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (9, 4), 'entrance_size': (2, 2)  }, 'tags': ['A']  }

        def addConnection_03(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_03 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_03['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_03
        connection_03 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_03, 'args': { 'exit_location': (17, 23), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 21), 'entrance_size': (1, 5)  } }

        def addConnection_04(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_04 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_04['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_04
        connection_04 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_04, 'args': { 'exit_location': (1, 23), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 21), 'entrance_size': (1, 5)  }, 'tags': ['A']  }

        gen_scene_connections = [connection_00, connection_01, connection_02, connection_03, connection_04]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data

    def scene_gen_Sewer02_00002_lower(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 0, 6, 1, 3)
        trigger_01 = generator.makeTrigger('trigger_01', 19, 6, 1, 3)
        trigger_02 = generator.makeTrigger('trigger_02', 9, 4, 2, 2)
        trigger_03 = generator.makeTrigger('trigger_03', 19, 21, 1, 5)
        trigger_04 = generator.makeTrigger('trigger_04', 0, 21, 1, 5)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 249, 255, 159, 255, 0, 0, 0, 0, 0, 0, 0, 240, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
        gen_scene_bkg = generator.makeBackground("sewer_02.png")

        gen_scene_scn = generator.makeScene("_gen_Sewer02_lower", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Sewer02_00002")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (1, 8), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 6), 'entrance_size': (1, 3)  }, 'tags': ['A']  }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (17, 8), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 6), 'entrance_size': (1, 3)  }, 'tags': ['A']  }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (9, 6), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (9, 4), 'entrance_size': (2, 2)  }, 'tags': ['A']  }

        def addConnection_03(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_03 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_03['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_03
        connection_03 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_03, 'args': { 'exit_location': (17, 23), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 21), 'entrance_size': (1, 5)  }, 'tags': ['A'] }

        def addConnection_04(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_04 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_04['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_04
        connection_04 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_04, 'args': { 'exit_location': (1, 23), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 21), 'entrance_size': (1, 5)  }, 'tags': ['A']  }

        gen_scene_connections = [connection_03, connection_04]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data

    def scene_gen_Sewer02_00002_upper(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 0, 6, 1, 3)
        trigger_01 = generator.makeTrigger('trigger_01', 19, 6, 1, 3)
        trigger_02 = generator.makeTrigger('trigger_02', 9, 4, 2, 2)
        trigger_03 = generator.makeTrigger('trigger_03', 19, 21, 1, 5)
        trigger_04 = generator.makeTrigger('trigger_04', 0, 21, 1, 5)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 249, 255, 159, 255, 0, 0, 0, 0, 0, 0, 0, 240, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
        gen_scene_bkg = generator.makeBackground("sewer_02.png")

        gen_scene_scn = generator.makeScene("_gen_Sewer02", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Sewer02_00002")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (1, 8), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 6), 'entrance_size': (1, 3)  }, 'tags': ['A']  }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (17, 8), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 6), 'entrance_size': (1, 3)  }, 'tags': ['A']  }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (9, 6), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (9, 4), 'entrance_size': (2, 2)  }, 'tags': ['A']  }

        def addConnection_03(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_03 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_03['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_03
        connection_03 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_03, 'args': { 'exit_location': (17, 23), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 21), 'entrance_size': (1, 5)  } }

        def addConnection_04(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_04 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_04['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_04
        connection_04 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_04, 'args': { 'exit_location': (1, 23), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 21), 'entrance_size': (1, 5)  }, 'tags': ['A']  }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Sewer04_00003(callback):
        actor_name_table = {}
        actor_00 = generator.makeActor(None, 11, 6, 'static', moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('cat')['id'], name='actor_3dbb1c93-666a-423d-9b43-f102cd1b6965')
        actor_name_table.update({'actor_3dbb1c93-666a-423d-9b43-f102cd1b6965': actor_00})
        actor_00['script'] = [
                script.text(text=['Meow!'], avatarId=''),
                script.end()
            ]
        actor_list = [actor_00]
        trigger_00 = generator.makeTrigger('trigger_00', 25, 6, 1, 6)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 63, 0, 192, 255, 0, 0, 255, 3, 0, 252, 15, 0, 240, 63, 0, 192, 255, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 15]
        gen_scene_bkg = generator.makeBackground("sewer_04.png")

        gen_scene_scn = generator.makeScene("_gen_Sewer04", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Sewer04_00003")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (23, 9), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (25, 6), 'entrance_size': (1, 6)  }, 'tags': ['A']  }

        gen_scene_connections = [connection_00]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data

    def scene_gen_Sewer04_00003a(callback):
        actor_name_table = {}
        actor_00 = generator.makeActor(None, 11, 6, 'static', moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('cat')['id'], name='actor_3dbb1c93-666a-423d-9b43-f102cd1b6965')
        actor_name_table.update({'actor_3dbb1c93-666a-423d-9b43-f102cd1b6965': actor_00})
        actor_00['script'] = [
                script.text(text=['Meow! I\'m going to tell a lengthy story here to stress-test having long dialogs in the games. You can tell that this story goes on a while because you have to keep pressing buttons until it ends and I just won\'t stop talking.'], avatarId=''),
                script.end()
            ]
        actor_list = [actor_00]
        trigger_00 = generator.makeTrigger('trigger_00', 25, 6, 1, 6)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 63, 0, 192, 255, 0, 0, 255, 3, 0, 252, 15, 0, 240, 63, 0, 192, 255, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 15]
        gen_scene_bkg = generator.makeBackground("sewer_04.png")

        gen_scene_scn = generator.makeScene("_gen_Sewer04", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Sewer04_00003")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (23, 9), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (25, 6), 'entrance_size': (1, 6)  }, 'tags': ['A']  }

        gen_scene_connections = [connection_00]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Sewer05_00004(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 10, 1, 2, 2)
        trigger_01 = generator.makeTrigger('trigger_01', 0, 3, 1, 5)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 207, 255, 255, 63, 255, 63, 0, 0, 255, 0, 0, 252, 3, 0, 240, 15, 0, 64, 62, 0, 0, 249, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 15]
        gen_scene_bkg = generator.makeBackground("sewer_05.png")

        gen_scene_scn = generator.makeScene("_gen_Sewer05", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Sewer05_00004")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (10, 3), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (10, 1), 'entrance_size': (2, 2)  }, 'tags': ['A']  }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (1, 6), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 3), 'entrance_size': (1, 5)  }, 'tags': ['A']  }

        gen_scene_connections = [connection_00, connection_01]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Sewer03_00005(callback):
        actor_name_table = {}
        actor_00 = generator.makeActor(None, 13, 10, 'static', animate=True, moveSpeed=1, animSpeed=1, direction='down', script=[], sprite_id=findSpriteByName('bubbles2')['id'], name='actor_e01b1a16-322f-40cc-8720-09e08add9e8c')
        actor_name_table.update({'actor_e01b1a16-322f-40cc-8720-09e08add9e8c': actor_00})
        actor_list = [actor_00]
        trigger_00 = generator.makeTrigger('trigger_00', 0, 2, 1, 5)
        trigger_01 = generator.makeTrigger('trigger_01', 25, 2, 1, 5)
        trigger_02 = generator.makeTrigger('trigger_02', 5, 17, 15, 1)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 255, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 192, 15, 192, 7, 63, 252, 31, 252, 240, 127, 240, 195, 255, 193, 15, 255, 7, 63, 252, 31, 252, 240, 127, 240, 195, 255, 1, 3, 255, 7, 0, 252, 31, 0, 240, 127, 0, 192, 15]
        gen_scene_bkg = generator.makeBackground("sewer_03.png")

        gen_scene_scn = generator.makeScene("_gen_Sewer03", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Sewer03_00005")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (1, 5), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 2), 'entrance_size': (1, 5)  }, 'tags': ['A']  }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (23, 5), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (25, 2), 'entrance_size': (1, 5)  }, 'tags': ['A']  }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (8, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (5, 17), 'entrance_size': (15, 1)  }, 'tags': ['A']  }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Sewer06_00006(callback):
        actor_name_table = {}
        actor_00 = generator.makeActor(None, 12, 16, 'static', animate=True, moveSpeed=1, animSpeed=2, direction='down', script=[], sprite_id=findSpriteByName('bubbles1')['id'], name='actor_8a18c7fb-4296-43b5-a483-13bf9c251f7d')
        actor_name_table.update({'actor_8a18c7fb-4296-43b5-a483-13bf9c251f7d': actor_00})
        actor_list = [actor_00]
        trigger_00 = generator.makeTrigger('trigger_00', 21, 2, 2, 2)
        trigger_01 = generator.makeTrigger('trigger_01', 25, 6, 1, 5)
        trigger_02 = generator.makeTrigger('trigger_02', 0, 6, 1, 5)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 255, 255, 255, 255, 249, 255, 255, 231, 255, 127, 128, 255, 255, 0, 14, 0, 240, 15, 0, 224, 63, 0, 0, 0, 0, 0, 0, 0, 0, 0, 192, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 15]
        gen_scene_bkg = generator.makeBackground("sewer_06.png")

        gen_scene_scn = generator.makeScene("_gen_Sewer06", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Sewer06_00006")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (21, 4), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (21, 2), 'entrance_size': (2, 2)  }, 'tags': ['A']  }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (23, 10), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (25, 6), 'entrance_size': (1, 5)  }, 'tags': ['A']  }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (1, 10), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 6), 'entrance_size': (1, 5)  }, 'tags': ['A']  }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Sewer04a_00007(callback):
        actor_name_table = {}
        actor_00 = generator.makeActor(None, 11, 6, 'static', animate=True, moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('savepoint')['id'], name='actor_2eee8011-395f-4958-bd5e-f79a3833b4cf')
        actor_name_table.update({'actor_2eee8011-395f-4958-bd5e-f79a3833b4cf': actor_00})
        actor_00['script'] = [
                script.saveData(),
                script.text(text=['Game Saved'], avatarId=''),
                script.end()
            ]
        actor_list = [actor_00]
        trigger_00 = generator.makeTrigger('trigger_00', 25, 6, 1, 6)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 63, 0, 192, 255, 0, 0, 255, 3, 0, 252, 15, 0, 240, 63, 0, 192, 255, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 15]
        gen_scene_bkg = generator.makeBackground("sewer_04.png")

        gen_scene_scn = generator.makeScene("_gen_Sewer04a", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Sewer04a_00007")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (23, 9), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (25, 6), 'entrance_size': (1, 6)  }, 'tags': ['A']  }

        gen_scene_connections = [connection_00]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def catalog(sample=True):
        """
        Returns a list of scene functions from this part of the library.
        """
        cat = [scene_gen_Sewer01_00001_upper,
            scene_gen_Sewer01_00001_lower,
            scene_gen_Sewer02_00002_upper,
            scene_gen_Sewer02_00002_lower,
            scene_gen_Sewer04_00003,
            scene_gen_Sewer04_00003a,
            scene_gen_Sewer05_00004,
            scene_gen_Sewer03_00005,
            scene_gen_Sewer06_00006,
            scene_gen_Sewer04a_00007]

        if sample:
            catalog_sample = random.sample(cat, 4)
            return catalog_sample
        return cat

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
