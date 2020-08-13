import tracery
import json
import uuid
import os
import random
import datetime
from pathlib import Path
from tracery.modifiers import base_english
from rom_generator import generator
from rom_generator import script_functions as script
import logging
import PIL
from PIL import Image, ImageFont, ImageDraw
from rom_generator.utilities import bcolors

# Inspired by https://stackoverflow.com/questions/12770218/using-pil-or-a-numpy-array-how-can-i-remove-entire-rows-from-an-image
def FindImageRowByColor(pixel_array, width, height, color):
    rows_found = []
    for y in range(height):
        for x in range(width):
            #print('\t\t', pixel_array[x, y], '\t', color)
            if pixel_array[x, y] != color:
                break
        else:
            rows_found.append(y)
    logging.info(f"rows found: {bcolors.OKGREEN}{rows_found}{bcolors.ENDC}")
    return rows_found

def removeBlankRows(image, gap_spacing = 3):
    pixels = image.load()
    img_width, img_height = image.size[0], image.size[1]
    blank_rows = FindImageRowByColor(pixels, img_width, img_height, (0,0,0))
    scratch_image = Image.new("RGB", (img_width, img_height), (0,0,0))
    new_pixels = scratch_image.load()
    rows_removed = 0
    blank_gap = 0
    for y in range(img_height):
        blank_gap += 1
        if (y in blank_rows) and (blank_gap >= gap_spacing):
            rows_removed += 1
        else:
            if (y not in blank_rows):
                blank_gap = 0
            for x in range(img_width):
                new_pixels[x, y - rows_removed] = pixels[x, y]

    vert_offset = int(rows_removed // 2)
    logging.info(f"{rows_removed} scanlines removed from title.")
    new_image = Image.new("RGB", (img_width, img_height), (0,0,0))
    new_image.paste(scratch_image, (0, vert_offset))
    return new_image


def generateTitleBackground(proj_title="Generated Game", no_split=False, squash=False):
    """
    Generates an image for the title screen. Returns the filename of the new image.
    """
    translation_table = {
    ":": "\n:\n",
    " for the ": "\nfor the\n",
    " of the ": "\nof the\n",
    " of a ": "\nof a\n",
    " of an ": "\nof an\n",
    " & ": "\n&\n",
    "'s ": "'s\n",
    " et ": " & ",
    "Super ": "Super\n",
    " of ": "\n of "
    }

    print(proj_title)
    if None==proj_title:
        logging.error("Invalid title")

    for sign, rep in translation_table.items():
        proj_title = proj_title.replace(sign, rep)
    title_list = proj_title.split("\n")
    split_title = proj_title.split("\n:\n")
    proj_title.replace("\n:\n", "\n")
    if len(title_list) == 1:
        proj_title = proj_title.replace(" ", "\n")
        title_list = proj_title.split("\n")
    if not no_split:
        if len(split_title) == 1:
            split_title = proj_title.split("\n")

    img_width = 160
    img_height = 144
    img = PIL.Image.new("RGB", (img_width, img_height), "black")
    d = ImageDraw.Draw(img)

    def pickFont():
        font_list = [
            'assets/fonts/goudy_bookletter_1911-webfont.ttf',
            'assets/fonts/goudy_bookletter_1911-webfont.ttf',
            'assets/fonts/goudy_bookletter_1911-webfont.ttf',
            'assets\\fonts\\LeagueSpartan-Semibold.ttf',
            'assets\\fonts\\kjv-1611\\dist\\KJV1611.otf',
            'assets\\fonts\\gfs-theokritos\\GFS_THEOKRITOS_OT\\GFSTheokritos.otf',
            'assets\\fonts\\gfs-theokritos\\GFS_THEOKRITOS_OT\\GFSTheokritos.otf',
            'assets\\fonts\\gfs-theokritos\\GFS_THEOKRITOS_OT\\GFSTheokritos.otf',
            'assets/fonts/goudy_bookletter_1911-webfont.ttf',
            'assets/fonts/goudy_bookletter_1911-webfont.ttf',
            'assets/fonts/goudy_bookletter_1911-webfont.ttf',
            'assets\\fonts\\LeagueSpartan-Semibold.ttf',
            'assets\\fonts\\kjv-1611\\dist\\KJV1611.otf',
            'assets\\fonts\\gfs-theokritos\\GFS_THEOKRITOS_OT\\GFSTheokritos.otf',
            'assets\\fonts\\gfs-theokritos\\GFS_THEOKRITOS_OT\\GFSTheokritos.otf',
            'assets\\fonts\\gfs-theokritos\\GFS_THEOKRITOS_OT\\GFSTheokritos.otf',
            'assets\\fonts\\germania-one\\GermaniaOne-Regular.ttf',
            'assets\\fonts\\chomsky\\dist\\chomsky.otf',
            'assets\\fonts\\blankenburg-2-font\\Blankenburg-eJGx.ttf',
            'assets\\fonts\\avdira-textfonts\\Avdira_hint.ttf',
            'assets\\fonts\\qt_uncial\\QTUSA-Uncial.otf',
            'assets\\fonts\\parker_chronicle\\ParkerChronicle.otf',
            'assets\\fonts\\joscelyn\\Joscelyn.otf',
            'assets\\fonts\\sinistre\\Sinistre-S†Caroline.otf',
            'assets\\fonts\\amphora\\font\\otf\\Amphora-Regular.otf',
            'assets\\fonts\\juniusx\\fonts\\JuniusX-SemiCondensedSemibold.ttf',
            'assets\\fonts\\juniusx\\fonts\\JuniusX-CondensedBold.ttf',
            'assets\\fonts\\grenze_gotisch\\fonts\\otf\\GrenzeGotisch-ExtraBold.otf',
            'assets\\fonts\\grenze_gotisch\\fonts\\otf\\GrenzeGotisch-Black.otf',
            'assets\\fonts\\grenze_gotisch\\fonts\\otf\\GrenzeGotisch-SemiBold.otf',
            'assets\\fonts\\grenze_gotisch\\fonts\\otf\\GrenzeGotisch-Medium.otf',
            'assets\\fonts\\cissanthemos\\Cissanthemos.otf',
            'assets\\fonts\\celtica\\Celtica-Bold.ttf',
            'assets\\fonts\\constantia\\CAT_Constantia.ttf',
            'assets\\fonts\\silverblade\\Silverblade.ttf',
            'assets\\fonts\\silverblade\\Silverblade Decorative.ttf',
            'assets\\fonts\\wiking\\font\\FDIWiking-Regular.otf'
        ]
        return random.choice(font_list)

    random.seed(None)
    font_path = pickFont()
    second_font = pickFont()
    print(font_path)
    print(second_font)

    if ("III" in proj_title) or ("'s" in proj_title):
        if font_path == 'assets\\fonts\\blankenburg-2-font\\Blankenburg-eJGx.ttf':
            font_path = pickFont() # switch fonts to one that looks better for that string
        if second_font == 'assets\\fonts\\blankenburg-2-font\\Blankenburg-eJGx.ttf':
            second_font = pickFont() # switch fonts to one that looks better for that string

    def addTitleText(title_text_line, top_edge=0, leave_room=0, cur_font_path=None):
        #print(f"[{top_edge}]", end=" ")
        if None == cur_font_path:
            cur_font_path = font_path

        font_size = 48
        if squash:
            font_size = 24
        t_h = 9999
        bottom_edge = top_edge
        side_margins = 20
        font_multiplier = 1
        line_spacing = 1
        if (("for " in title_text_line) or ("of " in title_text_line)):
            if not no_split:
                font_multiplier = 0.3
                #top_edge -= 7
        if top_edge < 0:
            top_edge = 0
        if True: #random.random() < 0.5:
            # calculate down
            font_size = 64
            calculate_font = True
            while calculate_font:
                fnt = ImageFont.truetype(cur_font_path, int(font_size * font_multiplier))
                #print(title_text_line)
                if ("\n" in title_text_line):
                    t_w, t_h = d.multiline_textsize(title_text_line, font=fnt, spacing=line_spacing)
                else:
                    t_w, t_h = d.textsize(title_text_line, font=fnt, spacing=line_spacing)
                t_h -= top_edge
                #print(t_w, t_h, end=", ", flush=True)
                #t_h += int(t_h*0.21) # add extra spacing for better centering
                bottom_edge = top_edge + t_h
                t_h += leave_room # add space for 'press start'

                if (t_w > (img_width - side_margins)) or ((top_edge + t_h) > (img_height - 30)):
                    font_size -= 1
                else:
                    calculate_font = False

        top_centering = ((img_height - t_h) / 2)
        top_centering = 0
        if (False):
            d.rectangle((  0, # ((img_width - t_w) / 2),
                       (top_edge + (top_centering - 0)),
                       img_width,
                       bottom_edge
                       ), outline=(128,128,0))
        if ("\n" in title_text_line):
            d.multiline_text(((img_width - t_w) / 2, 4 + top_edge + (top_centering - 0)), title_text_line, spacing=line_spacing, font=fnt, fill="white", align="center") #, features="liga"
        else:
            d.text(((img_width - t_w) / 2, 4 + top_edge + (top_centering - 0)), title_text_line, spacing=line_spacing, font=fnt, fill="white", align="center") #, features="liga"
        #print(f"<{bottom_edge}>")
        return bottom_edge

    edge = 10
    room_margin = 25
    room_count = len(split_title)
    cur_font_path = font_path

    if len(split_title) > 1:
        room_count = 0
        for n in split_title:
            if(len(n) == 1):
                sn = n.split("\n")
                for ssn in sn:
                    room_count += 1
            else:
                room_count += 1

        for idx_n, n in enumerate(split_title):
            cur_font_path = font_path
            if len(split_title) == 2:
                if idx_n > 0:
                    cur_font_path = second_font
            room_count -= 1
            room = room_count * room_margin
            if(len(n) == 1):
                sn = n.split("\n")
                for ssn in sn:
                    if (("for " in ssn) or ("of " in ssn)):
                        cur_font_path = second_font
                    edge += addTitleText(ssn, edge, room, cur_font_path=cur_font_path) + 2
            else:
                if (("for " in n) or ("of " in n)):
                    cur_font_path = second_font
                edge += addTitleText(n, edge, room, cur_font_path=cur_font_path) + 2
    else:
        addTitleText(proj_title, cur_font_path=cur_font_path)

    img = removeBlankRows(img, gap_spacing=2)
    d = ImageDraw.Draw(img)

    fnt = ImageFont.truetype(font_path, 10)
    t_w, t_h = d.multiline_textsize("press start", font=fnt, spacing=1)
    t_h += 3
    vert_pos = (img_height - t_h)
    if edge > vert_pos:
        vert_pos = 1

    d.multiline_text(((img_width - t_w) / 2, vert_pos), "press start", spacing=1, font=fnt, fill="white", align="center")

    filename = f"assets/backgrounds/_title_{uuid.uuid4()}.png"
    Path(os.path.dirname(os.path.abspath(filename))).mkdir(parents=True, exist_ok=True)


    img = img.convert('P', palette=Image.ADAPTIVE, colors=3)
    img = img.convert('RGB')
    img.save(filename)

    if edge > img_height:
        print(f"title text exceeded image height: {edge} > {img_height}")
        raise OSError("title text exceeded image height")

    return filename

def title_scene_generation(proj_title):
    sprite_sheet_data = [
        generator.makeSpriteSheet('actor.png', name='actor', type='actor', frames=3),
        generator.makeSpriteSheet('actor_animated.png', name='actor_animated', type='actor_animated', frames=6),
        generator.makeSpriteSheet('cat.png', name='cat', type='static', frames=1),
        generator.makeSpriteSheet('checkbox.png', name='checkbox', type='actor', frames=3),
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

    def scene_gen_Logo(callback):
        actor_list = []
        trigger_list = []
        collision_data_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        gen_scene_bkg = generator.makeBackground("autogen_logo.png")
        scene_script = [
        script.actorHide(actorId='player'), script.overlayShow(color='black', x=0, y=0), script.overlayMoveTo(x=0, y=18, speed='2'), script.wait(time=2), script.switchScene(sceneId='♔REFERENCE_TO_SCENES_<Title Screen>♔', x=0, y=0, direction='', fadeSpeed='2'), script.end()
        ]

        gen_scene_scn = generator.makeScene("_gen_Logo", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Logo")
        gen_scene_scn['script'] = scene_script
        gen_scene_connections = []
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data

    def scene_gen_Title_Screen(callback):
        actor_list = []
        trigger_list = []
        collision_data_list = []

        try:
            title_filename = generateTitleBackground(proj_title)
        except OSError as err:
            print(err)
            try:
                title_filename = generateTitleBackground(proj_title, no_split=True)
            except OSError as err:
                logging.error(proj_title)
                logging.error(err)
                try:
                    title_filename = generateTitleBackground(proj_title, no_split=True, squash=True)
                except OSError as err:
                    logging.error(proj_title)
                    logging.error(err)
                    breakpoint()


        gen_scene_bkg = generator.makeBackground(title_filename)

        scene_script = [
                script.actorHide(actorId='player'),
                script.awaitInput(input=['a', 'b', 'start', 'select']),
                # script.group(children = {
                #     'true': [script.setInputScript(input='start', children = {
                #             'true': [script.scenePushState(), script.switchScene(sceneId='♔REFERENCE_TO_SCENES_<Menu>♔', x=0, y=0, direction='', fadeSpeed='2'), script.end()]
                #             }), script.end()]
                # }),
                script.loop(children = {
                    'true': [script.choice(variable='10', trueText='New Game', falseText='Continue'), script.ifTrue(variable='10', children = {
                    'true': [script.switchScene(sceneId='♔REFERENCE_TO_SCENES_<BeginningCave>♔', x=9, y=7, direction='down', fadeSpeed='4'), script.end()],
                    'false': [script.ifSavedData(children = {
                    'true': [script.loadData(), script.end()],
                    'false': [script.text(text='No Save Data\nFound...'), script.end()]
                }), script.end()]
                }), script.end()]
                }), script.end()
        ]


        gen_scene_scn = generator.makeScene("_gen_Title_Screen", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_Title_Screen")
        gen_scene_scn['script'] = scene_script
        gen_scene_connections = []
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data

    def scene_gen_BeginningCave(callback):
        actor_list = []
        trigger_00 = generator.makeTrigger('trigger_00', 9, 17, 2, 1)
        trigger_list = []
        collision_data_list = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 63, 0, 192, 3, 0, 60, 0, 192, 3, 0, 60, 0, 192, 3, 0, 60, 0, 192, 3, 0, 60, 0, 192, 3, 0, 60, 0, 192, 255, 249, 255, 159, 255]
        gen_scene_bkg = generator.makeBackground("cave.png")

        gen_scene_scn = generator.makeScene("_gen_BeginningCave", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label="scene_gen_BeginningCave")

        def addConnection_00(source_location, source_size, destination_scene_id, destination_location, destination_direction):
            trigger_00 = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])
            trigger_00['script'] = [
                script.switchScene(sceneId=destination_scene_id, x=destination_location[0], y=destination_location[1], direction=destination_direction, fadeSpeed='2'),
                script.end()
            ]
            return trigger_00
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (9, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (9, 17), 'entrance_size': (2, 1)  } }

        gen_scene_connections = [connection_00]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data

    def catalog():
        """
        Returns a list of scene functions from this part of the library.
        """
        return [
            scene_gen_Logo,
            scene_gen_Title_Screen,
            scene_gen_BeginningCave
            ]

    return catalog, sprite_sheet_data

def createExampleProject(proj_title="generated"):
    """
    Demonstration of how the scene generators in this file can be used.
    """
    project = generator.makeBasicProject()
    project.name = proj_title


    # Create sprite sheet for the player sprite
    player_sprite_sheet = generator.addSpriteSheet(project, "actor_animated.png", "actor_animated", "actor_animated")
    project.settings["playerSpriteSheetId"] = player_sprite_sheet["id"]

    scene_data_list = []
    catalog, sprites = title_scene_generation(proj_title)
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
    project.settings["startSceneId"] = project.scenes[0]["id"] # Assumes that the logo is the first scene
    project.settings["startX"] = 0
    project.settings["startY"] = 0

    return project

def generateTitle():
    gen_title = "generated"
    with open("assets/title.json") as json_file:
        rules = json.load(json_file)

    grammar = tracery.Grammar(rules["grammar"])
    grammar.add_modifiers(base_english)
    gen_title = grammar.flatten("#origin#")
    print(gen_title)
    return gen_title

if __name__ == '__main__':
    for n in range(4000):
        random.seed(None)
        proj_title = generateTitle()
        title_munged = proj_title.replace(" ", "").replace(":", "_").replace("'", "_").replace("&", "and")
        destination = f"../gbprojects/generated/{title_munged}"
        generator.initializeGenerator()
        project = createExampleProject(proj_title)
        #generator.writeProjectToDisk(project, output_path = destination)
