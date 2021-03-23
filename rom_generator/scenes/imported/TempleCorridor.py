# Generated Scene Functions
# TempleCorridor.py

from rom_generator import generator
from rom_generator import script_functions as script

test_generation_destination_path = "../gbprojects/generated_export_test_TempleCorridor/"

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

    def scene_gen_temple_corridor_01_00001(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 10, 4, 10, 1)
        trigger_01 = generator.makeTrigger('trigger_01', 0, 14, 1, 4)
        trigger_02 = generator.makeTrigger('trigger_02', 29, 16, 1, 2)
        trigger_03 = generator.makeTrigger('trigger_03', 4, 0, 2, 1)
        trigger_04 = generator.makeTrigger('trigger_04', 23, 0, 3, 1)
        trigger_list = []
        collision_data_list = [207, 255, 127, 252, 195, 255, 15, 31, 240, 255, 3, 7, 252, 255, 192, 1, 51, 51, 112, 192, 204, 12, 28, 48, 51, 3, 7, 204, 204, 192, 1, 0, 0, 112, 0, 0, 0, 28, 0, 0, 0, 7, 0, 0, 192, 1, 0, 0, 112, 0, 0, 0, 12, 0, 0, 0, 3, 0, 0, 192, 0, 0, 0, 0, 0, 0, 0, 0]
        gen_scene_bkg = generator.makeBackground("corridors_01.png")

        gen_scene_scn = generator.makeScene("_gen_temple_corridor_01", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_temple_corridor_01_00001")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (14, 5), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (10, 4), 'entrance_size': (10, 1)  }, 'tags': ['B'] }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (1, 16), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 14), 'entrance_size': (1, 4)  }, 'tags': ['B']  }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (27, 17), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (29, 16), 'entrance_size': (1, 2)  }, 'tags': ['B']  }

        def addConnection_03(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_03 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_03['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_03
        connection_03 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_03, 'args': { 'exit_location': (4, 1), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (4, 0), 'entrance_size': (2, 1)  }, 'tags': ['B']  }

        def addConnection_04(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_04 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_04['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_04
        connection_04 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_04, 'args': { 'exit_location': (24, 1), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (23, 0), 'entrance_size': (3, 1)  }, 'tags': ['B']  }

        gen_scene_connections = [connection_00, connection_01, connection_02, connection_03, connection_04]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_temple_corridor_02_00002(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 6, 5, 8, 1)
        trigger_01 = generator.makeTrigger('trigger_01', 8, 29, 4, 1)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 3, 252, 3, 0, 60, 0, 192, 255, 240, 255, 15, 255, 255, 240, 255, 15, 255, 255, 240, 255, 15, 255, 255, 240, 255, 15, 255, 255, 240, 255, 15, 255, 255, 240, 255, 15, 255, 255, 240, 255, 15, 255, 255, 240, 255, 15, 255, 255, 240, 255, 15, 255, 255, 240, 255, 15, 255, 255, 240, 255, 15, 255]
        gen_scene_bkg = generator.makeBackground("corridors_02.png")

        gen_scene_scn = generator.makeScene("_gen_temple_corridor_02", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_temple_corridor_02_00002")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (9, 6), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (6, 5), 'entrance_size': (8, 1)  }, 'tags': ['B']  }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (9, 28), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (8, 29), 'entrance_size': (4, 1)  }, 'tags': ['B']  }

        gen_scene_connections = [connection_00, connection_01]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_temple_corridor_03_00003(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 8, 5, 4, 1)
        trigger_01 = generator.makeTrigger('trigger_01', 0, 18, 1, 4)
        trigger_02 = generator.makeTrigger('trigger_02', 6, 29, 10, 1)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 15, 255, 207, 48, 255, 12, 243, 207, 48, 255, 12, 243, 207, 48, 63, 0, 192, 3, 0, 60, 0, 192, 3, 0, 60, 0, 192, 3, 0, 60, 0, 192, 0, 0, 15, 0, 240, 0, 0, 15, 0, 240, 3, 51, 63, 48, 243, 3, 51, 63, 48, 243, 63, 0, 255, 3, 240, 63, 0, 255, 3, 240]
        gen_scene_bkg = generator.makeBackground("corridors_03.png")

        gen_scene_scn = generator.makeScene("_gen_temple_corridor_03", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_temple_corridor_03_00003")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (9, 6), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (8, 5), 'entrance_size': (4, 1)  }, 'tags': ['B']  }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (1, 20), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 18), 'entrance_size': (1, 4)  }, 'tags': ['B']  }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (10, 28), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (6, 29), 'entrance_size': (10, 1)  }, 'tags': ['B']  }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_temple_corridor_04_00004(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 0, 6, 1, 10)
        trigger_01 = generator.makeTrigger('trigger_01', 29, 6, 1, 10)
        trigger_02 = generator.makeTrigger('trigger_02', 18, 5, 2, 1)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 252, 15, 12, 12, 12, 0, 3, 3, 3, 192, 192, 192, 0, 48, 48, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 63]
        gen_scene_bkg = generator.makeBackground("corridors_04.png")

        gen_scene_scn = generator.makeScene("_gen_temple_corridor_04", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_temple_corridor_04_00004")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (1, 11), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 6), 'entrance_size': (1, 10)  }, 'tags': ['B']  }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (27, 11), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (29, 6), 'entrance_size': (1, 10)  }, 'tags': ['B']  }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (18, 6), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (18, 5), 'entrance_size': (2, 1)  }, 'tags': ['B']  }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_temple_corridor_05_00005(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 0, 3, 1, 8)
        trigger_01 = generator.makeTrigger('trigger_01', 17, 0, 6, 1)
        trigger_02 = generator.makeTrigger('trigger_02', 7, 2, 2, 1)
        trigger_list = []
        collision_data_list = [255, 255, 129, 224, 255, 127, 32, 248, 231, 31, 8, 2, 0, 0, 130, 0, 0, 128, 32, 0, 0, 32, 8, 0, 0, 8, 2, 0, 0, 130, 0, 0, 128, 32, 0, 0, 32, 8, 0, 0, 8, 254, 255, 255, 131, 255, 127, 248, 224, 255, 31, 62, 248, 255, 135, 15, 2, 0, 0, 128, 0, 0, 0, 32, 0, 0, 0, 8]
        gen_scene_bkg = generator.makeBackground("corridors_05.png")

        gen_scene_scn = generator.makeScene("_gen_temple_corridor_05", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_temple_corridor_05_00005")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (1, 8), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 3), 'entrance_size': (1, 8)  }, 'tags': ['B']  }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (19, 1), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (17, 0), 'entrance_size': (6, 1)  }, 'tags': ['B']  }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (7, 3), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (7, 2), 'entrance_size': (2, 1)  }, 'tags': ['B']  }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_temple_corridor_06_00006(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 0, 6, 1, 13)
        trigger_01 = generator.makeTrigger('trigger_01', 19, 6, 1, 13)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 128, 16, 0, 8, 1, 128, 16, 0, 8, 1, 128, 16, 0, 8, 1, 128, 16, 0, 8, 1, 128, 16, 0, 8, 1, 128, 16, 0, 8, 1, 128, 16, 240, 15, 255, 255, 240, 255, 15, 255, 255, 240, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        gen_scene_bkg = generator.makeBackground("corridors_06.png")

        gen_scene_scn = generator.makeScene("_gen_temple_corridor_06", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_temple_corridor_06_00006")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (1, 16), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 6), 'entrance_size': (1, 13)  }, 'tags': ['B']  }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (17, 7), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 6), 'entrance_size': (1, 13)  }, 'tags': ['B']  }

        gen_scene_connections = [connection_00, connection_01]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def catalog():
        """
        Returns a list of scene functions from this part of the library.
        """
        return [scene_gen_temple_corridor_01_00001,
            scene_gen_temple_corridor_02_00002,
            scene_gen_temple_corridor_03_00003,
            scene_gen_temple_corridor_04_00004,
            scene_gen_temple_corridor_05_00005,
            scene_gen_temple_corridor_06_00006]

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
