from rom_generator import generator
from rom_generator import script_functions as script

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
        generator.makeSpriteSheet('tower.png', name='tower', type='static', frames=1),
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

    def Sachita_Scene_Maze():
        actor2 = makeActor(findSpriteByName('duck'), 1, 30, "animated")
        actor3 = makeActor(findSpriteByName('doorway'), 29, 2)
        actor4 = makeActor(findSpriteByName('rock'), 15, 30)

        default_bkg = makeBackground("stars.png", "stars")

        amount = random.randint(1, 5)
        arr = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        increment = 0

        for i in range(1, 20):
            amount = random.randint(3, 5)
            xPos = random.randint(1, 30)
            yPos = random.randint(1, 30)
            increment = 0
            edgeBlock = 0
            while xPos == 31 or xPos == 30 or xPos == 29:
                if arr[0][xPos-1] == 1:
                    xPos = random.randint(3, 29)
                    edgeBlock = 1
                else:
                    edgeBlock = 1
                    break
            while yPos == 31 or yPos == 30 or yPos == 29:
                if arr[1][yPos-1] == 1:
                    yPos = random.randint(3, 29)
                    edgeBlock = 1
                else:
                    edgeBlock = 1
                    break
                    #avoiding out of bounds error
            if edgeBlock == 1:
                actor = makeActor(a_rock_sprite, xPos - increment, yPos - increment, "static")
                a_scene['actors'].append(actor)
                increment = increment + 2

        while arr[0][xPos-1] == 1 or arr[0][xPos + 1] == 1 or arr[0][ xPos - 3] == 1:
            xPos = random.randint(3, 29)
        while arr[1][yPos-1] == 1 or arr[1][yPos + 1] == 1 or arr[1][yPos - 3] == 1:
            yPos = random.randint(3, 29)

        if(0 <= xPos <= 15) and (0 <= yPos <= 15):
            choose = random.randint(1,2)
            if(choose == 1):
                for a in range (amount):
                    increment = increment + 2
                    actor = makeActor(a_rock_sprite, xPos, yPos + increment, "static")
                    a_scene['actors'].append(actor)
                    arr[0][ xPos-1] = 1
                    arr[1][ yPos-1 + increment] = 1
            if(choose == 2):
                for b in range (amount):
                    increment = increment + 2
                    actor = makeActor(a_rock_sprite, xPos + increment, yPos, "static")
                    a_scene['actors'].append(actor)
                    arr[0][xPos-1 + increment] = 1
                    arr[1][yPos-1] = 1

        if(0 <= xPos <= 15) and (15 <= yPos <= 28):
            choose = random.randint(1,2)
            if(choose == 1):
                for c in range (amount):
                    increment = increment + 2
                    actor = makeActor(a_rock_sprite, xPos + increment, yPos, "static")
                    a_scene['actors'].append(actor)
                    arr[0][xPos -1 + increment] = 1
                    arr[1][yPos-1] = 1
            if(choose == 2):
                for d in range (amount):
                    increment = increment + 2
                    actor = makeActor(a_rock_sprite, xPos, yPos - increment, "static")
                    a_scene['actors'].append(actor)
                    arr[0][xPos-1] = 1
                    arr[1][yPos-1 + increment] = 1

        if(15 <= xPos <= 28) and (15 <= yPos <= 28):
            choose = random.randint(1,2)
            if(choose == 1):
                for e in range (1, amount):
                    actor = makeActor(a_rock_sprite, xPos, yPos - increment, "static")
                    a_scene['actors'].append(actor)
                    arr[0][xPos-1] = 1
                    arr[1][yPos-1 - increment] = 1
            if(choose == 2):
                for f in range (1, amount):
                    increment = increment + 2
                    actor = makeActor(a_rock_sprite, xPos - increment, yPos, "static")
                    a_scene['actors'].append(actor)
                    arr[0][xPos-1 - increment] = 1
                    arr[1][yPos-1] = 1
                    increment = increment + 2

        if(15 <= xPos <= 28) and (0 <= yPos <= 15):
            choose = random.randint(1,2)
            if(choose == 1):
                for g in range (1, amount):
                    actor = makeActor(a_rock_sprite, xPos, yPos + increment, "static")
                    a_scene['actors'].append(actor)
                    arr[0][xPos-1] = 1
                    arr[1][yPos -1 - increment] = 1
                    increment = increment + 2
            if(choose == 2):
                for h in range (1, amount):
                    actor = makeActor(a_rock_sprite, xPos - increment, yPos, "static")
                    a_scene['actors'].append(actor)
                    arr[0][xPos -1 + increment] = 1
                    arr[1][yPos-1] = 1
                    increment = increment + 2


        actor_list = []
        trigger_list = []
        gen_scene_scn = generator.makeScene("_gen_Room_1", default_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Room_1_00001")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
                ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (9, 1), 'exit_direction': 'down', 'entrance': gen_scene_scn['id'], 'entrance_location': (9, 0), 'entrance_size': (2, 1)  } }

        def addConnection_01(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_01 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_01['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
                ]
            return trigger_01
        connection_01 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_01, 'args': { 'exit_location': (9, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (9, 17), 'entrance_size': (2, 1)  } }

        gen_scene_connections = [connection_00, connection_01]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data

    def catalog():
        """
        Returns a list of scene functions from this part of the library.
        """
        return [Sachita_Scene_Maze]

    return catalog, sprite_sheet_data
