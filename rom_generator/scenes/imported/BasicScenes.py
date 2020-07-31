# Generated Scene Functions
# BasicScenes.py

from rom_generator import generator
from rom_generator import script_functions as script

def scene_generation():
    sprite_sheet_data = [
        generator.makeSpriteSheet('actor.png', name='actor', type='actor', frames=3),
        generator.makeSpriteSheet('actor_animated.png', name='actor_animated', type='actor_animated', frames=6),
        generator.makeSpriteSheet('cat.png', name='cat', type='static', frames=1),
        generator.makeSpriteSheet('checkbox.png', name='checkbox', type='actor', frames=3),
        generator.makeSpriteSheet('connector.png', name='connector', type='animated', frames=2),
        generator.makeSpriteSheet('dog.png', name='dog', type='static', frames=1),
        generator.makeSpriteSheet('duck.png', name='duck', type='animated', frames=2),
        generator.makeSpriteSheet('fire.png', name='fire', type='animated', frames=4),
        generator.makeSpriteSheet('GreenBlock.png', name='GreenBlock', type='static', frames=1),
        generator.makeSpriteSheet('ice.png', name='ice', type='static', frames=1),
        generator.makeSpriteSheet('key_00.png', name='key_00', type='static', frames=1),
        generator.makeSpriteSheet('MazeBlock.png', name='MazeBlock', type='static', frames=1),
        generator.makeSpriteSheet('npc001.png', name='npc001', type='actor', frames=3),
        generator.makeSpriteSheet('npc002.png', name='npc002', type='actor', frames=3),
        generator.makeSpriteSheet('npc003.png', name='npc003', type='actor_animated', frames=6),
        generator.makeSpriteSheet('player.png', name='player', type='actor_animated', frames=6),
        generator.makeSpriteSheet('radio.png', name='radio', type='static', frames=1),
        generator.makeSpriteSheet('rock.png', name='rock', type='static', frames=1),
        generator.makeSpriteSheet('sage.png', name='sage', type='static', frames=1),
        generator.makeSpriteSheet('savepoint.png', name='savepoint', type='animated', frames=2),
        generator.makeSpriteSheet('signpost.png', name='signpost', type='static', frames=1),
        generator.makeSpriteSheet('static.png', name='static', type='static', frames=1),
        generator.makeSpriteSheet('torch.png', name='torch', type='static', frames=1),
        generator.makeSpriteSheet('tower.png', name='tower', type='static', frames=1)]
    
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
    
    def scene_gen_Outside_00001(callback):
        actor_00 = generator.makeActor(None, 25, 14, 'static', moveSpeed=0, direction='down', script=[], sprite_id=findSpriteByName('rock')['id'])
        actor_00['script'] = [
                script.actorPush(do_continue=False),
                script.end()
            ]
        actor_01 = generator.makeActor(None, 27, 23, 'static', direction='down', script=[], sprite_id=findSpriteByName('signpost')['id'])
        actor_01['script'] = [
                script.text(text='Welcome to\nGBStudio!'),
                script.end()
            ]
        actor_02 = generator.makeActor(None, 21, 18, 'static', animate=True, animSpeed=1, direction='down', script=[], sprite_id=findSpriteByName('duck')['id'])
        actor_03 = generator.makeActor(None, 3, 24, 'randomWalk', direction='down', script=[], sprite_id=findSpriteByName('npc003')['id'])
        actor_03['script'] = [
                script.text(text='Have you seen my\ncat anywhere?'),
                script.ifTrue(variable='0', children = {
                    'true': [script.text(text='He\'s by the house?\nThank you!'), script.setTrue(variable='4'), script.end()],
                    'false': [script.end()]
                }),
                script.end()
            ]
        actor_04 = generator.makeActor(None, 4, 6, 'static', direction='down', script=[], sprite_id=findSpriteByName('cat')['id'])
        actor_04['script'] = [
                script.text(text='Meow!'),
                script.setTrue(variable='0'),
                script.end()
            ]
        actor_05 = generator.makeActor(None, 21, 24, 'faceInteraction', direction='up', script=[], sprite_id=findSpriteByName('npc001')['id'])
        actor_05['script'] = [
                script.ifTrue(variable='1', children = {
                    'true': [script.text(text='I guess it was a\nmisunderstanding.'), script.setTrue(variable='8'), script.end()],
                    'false': [script.text(text='What is that guy\nlooking at?'), script.actorSetDirection(actorId='a85c4ba5-9bc0-4daa-94bc-4ef68a690659', direction='up'), script.end()]
                }),
                script.end()
            ]
        actor_06 = generator.makeActor(None, 21, 16, 'faceInteraction', direction='down', script=[], sprite_id=findSpriteByName('npc001')['id'])
        actor_06['script'] = [
                script.text(text='Check out this\nsweet duck!'),
                script.setTrue(variable='1'),
                script.actorSetDirection(actorId='5cf6eb6c-be62-4efc-9cbb-14a8efac21a8', direction='down'),
                script.end()
            ]
        actor_list = [actor_00, actor_01, actor_02, actor_03, actor_04, actor_05, actor_06]
        trigger_00 = generator.makeTrigger('trigger_00', 25, 13, 2, 2)
        trigger_01 = generator.makeTrigger('trigger_01', 24, 8, 2, 1)
        trigger_02 = generator.makeTrigger('trigger_02', 10, 8, 2, 1)
        trigger_list = []
        collision_data_list = [255, 255, 7, 0, 255, 255, 7, 0, 255, 255, 7, 0, 153, 153, 5, 0, 3, 63, 4, 0, 3, 63, 4, 0, 3, 63, 28, 0, 1, 63, 144, 7, 3, 51, 240, 252, 3, 0, 0, 192, 3, 0, 0, 192, 1, 0, 0, 128, 99, 0, 0, 192, 243, 0, 0, 192, 243, 0, 0, 192, 97, 0, 0, 128, 3, 0, 0, 192, 3, 128, 255, 207, 3, 248, 0, 216, 1, 14, 0, 144, 3, 2, 0, 208, 3, 30, 0, 208, 3, 112, 0, 220, 1, 192, 255, 135, 3, 0, 0, 192, 2, 0, 0, 192, 2, 0, 0, 192, 1, 0, 0, 128, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        gen_scene_bkg = generator.makeBackground("outside.png")
        gen_scene_scn = generator.makeScene("_gen_Outside", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label=scene_gen_Outside_00001)
        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (25, 15), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (25, 13), 'entrance_size': (2, 2)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (24, 9), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (24, 8), 'entrance_size': (2, 1)  } }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(x=destination_location[0], y=destination_location[1], direction=destination_direction, sceneId=destination_scene_id, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (10, 9), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (10, 8), 'entrance_size': (2, 1)  } }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "tags": []}
        return scene_data


    def scene_gen_Cave_00002(callback):
        actor_00 = generator.makeActor(None, 4, 6, 'faceInteraction', moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('torch')['id'])
        actor_01 = generator.makeActor(None, 4, 4, 'static', animate=True, moveSpeed=1, animSpeed=4, direction='down', script=[], sprite_id=findSpriteByName('fire')['id'])
        actor_02 = generator.makeActor(None, 9, 7, 'static', direction='down', script=[], sprite_id=findSpriteByName('sage')['id'])
        actor_02['script'] = [
                script.text(text='It\'s dangerous to\ngo without docs.'),
                script.text(text='Check out\ngbstudio.dev/docs'),
                script.text(text='Also, try moving\nthe rock outside.'),
                script.setTrue(variable='7'),
                script.end()
            ]
        actor_03 = generator.makeActor(None, 14, 6, 'faceInteraction', moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('torch')['id'])
        actor_04 = generator.makeActor(None, 14, 4, 'static', animate=True, moveSpeed=1, animSpeed=4, direction='down', script=[], sprite_id=findSpriteByName('fire')['id'])
        actor_05 = generator.makeActor(None, 14, 11, 'static', animate=True, moveSpeed=1, animSpeed=2, direction='down', script=[], sprite_id=findSpriteByName('savepoint')['id'])
        actor_05['script'] = [
                script.choice(variable='11', trueText='Save Game', falseText='Cancel'),
                script.ifTrue(variable='11', children = {
                    'true': [script.saveData(), script.text(text='Game progress has\nbeen saved.'), script.text(text='It is now safe to\nturn off your\nsystem.'), script.end()],
                    'false': [script.end()]
                }),
                script.end()
            ]
        actor_list = [actor_00, actor_01, actor_02, actor_03, actor_04, actor_05]
        trigger_00 = generator.makeTrigger('trigger_00', 9, 17, 2, 1)
        trigger_list = []
        collision_data_list = [0, 0, 0, 0, 0, 0, 0, 224, 255, 127, 2, 0, 36, 0, 64, 2, 0, 36, 0, 64, 2, 0, 36, 0, 64, 2, 0, 36, 0, 64, 2, 0, 36, 0, 64, 2, 0, 36, 0, 64, 254, 249, 7, 144, 0]
        gen_scene_bkg = generator.makeBackground("cave.png")
        gen_scene_scn = generator.makeScene("_gen_Cave", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label=scene_gen_Cave_00002)
        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(x=destination_location[0], y=destination_location[1], direction=destination_direction, sceneId=destination_scene_id, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (9, 15), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (9, 17), 'entrance_size': (2, 1)  } }

        gen_scene_connections = [connection_00]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "tags": []}
        return scene_data


    def scene_gen_House_00003(callback):
        actor_00 = generator.makeActor(None, 12, 5, 'faceInteraction', direction='down', script=[], sprite_id=findSpriteByName('npc002')['id'])
        actor_00['script'] = [
                script.ifFalse(variable='2', children = {
                    'true': [script.text(text='Have you tried\nusing this radio?'), script.end()],
                    'false': [script.text(text='Yeah it doesn\'t\nfit does it?'), script.actorEmote(actorId='566c8812-a204-45b5-b93a-c113c10c20de', emoteId='3'), script.text(text='But it\'s all I\nhave right now...'), script.setTrue(variable='6'), script.end()]
                }),
                script.end()
            ]
        actor_01 = generator.makeActor(None, 15, 5, 'static', direction='down', script=[], sprite_id=findSpriteByName('radio')['id'])
        actor_01['script'] = [
                script.ifFalse(variable='2', children = {
                    'true': [script.musicPlay(musicId='f50428ab-a084-4591-9bba-2ba10fe7b1c6', loop=True), script.setTrue(variable='2'), script.end()],
                    'false': [script.musicStop(), script.setFalse(variable='2'), script.end()]
                }),
                script.end()
            ]
        actor_02 = generator.makeActor(None, 15, 11, 'static', direction='down', script=[], sprite_id=findSpriteByName('signpost')['id'])
        actor_02['script'] = [
                script.text(text='Add sprites to\nassets/sprites'),
                script.end()
            ]
        actor_03 = generator.makeActor(None, 3, 11, 'static', direction='down', script=[], sprite_id=findSpriteByName('signpost')['id'])
        actor_03['script'] = [
                script.text(text='Add backgrounds to\nassets/backgrounds'),
                script.end()
            ]
        actor_04 = generator.makeActor(None, 3, 5, 'static', direction='down', script=[], sprite_id=findSpriteByName('signpost')['id'])
        actor_04['script'] = [
                script.text(text='This room is\npretty empty.'),
                script.text(text='Try to edit\nhouse.png'),
                script.end()
            ]
        actor_list = [actor_00, actor_01, actor_02, actor_03, actor_04]
        trigger_00 = generator.makeTrigger('trigger_00', 9, 16, 2, 1)
        trigger_list = []
        collision_data_list = [0, 0, 0, 0, 0, 0, 0, 224, 255, 127, 2, 0, 36, 0, 64, 2, 0, 36, 0, 64, 2, 0, 36, 0, 64, 2, 0, 36, 0, 64, 2, 0, 36, 0, 64, 2, 0, 228, 159, 127, 0, 9, 0, 240, 0]
        gen_scene_bkg = generator.makeBackground("house.png")
        gen_scene_scn = generator.makeScene("_gen_House", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label=scene_gen_House_00003)
        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (9, 14), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (9, 16), 'entrance_size': (2, 1)  } }

        gen_scene_connections = [connection_00]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "tags": []}
        return scene_data


    def scene_gen_Stars_00004(callback):
        actor_00 = generator.makeActor(None, 15, 12, 'static', direction='down', script=[], sprite_id=findSpriteByName('dog')['id'])
        actor_00['script'] = [
                script.text(text='How did you\nget here!?!?'),
                script.incValue(variable='3'),
                script.ifValue(variable='3', operator='==', comparator=1, children = {
                    'true': [script.text(text='You have spoken to\nme $03$ time.'), script.end()],
                    'false': [script.text(text='You have spoken to\nme $03$ times.'), script.end()]
                }),
                script.setTrue(variable='9'),
                script.end()
            ]
        actor_list = [actor_00]
        trigger_list = []
        collision_data_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        gen_scene_bkg = generator.makeBackground("stars.png")
        gen_scene_scn = generator.makeScene("_gen_Stars", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label=scene_gen_Stars_00004)
        gen_scene_connections = []
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "tags": []}
        return scene_data


    def scene_gen_Logo_00005(callback):
        actor_list = []
        trigger_list = []
        collision_data_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        gen_scene_bkg = generator.makeBackground("logo.png")
        gen_scene_scn = generator.makeScene("_gen_Logo", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label=scene_gen_Logo_00005)
        gen_scene_connections = []
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "tags": []}
        return scene_data


    def scene_gen_Title_Screen_00006(callback):
        actor_list = []
        trigger_list = []
        collision_data_list = []
        gen_scene_bkg = generator.makeBackground("titlescreen.png")
        gen_scene_scn = generator.makeScene("_gen_Title_Screen", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label=scene_gen_Title_Screen_00006)
        gen_scene_connections = []
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "tags": []}
        return scene_data


    def scene_gen_Underground_00007(callback):
        actor_00 = generator.makeActor(None, 7, 25, 'static', direction='down', script=[], sprite_id=findSpriteByName('signpost')['id'])
        actor_00['script'] = [
                script.text(text='Try to get the ice\nblock to the mark.'),
                script.text(text='If you get stuck,\nI\'ll reset it!'),
                script.actorSetPosition(actorId='27de6d44-f7c0-48df-a952-2c87471bbfd4', x=24, y=18),
                script.end()
            ]
        actor_01 = generator.makeActor(None, 24, 18, 'static', moveSpeed=2, direction='down', script=[], sprite_id=findSpriteByName('ice')['id'])
        actor_01['script'] = [
                script.ifActorAtPosition(actorId='27de6d44-f7c0-48df-a952-2c87471bbfd4', x=15, y=10, children = {
                    'true': [script.end()],
                    'false': [script.actorPush(do_continue=True), script.ifActorAtPosition(actorId='27de6d44-f7c0-48df-a952-2c87471bbfd4', x=15, y=10, children = {
                    'true': [script.text(text='Success!'), script.setTrue(variable='5'), script.end()],
                    'false': [script.end()]
                }), script.end()]
                }),
                script.setTrue(variable='12'),
                script.end()
            ]
        actor_02 = generator.makeActor(None, 23, 27, 'static', moveSpeed=0, direction='down', script=[], sprite_id=findSpriteByName('rock')['id'])
        actor_02['script'] = [
                script.actorPush(do_continue=False),
                script.end()
            ]
        actor_03 = generator.makeActor(None, 21, 27, 'static', moveSpeed=0, direction='down', script=[], sprite_id=findSpriteByName('rock')['id'])
        actor_03['script'] = [
                script.actorPush(do_continue=False),
                script.end()
            ]
        actor_04 = generator.makeActor(None, 19, 27, 'static', moveSpeed=0, direction='down', script=[], sprite_id=findSpriteByName('rock')['id'])
        actor_04['script'] = [
                script.actorPush(do_continue=False),
                script.end()
            ]
        actor_list = [actor_00, actor_01, actor_02, actor_03, actor_04]
        trigger_00 = generator.makeTrigger('trigger_00', 21, 30, 2, 2)
        trigger_list = []
        collision_data_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 248, 255, 255, 31, 248, 255, 255, 31, 8, 128, 1, 19, 200, 128, 1, 19, 200, 0, 0, 16, 200, 0, 0, 16, 8, 0, 0, 16, 8, 0, 0, 16, 8, 0, 6, 16, 8, 0, 6, 16, 8, 3, 6, 16, 8, 3, 0, 16, 248, 255, 255, 28, 254, 255, 255, 124, 254, 255, 255, 124, 2, 0, 0, 64, 2, 0, 158, 71, 2, 128, 159, 71, 2, 128, 159, 71, 2, 128, 7, 118, 2, 128, 7, 118, 2, 128, 7, 118, 2, 0, 6, 118, 2, 0, 6, 118, 254, 255, 159, 127, 0, 0, 144, 0]
        gen_scene_bkg = generator.makeBackground("underground.png")
        gen_scene_scn = generator.makeScene("_gen_Underground", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label=scene_gen_Underground_00007)
        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (21, 29), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (21, 30), 'entrance_size': (2, 2)  } }

        gen_scene_connections = [connection_00]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "tags": []}
        return scene_data


    def scene_gen_Menu_00008(callback):
        actor_00 = generator.makeActor(None, 2, 4, 'faceInteraction', moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('checkbox')['id'])
        actor_00['script'] = [
                script.end()
            ]
        actor_01 = generator.makeActor(None, 2, 6, 'faceInteraction', moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('checkbox')['id'])
        actor_01['script'] = [
                script.end()
            ]
        actor_02 = generator.makeActor(None, 2, 8, 'faceInteraction', moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('checkbox')['id'])
        actor_02['script'] = [
                script.end()
            ]
        actor_03 = generator.makeActor(None, 2, 11, 'faceInteraction', moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('checkbox')['id'])
        actor_03['script'] = [
                script.end()
            ]
        actor_04 = generator.makeActor(None, 2, 13, 'faceInteraction', moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('checkbox')['id'])
        actor_04['script'] = [
                script.end()
            ]
        actor_05 = generator.makeActor(None, 2, 15, 'faceInteraction', moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('checkbox')['id'])
        actor_05['script'] = [
                script.end()
            ]
        actor_list = [actor_00, actor_01, actor_02, actor_03, actor_04, actor_05]
        trigger_list = []
        collision_data_list = []
        gen_scene_bkg = generator.makeBackground("menu.png")
        gen_scene_scn = generator.makeScene("_gen_Menu", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label=scene_gen_Menu_00008)
        gen_scene_connections = []
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "tags": []}
        return scene_data


    def scene_gen_example_hall_02_00009(callback):
        actor_00 = generator.makeActor(None, 20, 13, 'static', moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('rock')['id'])
        actor_00['script'] = [
                script.text(text=["You push the rock\nbut it doesn't\nbudge."], avatarId=''),
                script.end()
            ]
        actor_01 = generator.makeActor(None, 6, 11, 'static', moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName('key_00')['id'])
        actor_01['startScript'] = [
                script.ifTrue(variable='25', children = {
                    'true': [script.actorHide(actorId='$self$'), script.end()],
                    'false': [script.end()]
                }),
                script.end()
            ]
        actor_01['script'] = [
                script.actorHide(actorId='$self$'),
                script.setTrue(variable='25'),
                script.text(text=['You got the key!'], avatarId=''),
                script.end()
            ]
        actor_list = [actor_00, actor_01]
        trigger_00 = generator.makeTrigger('trigger_00', 15, 27, 2, 1)
        trigger_01 = generator.makeTrigger('trigger_01', 8, 5, 2, 1)
        trigger_02 = generator.makeTrigger('trigger_02', 1, 10, 1, 2)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 207, 255, 255, 255, 240, 255, 255, 15, 255, 252, 3, 240, 207, 63, 0, 255, 252, 1, 240, 207, 31, 0, 255, 252, 3, 240, 207, 63, 0, 255, 252, 3, 240, 207, 255, 63, 255, 252, 255, 243, 207, 255, 63, 255, 252, 255, 243, 207, 255, 63, 255, 252, 63, 240, 207, 255, 3, 255, 252, 63, 0, 0, 252, 63, 0, 192, 255, 3, 0, 252, 255, 195, 255, 255, 63, 252, 255, 255, 231, 255]
        gen_scene_bkg = generator.makeBackground("halls_02.png")
        gen_scene_scn = generator.makeScene("_gen_example_hall_02", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label=scene_gen_example_hall_02_00009)
        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (15, 26), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (15, 27), 'entrance_size': (2, 1)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (8, 6), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (8, 5), 'entrance_size': (2, 1)  } }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (2, 11), 'exit_direction': 'right', 'entrance': gen_scene_scn['id'], 'entrance_location': (1, 10), 'entrance_size': (1, 2)  } }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "tags": []}
        return scene_data


    def scene_gen_example_hall_03_00010(callback):
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 11, 24, 2, 1)
        trigger_01 = generator.makeTrigger('trigger_01', 20, 19, 2, 1)
        trigger_02 = generator.makeTrigger('trigger_02', 14, 7, 2, 1)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 243, 255, 255, 63, 255, 255, 255, 243, 255, 255, 63, 255, 255, 255, 243, 255, 255, 63, 255, 255, 255, 243, 255, 255, 63, 252, 255, 255, 195, 255, 255, 63, 252, 255, 255, 195, 255, 255, 63, 252, 255, 255, 195, 252, 63, 0, 0, 255, 3, 0, 240, 63, 0, 0, 255, 127, 254, 255, 255, 231, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
        gen_scene_bkg = generator.makeBackground("halls_03.png")
        gen_scene_scn = generator.makeScene("_gen_example_hall_03", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label=scene_gen_example_hall_03_00010)
        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (11, 23), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (11, 24), 'entrance_size': (2, 1)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (20, 20), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (20, 19), 'entrance_size': (2, 1)  } }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.ifTrue(variable='25', children = {
                            'true': [script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'), script.end()],
                            'false': [script.text(text=['The door is\nlocked.'], avatarId=''), script.end()]
                        }),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (14, 8), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (14, 7), 'entrance_size': (2, 1)  } }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "tags": []}
        return scene_data


    def scene_gen_example_hall_04_00011(callback):
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 18, 15, 2, 1)
        trigger_01 = generator.makeTrigger('trigger_01', 13, 26, 2, 1)
        trigger_02 = generator.makeTrigger('trigger_02', 4, 11, 2, 1)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 252, 255, 255, 207, 255, 255, 255, 252, 255, 255, 207, 255, 255, 255, 252, 63, 255, 207, 255, 192, 255, 252, 15, 252, 207, 255, 192, 255, 252, 207, 255, 15, 0, 252, 255, 0, 192, 255, 15, 0, 252, 255, 0, 192, 255, 15, 0, 252, 255, 255, 249, 255, 255, 159, 255, 255, 255, 255, 255]
        gen_scene_bkg = generator.makeBackground("halls_04.png")
        gen_scene_scn = generator.makeScene("_gen_example_hall_04", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label=scene_gen_example_hall_04_00011)
        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (18, 16), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (18, 15), 'entrance_size': (2, 1)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (13, 25), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (13, 26), 'entrance_size': (2, 1)  } }

        def addConnection_02(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_02 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_02['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_02
        connection_02 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_02, 'args': { 'exit_location': (4, 12), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (4, 11), 'entrance_size': (2, 1)  } }

        gen_scene_connections = [connection_00, connection_01, connection_02]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "tags": []}
        return scene_data


    def scene_gen_Scene_12_00012(callback):
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 9, 17, 2, 1)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 63, 0, 192, 3, 0, 60, 0, 192, 3, 0, 60, 0, 192, 3, 0, 60, 0, 192, 3, 0, 60, 0, 192, 3, 0, 60, 0, 192, 255, 249, 255, 159, 255]
        gen_scene_bkg = generator.makeBackground("cave.png")
        gen_scene_scn = generator.makeScene("_gen_Scene_12", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label=scene_gen_Scene_12_00012)
        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (9, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (9, 17), 'entrance_size': (2, 1)  } }

        gen_scene_connections = [connection_00]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "tags": []}
        return scene_data


    def catalog():
        """
        Returns a list of scene functions from this part of the library.
        """
        return [scene_gen_Outside_00001,
            scene_gen_Cave_00002,
            scene_gen_House_00003,
            scene_gen_Stars_00004,
            scene_gen_Logo_00005,
            scene_gen_Title_Screen_00006,
            scene_gen_Underground_00007,
            scene_gen_Menu_00008,
            scene_gen_example_hall_02_00009,
            scene_gen_example_hall_03_00010,
            scene_gen_example_hall_04_00011,
            scene_gen_Scene_12_00012]

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
        generator.addSceneData(project, sdata)

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

