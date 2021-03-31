# Generated Scene Functions
# So_Many_Rooms.py

from rom_generator import generator
from rom_generator import script_functions as script
import random

def scene_generation():
    sprite_sheet_data = [
        generator.makeSpriteSheet('cat.png', name='cat', type='static', frames=1),
        generator.makeSpriteSheet('checkbox.png', name='checkbox', type='actor', frames=3),
        generator.makeSpriteSheet('dog.png', name='dog', type='static', frames=1),
        generator.makeSpriteSheet('duck.png', name='duck', type='animated', frames=2),
        generator.makeSpriteSheet('fire.png', name='fire', type='animated', frames=4),
        generator.makeSpriteSheet('ice.png', name='ice', type='static', frames=1),
        generator.makeSpriteSheet('npc001.png', name='npc001', type='actor', frames=3),
        generator.makeSpriteSheet('npc002.png', name='npc002', type='actor', frames=3),
        generator.makeSpriteSheet('npc003.png', name='npc003', type='actor_animated', frames=6),
        generator.makeSpriteSheet('player.png', name='player', type='actor_animated', frames=6),
        generator.makeSpriteSheet('radio.png', name='radio', type='static', frames=1),
        generator.makeSpriteSheet('rock.png', name='rock', type='static', frames=1),
        generator.makeSpriteSheet('sage.png', name='sage', type='static', frames=1),
        generator.makeSpriteSheet('savepoint.png', name='savepoint', type='animated', frames=2),
        generator.makeSpriteSheet('signpost.png', name='signpost', type='static', frames=1),
        generator.makeSpriteSheet('torch.png', name='torch', type='static', frames=1)]

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

    def scene_gen_Room_1_00001(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 9, 0, 2, 1)
        trigger_01 = generator.makeTrigger('trigger_01', 9, 17, 2, 1)
        trigger_list = []
        collision_data_list = [255, 249, 255, 159, 255, 255, 249, 255, 159, 255, 255, 249, 255, 31, 192, 255, 1, 252, 255, 207, 255, 255, 28, 254, 207, 225, 255, 124, 30, 192, 231, 1, 124, 128, 255, 7, 248, 255, 159, 255, 255, 249, 255, 159, 255]
        gen_scene_bkg = generator.makeBackground("room1.png")

        gen_scene_scn = generator.makeScene("_gen_Room_1", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Room_1_00001")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (9, 1), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (9, 0), 'entrance_size': (2, 1)  }, 'tags': ['A'] }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (9, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (9, 17), 'entrance_size': (2, 1)  }, 'tags': ['A'] }

        gen_scene_connections = [connection_00, connection_01]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Scene_2_00002(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 10, 0, 2, 1)
        trigger_01 = generator.makeTrigger('trigger_01', 19, 6, 1, 2)
        trigger_02 = generator.makeTrigger('trigger_02', 16, 17, 2, 1)
        trigger_03 = generator.makeTrigger('trigger_03', 4, 17, 2, 1)
        trigger_04 = generator.makeTrigger('trigger_04', 0, 2, 1, 2)
        trigger_list = []
        collision_data_list = [255, 243, 255, 63, 255, 0, 3, 12, 48, 192, 63, 255, 252, 243, 207, 3, 15, 48, 240, 0, 243, 207, 63, 255, 252, 195, 3, 63, 60, 240, 207, 51, 252, 60, 195, 15, 240, 252, 0, 207, 207, 255, 252, 252, 207]
        gen_scene_bkg = generator.makeBackground("room2.png")

        gen_scene_scn = generator.makeScene("_gen_Scene_2", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Scene_2_00002")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (10, 1), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (10, 0), 'entrance_size': (2, 1)  }, 'tags': ['A'] }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (17, 7), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 6), 'entrance_size': (1, 2)  }, 'tags': ['A'] }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (16, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (16, 17), 'entrance_size': (2, 1)  }, 'tags': ['A'] }

        def addConnection_03(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_03 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_03['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_03
        connection_03 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_03, 'args': { 'exit_location': (4, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (4, 17), 'entrance_size': (2, 1)  }, 'tags': ['A'] }

        def addConnection_04(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_04 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_04['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_04
        connection_04 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_04, 'args': { 'exit_location': (1, 3), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 2), 'entrance_size': (1, 2)  }, 'tags': ['A'] }

        gen_scene_connections = [connection_00, connection_01, connection_02, connection_03, connection_04]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Scene_3_00003(callback):
        actor_name_table = {}
        actor_00 = generator.makeActor(None, 14, 12, 'static', moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('cat')['id'], name='actor_05a26f2b-a2be-45cc-a41e-ef90f9c7d1d6')
        actor_name_table.update({'actor_05a26f2b-a2be-45cc-a41e-ef90f9c7d1d6': actor_00})
        actor_list = [actor_00]
        trigger_00 = generator.makeTrigger('trigger_00', 0, 5, 1, 2)
        trigger_01 = generator.makeTrigger('trigger_01', 13, 0, 2, 1)
        trigger_02 = generator.makeTrigger('trigger_02', 15, 17, 2, 1)
        trigger_list = []
        collision_data_list = [255, 159, 255, 255, 249, 255, 31, 252, 0, 193, 15, 240, 12, 60, 207, 192, 243, 252, 63, 207, 255, 243, 252, 63, 207, 7, 16, 120, 0, 129, 231, 31, 120, 254, 129, 7, 0, 120, 0, 128, 255, 127, 254, 255, 231]
        gen_scene_bkg = generator.makeBackground("room3.png")

        gen_scene_scn = generator.makeScene("_gen_Scene_3", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Scene_3_00003")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (1, 6), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 5), 'entrance_size': (1, 2)  }, 'tags': ['A'] }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (13, 1), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (13, 0), 'entrance_size': (2, 1)  }, 'tags': ['A'] }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (15, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (15, 17), 'entrance_size': (2, 1)  }, 'tags': ['A'] }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Scene_4_00004(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 0, 1, 1, 2)
        trigger_01 = generator.makeTrigger('trigger_01', 17, 0, 2, 1)
        trigger_02 = generator.makeTrigger('trigger_02', 1, 17, 2, 1)
        trigger_03 = generator.makeTrigger('trigger_03', 16, 17, 2, 1)
        trigger_list = []
        collision_data_list = [255, 255, 9, 254, 159, 192, 255, 120, 248, 135, 143, 127, 252, 1, 224, 31, 0, 254, 63, 255, 255, 243, 255, 7, 248, 63, 128, 127, 224, 225, 7, 31, 62, 254, 231, 225, 127, 28, 255, 199, 249, 255, 156, 255, 207]
        gen_scene_bkg = generator.makeBackground("room4.png")

        gen_scene_scn = generator.makeScene("_gen_Scene_4", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Scene_4_00004")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (1, 2), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 1), 'entrance_size': (1, 2)  }, 'tags': ['A'] }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (17, 1), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (17, 0), 'entrance_size': (2, 1)  }, 'tags': ['A'] }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (1, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (1, 17), 'entrance_size': (2, 1)  }, 'tags': ['A'] }

        def addConnection_03(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_03 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_03['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_03
        connection_03 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_03, 'args': { 'exit_location': (16, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (16, 17), 'entrance_size': (2, 1)  }, 'tags': ['A'] }

        gen_scene_connections = [connection_00, connection_01, connection_02, connection_03]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Scene_5_00005(callback):
        actor_name_table = {}
        actor_00 = generator.makeActor(None, 14, 5, 'randomWalk', moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('npc001')['id'], name='actor_952e2671-890b-4086-9be2-8330dbd5c54e')
        actor_name_table.update({'actor_952e2671-890b-4086-9be2-8330dbd5c54e': actor_00})
        actor_01 = generator.makeActor(None, 11, 2, 'randomWalk', moveSpeed=2, animSpeed=3, direction='right', script=[], sprite_id=findSpriteByName('npc001')['id'], name='actor_06d568c6-0402-426c-97f4-e5dcaa0af743')
        actor_name_table.update({'actor_06d568c6-0402-426c-97f4-e5dcaa0af743': actor_01})
        actor_02 = generator.makeActor(None, 16, 3, 'randomWalk', moveSpeed=3, animSpeed=3, direction='right', script=[], sprite_id=findSpriteByName('npc001')['id'], name='actor_6e727468-e92a-4278-832e-4a1656a4ad11')
        actor_name_table.update({'actor_6e727468-e92a-4278-832e-4a1656a4ad11': actor_02})
        actor_03 = generator.makeActor(None, 12, 7, 'randomWalk', moveSpeed=4, animSpeed=3, direction='up', script=[], sprite_id=findSpriteByName('npc001')['id'], name='actor_f3052938-84d7-4eb7-9e12-c5a02c05d0ba')
        actor_name_table.update({'actor_f3052938-84d7-4eb7-9e12-c5a02c05d0ba': actor_03})
        actor_04 = generator.makeActor(None, 16, 7, 'randomWalk', moveSpeed=0, animSpeed=3, direction='left', script=[], sprite_id=findSpriteByName('npc001')['id'], name='actor_347158f0-1b1a-492a-a5a8-714de301528d')
        actor_name_table.update({'actor_347158f0-1b1a-492a-a5a8-714de301528d': actor_04})
        actor_list = [actor_00, actor_01, actor_02, actor_03, actor_04]
        trigger_00 = generator.makeTrigger('trigger_00', 15, 0, 2, 1)
        trigger_01 = generator.makeTrigger('trigger_01', 19, 3, 1, 2)
        trigger_02 = generator.makeTrigger('trigger_02', 0, 9, 1, 2)
        trigger_03 = generator.makeTrigger('trigger_03', 15, 17, 2, 1)
        trigger_04 = generator.makeTrigger('trigger_04', 13, 8, 2, 2)
        trigger_04['script'] = [
                script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<952e2671-890b-4086-9be2-8330dbd5c54e>♔', direction='down'),
                script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<06d568c6-0402-426c-97f4-e5dcaa0af743>♔', direction='down'),
                script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<6e727468-e92a-4278-832e-4a1656a4ad11>♔', direction='down'),
                script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<f3052938-84d7-4eb7-9e12-c5a02c05d0ba>♔', direction='down'),
                script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<347158f0-1b1a-492a-a5a8-714de301528d>♔', direction='down'),
                script.end()
            ]
        trigger_05 = generator.makeTrigger('trigger_05', 10, 5, 2, 2)
        trigger_05['script'] = [
                script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<952e2671-890b-4086-9be2-8330dbd5c54e>♔', direction='left'),
                script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<06d568c6-0402-426c-97f4-e5dcaa0af743>♔', direction='left'),
                script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<6e727468-e92a-4278-832e-4a1656a4ad11>♔', direction='left'),
                script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<f3052938-84d7-4eb7-9e12-c5a02c05d0ba>♔', direction='left'),
                script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<347158f0-1b1a-492a-a5a8-714de301528d>♔', direction='left'),
                script.end()
            ]
        trigger_list = [trigger_04, trigger_05]
        collision_data_list = [255, 127, 254, 127, 128, 255, 7, 248, 127, 0, 255, 7, 240, 1, 128, 31, 0, 248, 121, 128, 159, 7, 8, 248, 249, 128, 159, 127, 254, 129, 231, 31, 24, 192, 231, 1, 124, 30, 0, 224, 1, 0, 254, 255, 231]
        gen_scene_bkg = generator.makeBackground("room5.png")

        gen_scene_scn = generator.makeScene("_gen_Scene_5", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Scene_5_00005")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (15, 1), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (15, 0), 'entrance_size': (2, 1)  }, 'tags': ['A'] }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (17, 4), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 3), 'entrance_size': (1, 2)  }, 'tags': ['A'] }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (1, 10), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 9), 'entrance_size': (1, 2)  }, 'tags': ['A'] }

        def addConnection_03(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_03 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_03['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_03
        connection_03 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_03, 'args': { 'exit_location': (15, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (15, 17), 'entrance_size': (2, 1)  }, 'tags': ['A'] }

        gen_scene_connections = [connection_00, connection_01, connection_02, connection_03]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Scene_6_00006(callback):
        actor_name_table = {}
        actor_00 = generator.makeActor(None, 16, 1, 'static', animate=True, moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('fire')['id'], name='actor_8462f086-7b40-4e93-a9a2-5e7e198b6774')
        actor_name_table.update({'actor_8462f086-7b40-4e93-a9a2-5e7e198b6774': actor_00})
        actor_00['startScript'] = [
                script.actorHide(actorId='♔REFERENCE_TO_ACTORS_<$self$>♔'),
                script.end()
            ]
        actor_01 = generator.makeActor(None, 14, 1, 'static', animate=True, moveSpeed=1, animSpeed=2, direction='down', script=[], sprite_id=findSpriteByName('fire')['id'], name='actor_81223844-bafc-4aae-bd14-9239801a81da')
        actor_name_table.update({'actor_81223844-bafc-4aae-bd14-9239801a81da': actor_01})
        actor_01['startScript'] = [
                script.actorHide(actorId='♔REFERENCE_TO_ACTORS_<$self$>♔'),
                script.end()
            ]
        actor_02 = generator.makeActor(None, 12, 1, 'static', animate=True, moveSpeed=1, animSpeed=4, direction='down', script=[], sprite_id=findSpriteByName('fire')['id'], name='actor_ca6236bf-719b-4eb6-92e1-bd8a17970037')
        actor_name_table.update({'actor_ca6236bf-719b-4eb6-92e1-bd8a17970037': actor_02})
        actor_02['startScript'] = [
                script.actorHide(actorId='♔REFERENCE_TO_ACTORS_<ca6236bf-719b-4eb6-92e1-bd8a17970037>♔'),
                script.end()
            ]
        actor_03 = generator.makeActor(None, 10, 3, 'static', animate=True, moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('fire')['id'], name='actor_68ea3dab-54be-4dbd-b53a-2aa65c1e319a')
        actor_name_table.update({'actor_68ea3dab-54be-4dbd-b53a-2aa65c1e319a': actor_03})
        actor_03['startScript'] = [
                script.actorHide(actorId='♔REFERENCE_TO_ACTORS_<$self$>♔'),
                script.end()
            ]
        actor_04 = generator.makeActor(None, 10, 7, 'static', animate=True, moveSpeed=1, animSpeed=2, direction='down', script=[], sprite_id=findSpriteByName('fire')['id'], name='actor_564a5805-f1f6-4b04-96af-53a776e83a15')
        actor_name_table.update({'actor_564a5805-f1f6-4b04-96af-53a776e83a15': actor_04})
        actor_04['startScript'] = [
                script.actorHide(actorId='♔REFERENCE_TO_ACTORS_<$self$>♔'),
                script.end()
            ]
        actor_04['script'] = [
                script.end()
            ]
        actor_05 = generator.makeActor(None, 8, 3, 'static', animate=True, moveSpeed=1, animSpeed=4, direction='down', script=[], sprite_id=findSpriteByName('fire')['id'], name='actor_0a5d6619-a223-418e-953d-2faac5c7f9ab')
        actor_name_table.update({'actor_0a5d6619-a223-418e-953d-2faac5c7f9ab': actor_05})
        actor_05['startScript'] = [
                script.actorHide(actorId='♔REFERENCE_TO_ACTORS_<$self$>♔'),
                script.end()
            ]
        actor_06 = generator.makeActor(None, 8, 7, 'static', animate=True, moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('fire')['id'], name='actor_45ade20b-b5af-4263-a8e7-1bd4c7f65ff7')
        actor_name_table.update({'actor_45ade20b-b5af-4263-a8e7-1bd4c7f65ff7': actor_06})
        actor_06['startScript'] = [
                script.actorHide(actorId='♔REFERENCE_TO_ACTORS_<$self$>♔'),
                script.end()
            ]
        actor_07 = generator.makeActor(None, 16, 3, 'static', moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('torch')['id'], name='actor_f2f4ce65-c898-4810-b31c-a6a766b321f9')
        actor_name_table.update({'actor_f2f4ce65-c898-4810-b31c-a6a766b321f9': actor_07})
        actor_07['startScript'] = [
                script.setFalse(variable='13'),
                script.setFalse(variable='L0'),
                script.end()
            ]
        actor_07['script'] = [
                script.ifFalse(variable='13', children = {
                    'true': [script.actorShow(actorId='♔REFERENCE_TO_ACTORS_<8462f086-7b40-4e93-a9a2-5e7e198b6774>♔'), script.setTrue(variable='13'), script.end()],
                    'false': [script.actorHide(actorId='♔REFERENCE_TO_ACTORS_<8462f086-7b40-4e93-a9a2-5e7e198b6774>♔'), script.setFalse(variable='13'), script.ifFalse(variable='L0', children = {
                    'true': [script.wait(time=2.3), script.actorEmote(actorId='♔REFERENCE_TO_ACTORS_<player>♔', emoteId='5'), script.setTrue(variable='L0'), script.end()],
                    'false': [script.end()]
                }), script.end()]
                }),
                script.end()
            ]
        actor_list = [actor_00, actor_01, actor_02, actor_03, actor_04, actor_05, actor_06, actor_07]
        trigger_00 = generator.makeTrigger('trigger_00', 2, 0, 2, 1)
        trigger_01 = generator.makeTrigger('trigger_01', 19, 6, 1, 2)
        trigger_02 = generator.makeTrigger('trigger_02', 14, 17, 2, 1)
        trigger_list = []
        collision_data_list = [243, 255, 63, 255, 255, 243, 15, 60, 255, 192, 3, 0, 60, 0, 192, 255, 15, 240, 255, 0, 63, 0, 252, 3, 192, 3, 255, 63, 240, 255, 3, 0, 63, 0, 240, 3, 63, 63, 240, 243, 255, 63, 255, 255, 243]
        gen_scene_bkg = generator.makeBackground("room6.png")
        scene_script = [
        script.setValue(variable='14', value='0'), script.setTimerScript(duration=0.3, children = {
                    'script': [script.ifTrue(variable='13', children = {
                    'true': [script.incValue(variable='14'), script.switch(variable='14', choices=7, value0=1, value1=2, value2=3, value3=4, value4=5, value5=6, value6=7, value7=8, value8=9, value9=10, value10=11, value11=12, value12=13, value13=14, value14=15, value15=16, children = {
                    'true0': [script.actorShow(actorId='♔REFERENCE_TO_ACTORS_<8462f086-7b40-4e93-a9a2-5e7e198b6774>♔'), script.wait(time=1), script.end()],
                    'true1': [script.actorShow(actorId='♔REFERENCE_TO_ACTORS_<81223844-bafc-4aae-bd14-9239801a81da>♔'), script.actorEmote(actorId='♔REFERENCE_TO_ACTORS_<player>♔', emoteId='0'), script.end()],
                    'true2': [script.actorShow(actorId='♔REFERENCE_TO_ACTORS_<ca6236bf-719b-4eb6-92e1-bd8a17970037>♔'), script.end()],
                    'true3': [script.actorShow(actorId='♔REFERENCE_TO_ACTORS_<68ea3dab-54be-4dbd-b53a-2aa65c1e319a>♔'), script.end()],
                    'true4': [script.actorShow(actorId='♔REFERENCE_TO_ACTORS_<564a5805-f1f6-4b04-96af-53a776e83a15>♔'), script.end()],
                    'true5': [script.actorShow(actorId='♔REFERENCE_TO_ACTORS_<0a5d6619-a223-418e-953d-2faac5c7f9ab>♔'), script.end()],
                    'true6': [script.actorShow(actorId='♔REFERENCE_TO_ACTORS_<45ade20b-b5af-4263-a8e7-1bd4c7f65ff7>♔'), script.end()],
                    'true7': [script.end()],
                    'true8': [script.end()],
                    'true9': [script.end()],
                    'true10': [script.end()],
                    'true11': [script.end()],
                    'true12': [script.end()],
                    'true13': [script.end()],
                    'true14': [script.end()],
                    'true15': [script.end()],
                    'false': [script.end()]
                }), script.end()],
                    'false': [script.end()]
                }), script.end()]
                }), script.end()
        ]

        gen_scene_scn = generator.makeScene("_gen_Scene_6", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Scene_6_00006")
        gen_scene_scn['script'] = scene_script
        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (2, 1), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (2, 0), 'entrance_size': (2, 1)  }, 'tags': ['A'] }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (17, 7), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 6), 'entrance_size': (1, 2)  }, 'tags': ['A'] }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (14, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (14, 17), 'entrance_size': (2, 1)  }, 'tags': ['A'] }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Scene_7_00007(callback):
        actor_name_table = {}
        actor_00 = generator.makeActor(None, 8, 7, 'randomFace', moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('npc002')['id'], name='actor_3c589b65-9bae-4da9-8959-fdcc1d750659')
        actor_name_table.update({'actor_3c589b65-9bae-4da9-8959-fdcc1d750659': actor_00})
        actor_00['startScript'] = [
                script.setTimerScript(duration=0.25, children = {
                    'script': [script.ifActorDirection(actorId='♔REFERENCE_TO_ACTORS_<$self$>♔', direction='up', children = {
                    'true': [script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<$self$>♔', direction='right'), script.end()],
                    'false': [script.end()]
                }), script.ifActorDirection(actorId='♔REFERENCE_TO_ACTORS_<$self$>♔', direction='left', children = {
                    'true': [script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<$self$>♔', direction='down'), script.end()],
                    'false': [script.end()]
                }), script.end()]
                }),
                script.end()
            ]
        actor_00['script'] = [
                script.end()
            ]
        actor_01 = generator.makeActor(None, 8, 11, 'randomFace', moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('npc002')['id'], name='actor_86174fcb-4e06-4c87-9ac6-49b0fb8da804')
        actor_name_table.update({'actor_86174fcb-4e06-4c87-9ac6-49b0fb8da804': actor_01})
        actor_01['startScript'] = [
                script.setTimerScript(duration=0.25, children = {
                    'script': [script.ifActorDirection(actorId='♔REFERENCE_TO_ACTORS_<$self$>♔', direction='down', children = {
                    'true': [script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<$self$>♔', direction='right'), script.end()],
                    'false': [script.end()]
                }), script.ifActorDirection(actorId='♔REFERENCE_TO_ACTORS_<$self$>♔', direction='left', children = {
                    'true': [script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<$self$>♔', direction='up'), script.end()],
                    'false': [script.end()]
                }), script.end()]
                }),
                script.end()
            ]
        actor_01['script'] = [
                script.end()
            ]
        actor_02 = generator.makeActor(None, 14, 11, 'randomFace', moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('npc002')['id'], name='actor_06c83bf1-77c9-436b-9dbd-3293f0275864')
        actor_name_table.update({'actor_06c83bf1-77c9-436b-9dbd-3293f0275864': actor_02})
        actor_02['startScript'] = [
                script.setTimerScript(duration=0.25, children = {
                    'script': [script.ifActorDirection(actorId='♔REFERENCE_TO_ACTORS_<$self$>♔', direction='down', children = {
                    'true': [script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<$self$>♔', direction='left'), script.end()],
                    'false': [script.end()]
                }), script.ifActorDirection(actorId='♔REFERENCE_TO_ACTORS_<$self$>♔', direction='right', children = {
                    'true': [script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<$self$>♔', direction='up'), script.end()],
                    'false': [script.end()]
                }), script.end()]
                }),
                script.end()
            ]
        actor_03 = generator.makeActor(None, 14, 7, 'randomFace', moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('npc002')['id'], name='actor_859b0137-ea19-42fb-a80c-bd85edb36a18')
        actor_name_table.update({'actor_859b0137-ea19-42fb-a80c-bd85edb36a18': actor_03})
        actor_03['startScript'] = [
                script.setTimerScript(duration=0.25, children = {
                    'script': [script.ifActorDirection(actorId='♔REFERENCE_TO_ACTORS_<$self$>♔', direction='right', children = {
                    'true': [script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<$self$>♔', direction='down'), script.end()],
                    'false': [script.end()]
                }), script.ifActorDirection(actorId='♔REFERENCE_TO_ACTORS_<$self$>♔', direction='up', children = {
                    'true': [script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<$self$>♔', direction='left'), script.end()],
                    'false': [script.end()]
                }), script.end()]
                }),
                script.end()
            ]
        actor_list = [actor_00, actor_01, actor_02, actor_03]
        trigger_00 = generator.makeTrigger('trigger_00', 0, 6, 1, 2)
        trigger_01 = generator.makeTrigger('trigger_01', 19, 8, 1, 2)
        trigger_02 = generator.makeTrigger('trigger_02', 16, 17, 2, 1)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 3, 240, 63, 0, 255, 243, 243, 63, 63, 255, 240, 0, 15, 15, 240, 255, 0, 240, 15, 0, 255, 0, 255, 15, 240, 255, 207, 255, 255, 252, 255, 15, 252, 255, 192, 255, 255, 252, 255, 207]
        gen_scene_bkg = generator.makeBackground("room7.png")
        scene_script = [
        script.setTimerScript(duration=0.25, children = {
                    'script': [script.ifActorDirection(actorId='♔REFERENCE_TO_ACTORS_<3c589b65-9bae-4da9-8959-fdcc1d750659>♔', direction='up', children = {
                    'true': [script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<3c589b65-9bae-4da9-8959-fdcc1d750659>♔', direction='right'), script.end()],
                    'false': [script.end()]
                }), script.ifActorDirection(actorId='♔REFERENCE_TO_ACTORS_<3c589b65-9bae-4da9-8959-fdcc1d750659>♔', direction='left', children = {
                    'true': [script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<3c589b65-9bae-4da9-8959-fdcc1d750659>♔', direction='down'), script.end()],
                    'false': [script.end()]
                }), script.ifActorDirection(actorId='♔REFERENCE_TO_ACTORS_<86174fcb-4e06-4c87-9ac6-49b0fb8da804>♔', direction='down', children = {
                    'true': [script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<86174fcb-4e06-4c87-9ac6-49b0fb8da804>♔', direction='right'), script.end()],
                    'false': [script.end()]
                }), script.ifActorDirection(actorId='♔REFERENCE_TO_ACTORS_<86174fcb-4e06-4c87-9ac6-49b0fb8da804>♔', direction='left', children = {
                    'true': [script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<86174fcb-4e06-4c87-9ac6-49b0fb8da804>♔', direction='up'), script.end()],
                    'false': [script.end()]
                }), script.ifActorDirection(actorId='♔REFERENCE_TO_ACTORS_<06c83bf1-77c9-436b-9dbd-3293f0275864>♔', direction='down', children = {
                    'true': [script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<06c83bf1-77c9-436b-9dbd-3293f0275864>♔', direction='left'), script.end()],
                    'false': [script.end()]
                }), script.ifActorDirection(actorId='♔REFERENCE_TO_ACTORS_<06c83bf1-77c9-436b-9dbd-3293f0275864>♔', direction='right', children = {
                    'true': [script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<06c83bf1-77c9-436b-9dbd-3293f0275864>♔', direction='up'), script.end()],
                    'false': [script.end()]
                }), script.ifActorDirection(actorId='♔REFERENCE_TO_ACTORS_<859b0137-ea19-42fb-a80c-bd85edb36a18>♔', direction='up', children = {
                    'true': [script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<859b0137-ea19-42fb-a80c-bd85edb36a18>♔', direction='left'), script.end()],
                    'false': [script.end()]
                }), script.ifActorDirection(actorId='♔REFERENCE_TO_ACTORS_<859b0137-ea19-42fb-a80c-bd85edb36a18>♔', direction='right', children = {
                    'true': [script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<859b0137-ea19-42fb-a80c-bd85edb36a18>♔', direction='down'), script.end()],
                    'false': [script.end()]
                }), script.end()]
                }), script.end()
        ]

        gen_scene_scn = generator.makeScene("_gen_Scene_7", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Scene_7_00007")
        gen_scene_scn['script'] = scene_script
        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (1, 7), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 6), 'entrance_size': (1, 2)  }, 'tags': ['A'] }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (17, 9), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 8), 'entrance_size': (1, 2)  }, 'tags': ['A'] }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (16, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (16, 17), 'entrance_size': (2, 1)  }, 'tags': ['A'] }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Scene_8_00008(callback):
        actor_name_table = {}
        actor_00 = generator.makeActor(None, 6, 5, 'static', moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('duck')['id'], name='actor_6559455e-b4ae-4f5f-8533-b340b1ce21af')
        actor_name_table.update({'actor_6559455e-b4ae-4f5f-8533-b340b1ce21af': actor_00})
        actor_list = [actor_00]
        trigger_00 = generator.makeTrigger('trigger_00', 2, 0, 2, 1)
        trigger_01 = generator.makeTrigger('trigger_01', 19, 2, 1, 2)
        trigger_02 = generator.makeTrigger('trigger_02', 8, 17, 2, 1)
        trigger_03 = generator.makeTrigger('trigger_03', 0, 12, 1, 2)
        trigger_04 = generator.makeTrigger('trigger_04', 16, 17, 2, 1)
        trigger_list = []
        collision_data_list = [243, 255, 63, 255, 255, 243, 63, 48, 255, 3, 51, 0, 63, 3, 240, 3, 0, 63, 0, 240, 255, 63, 255, 255, 243, 255, 0, 255, 15, 240, 192, 60, 12, 204, 195, 3, 60, 60, 192, 195, 255, 252, 252, 207, 207]
        gen_scene_bkg = generator.makeBackground("room8.png")

        gen_scene_scn = generator.makeScene("_gen_Scene_8", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Scene_8_00008")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (2, 1), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (2, 0), 'entrance_size': (2, 1)  }, 'tags': ['A'] }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (17, 3), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 2), 'entrance_size': (1, 2)  }, 'tags': ['A'] }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (8, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (8, 17), 'entrance_size': (2, 1)  }, 'tags': ['A'] }

        def addConnection_03(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_03 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_03['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_03
        connection_03 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_03, 'args': { 'exit_location': (1, 13), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (0, 12), 'entrance_size': (1, 2)  }, 'tags': ['A'] }

        def addConnection_04(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_04 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_04['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_04
        connection_04 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_04, 'args': { 'exit_location': (16, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (16, 17), 'entrance_size': (2, 1)  }, 'tags': ['A'] }

        gen_scene_connections = [connection_00, connection_01, connection_02, connection_03, connection_04]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Scene_9_00009(callback):
        actor_name_table = {}
        actor_00 = generator.makeActor(None, 7, 6, 'randomFace', moveSpeed=4, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('npc001')['id'], name='actor_9d993388-8e2f-451d-a5d3-5cedfab8f780')
        actor_name_table.update({'actor_9d993388-8e2f-451d-a5d3-5cedfab8f780': actor_00})
        actor_01 = generator.makeActor(None, 11, 6, 'randomFace', moveSpeed=4, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('npc002')['id'], name='actor_fddcf3d0-5a33-4fd2-8d93-a62b5ff05410')
        actor_name_table.update({'actor_fddcf3d0-5a33-4fd2-8d93-a62b5ff05410': actor_01})
        actor_list = [actor_00, actor_01]
        trigger_00 = generator.makeTrigger('trigger_00', 9, 0, 2, 1)
        trigger_01 = generator.makeTrigger('trigger_01', 6, 17, 2, 1)
        trigger_02 = generator.makeTrigger('trigger_02', 19, 1, 1, 2)
        trigger_list = []
        collision_data_list = [255, 249, 255, 159, 31, 255, 249, 241, 1, 152, 31, 128, 249, 1, 152, 1, 128, 25, 0, 152, 25, 128, 153, 127, 158, 9, 38, 152, 96, 130, 9, 38, 31, 32, 224, 1, 2, 254, 32, 224, 63, 3, 254, 243, 255]
        gen_scene_bkg = generator.makeBackground("room9.png")
        scene_script = [
        script.setTrue(variable='L0'), script.setTrue(variable='L1'), script.setTimerScript(duration=0.25, children = {
                    'script': [script.ifActorDirection(actorId='♔REFERENCE_TO_ACTORS_<9d993388-8e2f-451d-a5d3-5cedfab8f780>♔', direction='right', children = {
                    'true': [script.ifTrue(variable='L0', children = {
                    'true': [script.actorEmote(actorId='♔REFERENCE_TO_ACTORS_<9d993388-8e2f-451d-a5d3-5cedfab8f780>♔', emoteId=0), script.setFalse(variable='L0'), script.end()],
                    'false': [script.end()]
                }), script.ifActorDirection(actorId='♔REFERENCE_TO_ACTORS_<fddcf3d0-5a33-4fd2-8d93-a62b5ff05410>♔', direction='left', children = {
                    'true': [script.text(text=['The two rivals\nlock eyes with\neach other...', "And after just a\nmoment's\nhesitation...", 'They begin an\napocalpytic duel.'], avatarId=''), script.cameraShake(time=5), script.switchScene(sceneId='♔REFERENCE_TO_SCENES_<nothing>♔', x=9, y=8, direction='down', fadeSpeed='1'), script.end()],
                    'false': [script.end()]
                }), script.end()],
                    'false': [script.setTrue(variable='L0'), script.end()]
                }), script.ifActorDirection(actorId='♔REFERENCE_TO_ACTORS_<fddcf3d0-5a33-4fd2-8d93-a62b5ff05410>♔', direction='left', children = {
                    'true': [script.ifTrue(variable='L1', children = {
                    'true': [script.actorEmote(actorId='♔REFERENCE_TO_ACTORS_<fddcf3d0-5a33-4fd2-8d93-a62b5ff05410>♔', emoteId=0), script.setFalse(variable='L1'), script.end()],
                    'false': [script.end()]
                }), script.end()],
                    'false': [script.setTrue(variable='L1'), script.end()]
                }), script.end()]
                }), script.end()
        ]

        gen_scene_scn = generator.makeScene("_gen_Scene_9", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Scene_9_00009")
        gen_scene_scn['script'] = scene_script
        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (9, 1), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (9, 0), 'entrance_size': (2, 1)  }, 'tags': ['A'] }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (6, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (6, 17), 'entrance_size': (2, 1)  }, 'tags': ['A'] }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (17, 2), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 1), 'entrance_size': (1, 2)  }, 'tags': ['A'] }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Scene_10_00010(callback):
        actor_name_table = {}
        actor_00 = generator.makeActor(None, 9, 10, 'static', animate=True, moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('fire')['id'], name='actor_447f46ce-f3e4-4215-8ac1-3bf2518c2b96')
        actor_name_table.update({'actor_447f46ce-f3e4-4215-8ac1-3bf2518c2b96': actor_00})
        actor_list = [actor_00]
        trigger_00 = generator.makeTrigger('trigger_00', 17, 0, 2, 1)
        trigger_01 = generator.makeTrigger('trigger_01', 1, 17, 2, 1)
        trigger_list = []
        collision_data_list = [255, 255, 25, 248, 159, 129, 7, 25, 120, 144, 129, 7, 24, 120, 128, 129, 7, 31, 248, 252, 129, 207, 63, 255, 252, 243, 207, 63, 28, 128, 195, 1, 248, 28, 128, 1, 0, 24, 0, 128, 249, 1, 152, 255, 255]
        gen_scene_bkg = generator.makeBackground("room10.png")

        gen_scene_scn = generator.makeScene("_gen_Scene_10", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Scene_10_00010")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (17, 1), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (17, 0), 'entrance_size': (2, 1)  }, 'tags': ['A'] }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (1, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (1, 17), 'entrance_size': (2, 1)  }, 'tags': ['A'] }

        gen_scene_connections = [connection_00, connection_01]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_Scene_11_00011(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 1, 17, 2, 1)
        trigger_01 = generator.makeTrigger('trigger_01', 19, 4, 1, 2)
        trigger_02 = generator.makeTrigger('trigger_02', 19, 13, 1, 2)
        trigger_list = []
        collision_data_list = [255, 255, 63, 240, 255, 3, 0, 62, 0, 224, 3, 63, 240, 28, 2, 207, 225, 255, 28, 224, 7, 1, 126, 144, 231, 7, 9, 124, 144, 192, 7, 8, 28, 128, 0, 1, 15, 144, 255, 192, 249, 255, 159, 255, 255]
        gen_scene_bkg = generator.makeBackground("room11.png")

        gen_scene_scn = generator.makeScene("_gen_Scene_11", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Scene_11_00011")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (1, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (1, 17), 'entrance_size': (2, 1)  }, 'tags': ['A'] }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (17, 5), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 4), 'entrance_size': (1, 2)  }, 'tags': ['A'] }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (17, 14), 'exit_direction': 'left', 'entrance': gen_scene_scn['id'], 'entrance_location': (19, 13), 'entrance_size': (1, 2)  }, 'tags': ['A'] }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_nothing_00012(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 1, 0, 18, 1)
        trigger_00['script'] = [
                script.actorGetPosition(actorId='♔REFERENCE_TO_ACTORS_<player>♔', vectorX='L0', vectorY='L1'),
                script.setValue(variable='L2', value=16),
                script.fadeOut(speed='1'),
                script.actorSetPositionToValue(actorId='♔REFERENCE_TO_ACTORS_<player>♔', vectorX='L0', vectorY='L2'),
                script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<player>♔', direction='up'),
                script.fadeIn(speed='1'),
                script.end()
            ]
        trigger_01 = generator.makeTrigger('trigger_01', 1, 17, 18, 1)
        trigger_01['script'] = [
                script.actorGetPosition(actorId='♔REFERENCE_TO_ACTORS_<player>♔', vectorX='L0', vectorY='L1'),
                script.setValue(variable='L2', value=1),
                script.fadeOut(speed='1'),
                script.actorSetPositionToValue(actorId='♔REFERENCE_TO_ACTORS_<player>♔', vectorX='L0', vectorY='L2'),
                script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<player>♔', direction='down'),
                script.fadeIn(speed='1'),
                script.end()
            ]
        trigger_02 = generator.makeTrigger('trigger_02', 0, 1, 1, 16)
        trigger_02['script'] = [
                script.actorGetPosition(actorId='♔REFERENCE_TO_ACTORS_<player>♔', vectorX='L0', vectorY='L1'),
                script.setValue(variable='L2', value=18),
                script.fadeOut(speed='1'),
                script.actorSetPositionToValue(actorId='♔REFERENCE_TO_ACTORS_<player>♔', vectorX='L2', vectorY='L1'),
                script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<player>♔', direction='left'),
                script.fadeIn(speed='1'),
                script.end()
            ]
        trigger_03 = generator.makeTrigger('trigger_03', 19, 1, 1, 16)
        trigger_03['script'] = [
                script.actorGetPosition(actorId='♔REFERENCE_TO_ACTORS_<player>♔', vectorX='L0', vectorY='L1'),
                script.setValue(variable='L2', value=1),
                script.fadeOut(speed='1'),
                script.actorSetPositionToValue(actorId='♔REFERENCE_TO_ACTORS_<player>♔', vectorX='L2', vectorY='L1'),
                script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<player>♔', direction='right'),
                script.fadeIn(speed='1'),
                script.end()
            ]
        trigger_list = [trigger_00, trigger_01, trigger_02, trigger_03]
        collision_data_list = []
        gen_scene_bkg = generator.makeBackground("nothing.png")
        scene_script = [
        script.hideSprites(), script.text(text=['Nothing survives.', 'Fortunately...'], avatarId=''), script.showSprites(), script.text(text=['You are nothing.'], avatarId=''), script.end()
        ]

        gen_scene_scn = generator.makeScene("_gen_nothing", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_nothing_00012")
        gen_scene_scn['script'] = scene_script
        gen_scene_connections = []
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def scene_gen_nothing_00013(callback):
        actor_name_table = {}
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 1, 0, 18, 1)
        trigger_00['script'] = [
                script.actorGetPosition(actorId='♔REFERENCE_TO_ACTORS_<player>♔', vectorX='L0', vectorY='L1'),
                script.setValue(variable='L2', value=16),
                script.fadeOut(speed='1'),
                script.actorSetPositionToValue(actorId='♔REFERENCE_TO_ACTORS_<player>♔', vectorX='L0', vectorY='L2'),
                script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<player>♔', direction='up'),
                script.fadeIn(speed='1'),
                script.end()
            ]
        trigger_01 = generator.makeTrigger('trigger_01', 1, 17, 18, 1)
        trigger_01['script'] = [
                script.actorGetPosition(actorId='♔REFERENCE_TO_ACTORS_<player>♔', vectorX='L0', vectorY='L1'),
                script.setValue(variable='L2', value=1),
                script.fadeOut(speed='1'),
                script.actorSetPositionToValue(actorId='♔REFERENCE_TO_ACTORS_<player>♔', vectorX='L0', vectorY='L2'),
                script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<player>♔', direction='down'),
                script.fadeIn(speed='1'),
                script.end()
            ]
        trigger_02 = generator.makeTrigger('trigger_02', 0, 1, 1, 16)
        trigger_02['script'] = [
                script.actorGetPosition(actorId='♔REFERENCE_TO_ACTORS_<player>♔', vectorX='L0', vectorY='L1'),
                script.setValue(variable='L2', value=18),
                script.fadeOut(speed='1'),
                script.actorSetPositionToValue(actorId='♔REFERENCE_TO_ACTORS_<player>♔', vectorX='L2', vectorY='L1'),
                script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<player>♔', direction='left'),
                script.fadeIn(speed='1'),
                script.end()
            ]
        trigger_03 = generator.makeTrigger('trigger_03', 19, 1, 1, 16)
        trigger_03['script'] = [
                script.actorGetPosition(actorId='♔REFERENCE_TO_ACTORS_<player>♔', vectorX='L0', vectorY='L1'),
                script.setValue(variable='L2', value=1),
                script.fadeOut(speed='1'),
                script.actorSetPositionToValue(actorId='♔REFERENCE_TO_ACTORS_<player>♔', vectorX='L2', vectorY='L1'),
                script.actorSetDirection(actorId='♔REFERENCE_TO_ACTORS_<player>♔', direction='right'),
                script.fadeIn(speed='1'),
                script.end()
            ]
        trigger_list = [trigger_00, trigger_01, trigger_02, trigger_03]
        collision_data_list = []
        gen_scene_bkg = generator.makeBackground("nothing.png")
        scene_script = [
        script.end()
        ]

        gen_scene_scn = generator.makeScene("_gen_nothing", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_nothing_00013")
        gen_scene_scn['script'] = scene_script
        gen_scene_connections = []
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data


    def catalog(sample=True):
        """
        Returns a list of scene functions from this part of the library.
        """
        cat = [scene_gen_Room_1_00001,
            scene_gen_Scene_2_00002,
            scene_gen_Scene_3_00003,
            scene_gen_Scene_4_00004,
            scene_gen_Scene_5_00005,
            scene_gen_Scene_6_00006,
            scene_gen_Scene_7_00007,
            scene_gen_Scene_8_00008,
            scene_gen_Scene_9_00009,
            scene_gen_Scene_10_00010,
            scene_gen_Scene_11_00011]
        if sample:
            catalog_sample = random.sample(cat, 2)
        else:
            catalog_sample = cat
        catalog_sample += [scene_gen_nothing_00012,
        scene_gen_nothing_00013]

        return catalog_sample


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
    destination = "../gbprojects/generated_export_test/"
    runTest(destination)
