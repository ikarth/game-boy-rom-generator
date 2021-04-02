import tracery
import json
import uuid
import os
import random
import datetime
import itertools
import colorsys
import math
from pathlib import Path
from tracery.modifiers import base_english
from rom_generator import generator
from rom_generator import script_functions as script
import logging
import PIL
from PIL import Image, ImageFont, ImageDraw
from rom_generator.utilities import bcolors
import re

from vendor.seam_carver import seam_carver
from vendor.seam_carver.utils import pad_img, highlight_seam
from vendor.seam_carver.energy_functions import simple_energy, dual_gradient_energy
import numpy as np
from tqdm import trange

def SeamCarverResize(full_image, cropped_by, energy_fn, pad=True, savepoints=None, save_name=None, rotated=False, highlight=False):
    if savepoints == None:
        savepoints = []
    img = full_image.copy()
    if savepoints:
        #Path("carving/" + os.path.basename(os.path.abspath(save_name)).split('.')[0]).mkdir(parents=True, exist_ok=True)
        Path("carving/").mkdir(parents=True, exist_ok=True)
        #print(Path("carving/" + os.path.basename(os.path.abspath(save_name)).split('.')[0]))
    original_color_sum = img.sum()
    for i in trange(cropped_by, desc=f"cropping image by {cropped_by} pixels"):
        #print(img.sum())
        if original_color_sum > img.sum():
            break
        e_map = seam_carver.energy_map(img, energy_fn)
        e_paths, e_totals = seam_carver.cumulative_energy(e_map)
        seam = seam_carver.find_seam(e_paths, seam_carver.seam_end(e_totals))
        if i in savepoints:
            try:
                seam_carver.save_image_with_options(img, highlight, pad, seam, rotated, "carving\\"+os.path.basename(os.path.abspath(save_name)), full_image.shape[0], full_image.shape[1], i, savepoints)
            except Exception as err:
                print(err)
        #print(e_map.sum(), e_paths.sum(), e_totals.sum())
        img = seam_carver.remove_seam(img, seam)
    return img

def CarveSeams(pillow_image, save_name, skip_carving=False):
    """
    Use seam carving to remove black lines in the middle of the image and
    hopefully improve the vertical spacing between words.
    """
    img_array = np.array(pillow_image)
    carving_axis = 'y'
    if 'y' == carving_axis:
        img_array = np.transpose(img_array, axes=(1, 0, 2))

    crop_by = 200
    show_seam = True
    pad_border = False
    savepoints = list(range(crop_by))
    save_points = None

    if skip_carving:
        cropped_img_array = img_array
    else:
        cropped_img_array = SeamCarverResize(img_array,
                                        crop_by,
                                        dual_gradient_energy,
                                        save_name=save_name,
                                        savepoints=savepoints,
                                        rotated=carving_axis=='y',
                                        pad=pad_border,
                                        highlight=show_seam
                                        )



    if 'y' == carving_axis:
        cropped_img_array = np.transpose(cropped_img_array, axes=(1, 0, 2))

    if pad_border:
        h,w = img_array.shape[:2]
        if carving_axis == 'y':
            h,w = w,h
        cropped_img_array = pad_img(cropped_img_array, h, w)

    return Image.fromarray(cropped_img_array)
    # return cropped_img_array

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

def removeBlankRows(image, gap_spacing = 3, carving=False, padding=True):
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

    new_image = scratch_image
    if carving:
        unique_id = str(uuid.uuid4()) + ".png"
        pretrim_image = removeBlankRows(new_image, gap_spacing=0, carving=False, padding=False)
        left, top, right, bottom = 0, 0, img_width, img_height - rows_removed
        pretrim_image = pretrim_image.crop((left, top, right, bottom))
        new_image = CarveSeams(pretrim_image, unique_id)

    if padding:
        padded_image = Image.new("RGB", (img_width, img_height), (0,0,0))
        padded_image.paste(new_image, (0, (img_height - new_image.size[1]) // 2))
        new_image = padded_image
    return new_image

def splitInTheMiddle(string_to_split):
    if (isinstance(string_to_split, list)):
        string_to_split = " ".join(string_to_split)
    print(f"\t\t\t[ {string_to_split} ]")
    parts = string_to_split.split(" ")
    midpoint = len(parts) // 2
    return [parts[:midpoint], parts[midpoint:]]

def generateTitleBackground(proj_title, no_split=False, squash=0, use_seam_carving=True):
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

    if squash > 1:
        if len(split_title) > 1:
            split_title_cdr = split_title[1:]
            split_title_car = split_title[0]
            split_title = [split_title_car]
            split_title = split_title + splitInTheMiddle(split_title_cdr)
        else:
            split_title = splitInTheMiddle(proj_title)

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

    def addTitleText(title_text_line, top_edge=0, leave_room=0, cur_font_path=None, use_seam_carving=True):
        title_text_generation_command = {}
        is_primary_line = True
        #print(f"[{top_edge}]", end=" ")
        #print(type(title_text_line))
        if (isinstance(title_text_line, list)):
            title_text_line = " ".join(title_text_line)
        #print(title_text_line)

        if None == cur_font_path:
            cur_font_path = font_path

        font_size = 48
        if squash > 0:
            font_size = 24
            if squash > 1:
                font_size = 12
                if squash > 2:
                    font_size = 10
        t_h = 9999
        bottom_edge = top_edge
        side_margins = 20
        font_multiplier = 1
        line_spacing = 1
        if (("for " in title_text_line) or ("of " in title_text_line)):
            if not no_split:
                font_multiplier = 0.3
            is_primary_line = False
                #top_edge -= 7
        if top_edge < 0:
            top_edge = 0
        if True: #random.random() < 0.5:
            # calculate down
            font_size = 64
            for n in range(squash):
                font_size *= 0.6
            font_size = int(font_size)
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
            title_text_generation_command = {"type": "multiline_text", "placement": ((img_width - t_w) / 2, 4 + top_edge + (top_centering - 0)), "text": title_text_line, "line_spacing": line_spacing, "fill": "white", "align": "center", "font_path": cur_font_path, "font_size": int(font_size * font_multiplier), "is_primary": is_primary_line}
            d.multiline_text(((img_width - t_w) / 2, 4 + top_edge + (top_centering - 0)), title_text_line, spacing=line_spacing, font=fnt, fill="white", align="center") #, features="liga"
        else:
            title_text_generation_command = {"type": "text", "placement": ((img_width - t_w) / 2, 4 + top_edge + (top_centering - 0)), "text": title_text_line, "line_spacing": line_spacing, "fill": "white", "align": "center", "font_path": cur_font_path, "font_size": int(font_size * font_multiplier), "is_primary": is_primary_line}
            d.text(((img_width - t_w) / 2, 4 + top_edge + (top_centering - 0)), title_text_line, spacing=line_spacing, font=fnt, fill="white", align="center") #, features="liga"
        #print(f"<{bottom_edge}>")
        return bottom_edge, title_text_generation_command

    edge = 10
    room_margin = 25
    room_count = len(split_title)
    cur_font_path = font_path
    text_draw_commands = []

    if len(split_title) > 1:
        room_count = 0
        for n in split_title:
            if(len(n) == 1):
                sn = []
                if (isinstance(n, list)):
                    sn = n
                else:
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
            # print(f"\t\t\t< {n} >")
            if(len(n) == 1):
                sn = []
                if (isinstance(n, list)):
                    sn = n
                else:
                    sn = n.split("\n")
                for ssn in sn:
                    if (("for " in ssn) or ("of " in ssn)):
                        cur_font_path = second_font
                    edge_plus, text_draw_command = addTitleText(ssn, edge, room, cur_font_path=cur_font_path, use_seam_carving=use_seam_carving)
                    edge += edge_plus + 2
                    text_draw_commands.append(text_draw_command)
            else:
                if (("for " in n) or ("of " in n)):
                    cur_font_path = second_font
                edge_plus, text_draw_command = addTitleText(n, edge, room, cur_font_path=cur_font_path, use_seam_carving=use_seam_carving)
                text_draw_commands.append(text_draw_command)
                edge += edge_plus + 2
    else:
        edge_plus, text_draw_command = addTitleText(proj_title, cur_font_path=cur_font_path, use_seam_carving=use_seam_carving)
        text_draw_commands.append(text_draw_command)

    if squash > 0:
        img = removeBlankRows(img, gap_spacing=0)
    else:
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

    if edge > img_height:
        d.rectangle((0, 0, img_width, 2), (255, 64, 0))
    else:
        img = img.convert('P', palette=Image.ADAPTIVE, colors=3)
        img = img.convert('RGB')
    img.save(filename)

    if edge > img_height:
        print(f"title text exceeded image height: {edge} > {img_height}")
        raise OSError("title text exceeded image height")

    # Draw big image
    primary_color_hsv = (random.random(), 0.3 + (random.random() * 0.6), 0.8 + (random.random() * 0.1))
    secondary_color_hsv = (math.sin(primary_color_hsv[0] + 0.5), 0.7 + (random.random() * 0.1), 0.6 + (random.random() * 0.2))
    big_multiplier = 8
    img_width = 160 * big_multiplier
    img_height = 144 * big_multiplier
    big_img = PIL.Image.new("RGB", (img_width, img_height), "black")
    big_d = ImageDraw.Draw(big_img)
    for cmd in text_draw_commands:
        #print(cmd)
        draw_cmd = big_d.text
        if cmd["type"] == "multiline_text":
            draw_cmd = big_d.multiline_text
        fnt = ImageFont.truetype(cmd["font_path"], cmd["font_size"] * 8)
        x1, y1 = cmd["placement"]
        selected_color = colorsys.hsv_to_rgb(primary_color_hsv[0], primary_color_hsv[1], primary_color_hsv[2])
        if not cmd["is_primary"]:
            selected_color = colorsys.hsv_to_rgb(secondary_color_hsv[0], secondary_color_hsv[1], secondary_color_hsv[2])
        selected_color = tuple([int(255 * x) for x in selected_color])
        draw_cmd((x1 * big_multiplier, y1 * big_multiplier), cmd["text"], spacing=cmd["line_spacing"] * big_multiplier, font=fnt, fill=selected_color, align=cmd["align"])
        #print([(x1, y1), cmd["text"], cmd["line_spacing"] * big_multiplier, (255,255,255), cmd["align"]])

    #use_seam_carving = True
    if squash > 0:
        big_img = removeBlankRows(big_img, gap_spacing=0, carving=use_seam_carving, padding=True)
    else:
        big_img = removeBlankRows(big_img, gap_spacing=int(2 * (big_multiplier / 4)), carving=use_seam_carving, padding=True)
    big_d = ImageDraw.Draw(big_img)


    big_filename = filename[:-4] + "_big.png"
    big_img.save(big_filename)


    return filename, big_filename

def title_scene_generation(proj_title, use_seam_carving=True):
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
            title_filename, big_filename = generateTitleBackground(proj_title, use_seam_carving=use_seam_carving)
        except OSError as err:
            print(err)
            try:
                title_filename, big_filename = generateTitleBackground(proj_title, no_split=True, use_seam_carving=use_seam_carving)
            except OSError as err:
                logging.error(proj_title)
                logging.error(err)
                try:
                    title_filename, big_filename = generateTitleBackground(proj_title, no_split=True, squash=1, use_seam_carving=use_seam_carving)
                except OSError as err:
                    try:
                        title_filename, big_filename = generateTitleBackground(proj_title, no_split=True, squash=2, use_seam_carving=use_seam_carving)
                    except OSError as err:
                        try:
                            title_filename, big_filename = generateTitleBackground(proj_title, no_split=True, squash=3, use_seam_carving=use_seam_carving)
                        except OSError as err:
                            logging.error(proj_title)
                            logging.error(err)
                            breakpoint()



        gen_scene_bkg = generator.makeBackground(title_filename)

        scene_script = [
                script.setFalse(variable='26'),
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
        gen_scene_scn['box_cover'] = big_filename
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
        connection_00 = {'type': 'SLOT_CONNECTION', 'creator': addConnection_00, 'args': { 'exit_location': (9, 16), 'exit_direction': 'up', 'entrance': gen_scene_scn['id'], 'entrance_location': (9, 17), 'entrance_size': (2, 1)  }, 'tags': ['A', 'D'] }

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

def createExampleProject(proj_title="generated", use_seam_carving=True):
    """
    Demonstration of how the scene generators in this file can be used.
    """
    project = generator.makeBasicProject()
    project.name = proj_title


    # Create sprite sheet for the player sprite
    player_sprite_sheet = generator.addSpriteSheet(project, "actor_animated.png", "actor_animated", "actor_animated")
    project.settings["playerSpriteSheetId"] = player_sprite_sheet["id"]

    scene_data_list = []
    catalog, sprites = title_scene_generation(proj_title, use_seam_carving=use_seam_carving)
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

    # remove the/a confusion
    gen_title = gen_title.replace(" the a ", " the ")

    # Reduce the number of repetitions of "of the" clauses
    def filterRepeatClauses(g_title, clause_phrase=" of the "):
        if g_title.count(clause_phrase) > 1:
            of_title = g_title.split(clause_phrase)
            print(of_title)
            possible_titles = [g_title]
            for first, second in zip(of_title, of_title[1:]):
                pos_title = first + clause_phrase + second
                print(pos_title)
                possible_titles.append(pos_title)
            return random.choice(possible_titles)
        return g_title
    gen_title = filterRepeatClauses(gen_title, " of the ")
    gen_title = filterRepeatClauses(gen_title, " & ")

    # if there are still too many "of"s make it a subtitle
    if gen_title.count(" of ") > 1:
        gen_title = gen_title.replace(" of ", ": ", 1)


    def filterMacGuffinFromTitle(g_title):
        mgs = re.search("(§.*?§)", g_title)
        found = ""
        if mgs:
            found = mgs.group(1)
            print("##################")
            print(found)
        return g_title.replace('§','').replace('Â',''), found.replace('§','').replace('Â','')

    gen_title, macguffin_title = filterMacGuffinFromTitle(gen_title)

    return gen_title, macguffin_title

if __name__ == '__main__':
    for n in range(4):
        random.seed(None)
        proj_title = generateTitle()
        title_munged = proj_title.replace(" ", "").replace(":", "_").replace("'", "_").replace("&", "and")
        destination = f"../gbprojects/generated/{title_munged}"
        generator.initializeGenerator()
        project = createExampleProject(proj_title)
        #generator.writeProjectToDisk(project, output_path = destination)
