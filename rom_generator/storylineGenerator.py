import argparse
import copy
import random
from rom_generator import script_functions as script
from rom_generator.generator import makeBasicProject, addSceneData, addSpriteSheet, makeSpriteSheet, makeBackground, makeScene, makeActor, addSymmetricSceneConnections, makeMusic, reverse_direction, initializeGenerator, writeProjectToDisk, makeTrigger

def fullProject():
    sprite_sheet_data = [
            makeSpriteSheet('actor.png', name='actor', type='actor', frames=3),
            makeSpriteSheet('cat.png', name='cat', type='static', frames=1),
            makeSpriteSheet('checkbox.png', name='checkbox', type='actor', frames=3),
            makeSpriteSheet('connector.png', name='connector', type='animated', frames=2),
            makeSpriteSheet('dog.png', name='dog', type='static', frames=1),
            makeSpriteSheet('duck.png', name='duck', type='animated', frames=2),
            makeSpriteSheet('GreenBlock.png', name='GreenBlock', type='static', frames=1),
            makeSpriteSheet('ice.png', name='ice', type='static', frames=1),
            makeSpriteSheet('key_00.png', name='key_00', type='static', frames=1),
            makeSpriteSheet('MazeBlock.png', name='MazeBlock', type='static', frames=1),
            makeSpriteSheet('npc001.png', name='npc001', type='actor', frames=3),
            makeSpriteSheet('npc002.png', name='npc002', type='actor', frames=3),
            makeSpriteSheet('npc003.png', name='npc003', type='actor_animated', frames=6),
            makeSpriteSheet('player.png', name='player', type='actor_animated', frames=6),
            makeSpriteSheet('radio.png', name='radio', type='static', frames=1),
            makeSpriteSheet('rock.png', name='rock', type='static', frames=1),
            makeSpriteSheet('sage.png', name='sage', type='static', frames=1),
            makeSpriteSheet('savepoint.png', name='savepoint', type='animated', frames=2),
            makeSpriteSheet('signpost.png', name='signpost', type='static', frames=1),
            makeSpriteSheet('static.png', name='static', type='static', frames=1),
            makeSpriteSheet('tower.png', name='tower', type='static', frames=1),
            makeSpriteSheet('torch.png', name='torch', type='static', frames=1),
            makeSpriteSheet('fire.png', name='fire', type='animated', frames=4),
            ]

    def findSpriteByName(sprite_name):
            '''
            Returns first sprite that matches the name given.
            '''
            try:
                result = [s for s in sprite_sheet_data if (s['name'] == sprite_name)][0]
                if None == result:
                    print(f"missing {sprite_name}")
                return result
            except:
                print(f"Missing {sprite_name}")
                return None

    def scene_gen_Cave_00002(callback):
        actor_00 = makeActor(None, 4, 6, 'faceInteraction', moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName("torch")["id"])
        actor_01 = makeActor(None, 4, 4, 'static', animate=True, moveSpeed=1, animSpeed=4, direction='down', script=[], sprite_id=findSpriteByName("fire")["id"])
        actor_02 = makeActor(None, 9, 7, 'static', direction='down', script=[], sprite_id=findSpriteByName("sage")["id"])
        actor_02['script'] = [
                script.text(text='In this game we are\' to learn about COVID\n'),
                script.text(text='Let us get\nstarted!'),
                script.text(text='Also, try going\nto the rock.'),
                script.setTrue(variable='7'),
                script.end()
            ]
        actor_03 = makeActor(None, 14, 6, 'faceInteraction', moveSpeed=1, animSpeed=3, direction='down', script=[], sprite_id=findSpriteByName("torch")["id"])
        actor_04 = makeActor(None, 14, 4, 'static', animate=True, moveSpeed=1, animSpeed=4, direction='down', script=[], sprite_id=findSpriteByName("fire")["id"])
        actor_05 = makeActor(None, 14, 11, 'static', animate=True, moveSpeed=1, animSpeed=2, direction='down', script=[], sprite_id=findSpriteByName("savepoint")["id"])
        actor_05['script'] = [
                script.text(text='Is losing your\'taste a symptom of\ngetting COVID?'),
                script.choice(variable='11', trueText='True', falseText='False'),
                script.ifTrue(variable='11', children = {
                    'true': [script.text(text='You got it right!'), script.text(text='Let us continue'), script.end()],
                    'false': [script.text(text='You got it wrong!'), script.text(text='It is a new symptom.')]
                }),
                script.end()
        ]
        actor_list = [actor_00, actor_01, actor_02, actor_03, actor_04, actor_05]
        trigger_00 = makeTrigger('trigger_00', 9, 17, 2, 1)
        trigger_list = []
        collision_data_list = [0, 0, 0, 0, 0, 0, 0, 224, 255, 127, 2, 0, 36, 0, 64, 2, 0, 36, 0, 64, 2, 0, 36, 0, 64, 2, 0, 36, 0, 64, 2, 0, 36, 0, 64, 2, 0, 36, 0, 64, 254, 249, 7, 144, 0]
        gen_scene_bkg = makeBackground("cave.png")
        gen_scene_scn = makeScene("_gen_Cave", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label=scene_gen_Cave_00002)
        gen_scene_connections = []
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "tags": []}
        return scene_data

    def scene_gen_Stars_00004(callback):
        actor_00 = makeActor(None, 15, 12, 'static', direction='down', script=[], sprite_id=findSpriteByName('dog')['id'])
        actor_00['script'] = [
                script.text(text='Does COVID make you dizzy?'),
                script.choice(variable='11', trueText='True', falseText='False'),
                script.ifTrue(variable='11', children = {
                'true': [script.text(text='You got it right!'), script.text(text='Let us continue'), script.end()],
                'false': [script.text(text='You got it wrong!'), script.text(text='It is a new symptom.')]
            }),
                script.end()
            ]
        actor_list = [actor_00]
        trigger_list = []
        collision_data_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        gen_scene_bkg = makeBackground("stars.png")
        gen_scene_scn = makeScene("_gen_Stars", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label=scene_gen_Stars_00004)
        gen_scene_connections = []
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "tags": []}
        return scene_data

    def createConnection(scene, x, y):
        global connections, sceneA, x2, y2
        #scene["triggers"].append(gen.makeTrigger(scene, 3, 3, 2, 1, []))
        sceneA = scene
        x2 = x
        y2 = y

    def storylineGenerator():
        """
        Create an empty world as an example to build future projects from.
        """
        # Set up a barebones project
        project = makeBasicProject()

        # Add a background image
        default_bkg = makeBackground("placeholder.png", "placeholder")
        project.backgrounds.append(default_bkg)

        player_sprite_sheet = addSpriteSheet(project, "actor_animated.png", "actor_animated", "actor_animated", frames=6)
        project.settings["playerSpriteSheetId"] = player_sprite_sheet["id"]


        #a_rock_sprite = addSpriteSheet(project, "rock.png", "rock", "static")
        #main_actor = makeActor(player_sprite_sheet, 10, 11, "static")
        #first_to_second = addSymmetricSceneConnections(project, first_scene, second_scene, "right", None)

        first_scene = scene_gen_Cave_00002(None)
        second_scene = scene_gen_Stars_00004(None)
        createConnection(first_scene,10, 12)

        # Create sprite sheet for the player sprite
        project.settings["playerSpriteSheetId"] = player_sprite_sheet["id"]

        # Get information about the background
        #bkg_x = default_bkg["imageWidth"]
        #bkg_y = default_bkg["imageHeight"]
        #bkg_width = default_bkg["width"]
        #bkg_height = default_bkg["height"]

        # add a sprite to indicate the location of a doorway
        # a better way to do this in the actual levels is to alter the background image instead
        #doorway_sprite = addSpriteSheet(project, "tower.png", "tower", "static")

        # Add scene to project
        for element_sprite in sprite_sheet_data:
            project.spriteSheets.append(element_sprite)

        scene_data_list = [first_scene, second_scene]

        for sdata in scene_data_list:
            # uncomment when you have generator.translateReferences: generator.addSceneData(project, generator.translateReferences(sdata, scene_data_list))
            addSceneData(project, sdata)
            project.backgrounds.append(sdata["background"])





        # Add some music
        project.music.append(makeMusic("template", "template.mod"))

        # Set the starting scene
        #project.settings["startSceneId"] = project.scenes[0]["id"]
        return project

    def getProject():
        return project
    return storylineGenerator

# Utilities
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

### Run the generator
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate a Game Boy ROM via a GB Studio project file.")
    parser.add_argument('--destination', '-d', type=str, help="destination folder name", default="../gbprojects/projects/storyline_01")
    args = parser.parse_args()
    initializeGenerator()
    gen_func = fullProject()
    project = gen_func()
    writeProjectToDisk(project, output_path = args.destination)
