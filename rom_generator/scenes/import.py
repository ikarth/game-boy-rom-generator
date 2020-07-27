##### Imports scenes from a gbsproj #####

import json
import copy
import logging
import os
import textwrap
import keyword
import re
import pprint
from pathlib import Path
from ..utilities import bcolors, translateScriptCommandNames
from rom_generator.meta import scripting

indent_string = "    "

code_line_num = 0
def generateCode(code_tree, indent_depth=0):
    global code_line_num
    code_line_num += 1
    # print(code_line_num)
    # print(code_tree)

    code_string = ""
    if isinstance(code_tree, str):
        return code_tree + "\n"
    for code_line in code_tree:
        if isinstance(code_line, str):
            for n in range(indent_depth):
                code_string = code_string + indent_string
            code_string = code_string + str(code_line) + "\n"
        else:
            if isinstance(code_line, list):
                code_text = generateCode(code_line, indent_depth + 1)
                code_string += code_text
            else:
                logging.error(f"unknown line! {code_line}")
    return code_string

def findFilenameById(proj_data, file_id):
    """
    Find the filename of the file_id being referenced.
    """
    filename = ""
    filtered = [bkg for bkg in proj_data["backgrounds"] if bkg["id"] == file_id]
    if len(filtered) == 0:
        filtered = [sprite for sprite in proj_data["spriteSheets"] if sprite["id"] == file_id]
    if len(filtered) == 0:
        raise ValueError("no matching ID found in gbs project")
    filename = filtered[0]["filename"]
    return filename

def cleanString(input_str):
    v_arg = input_str
    if '\n' in v_arg:
        v_arg = v_arg.replace('\n', '\\n')
    if '\'' in v_arg:
        v_arg = v_arg.replace('\'', '\\\'')
    if 'n\'t' in v_arg:
        v_arg = v_arg.replace('n\'t', 'n\\\'t')
    return f"'{v_arg}'"

child_count = 0
def convertScripts(scripts):
    global child_count
    converted_scripts = []
    for scr in scripts:
        arg_text = []
        if "args" in scr.keys():
            for k_arg, v_arg in scr["args"].items():
                if k_arg[:2] == "__":
                    pass # skip __collapse and other editor variables
                else:
                    if isinstance(v_arg, str):
                        v_arg = cleanString(v_arg)
                    k_str = str(k_arg)
                    if keyword.iskeyword(k_arg):
                        k_str = "do_" + str(k_arg)
                    if k_str == "sceneId":
                        v_arg = {v_arg} #f"<♔sceneId|{v_arg}♔>"
                        # TODO: have way to point sceneId at new target
                    arg_text.append(f"{k_str}={v_arg}")
            if "children" in scr:
                child_scripts = {}
                for k_arg, v_arg in scr["children"].items():
                    child_args = convertScripts(v_arg)
                    child_scripts.update({k_arg: child_args})
                child_scripts_processed = ""
                child_scripts_processed += "{\n"
                subscripts = []
                for k_i, v_i in child_scripts.items():
                    subscripts.append(f"            '{k_i}': [" + ", ".join(v_i) + "]")
                child_scripts_processed += ",\n".join(subscripts)
                child_scripts_processed += "\n        }"

                arg_text.append('children = ' + str(child_scripts_processed))
                child_count += 1
        func_call_text = "script." + translateScriptCommandNames(scr["command"]) + "("
        if len(arg_text) > 0:
            func_call_text += ", ".join(arg_text)
        func_call_text += ")"
        converted_scripts.append(func_call_text)
    return converted_scripts

def convertTriggers(trigger_list, proj_data):
    code_elements = []
    actor_name_list = []
    for actor_count, element in enumerate(trigger_list):
        # TODO: pattern-matching on triggers
        code_elements.append(f"trigger_{actor_count:02d} = generator.makeTrigger('trigger_{actor_count:02d}', {element['x']}, {element['y']}, {element['width']}, {element['height']})")

        script_start = []
        if "startScript" in element.keys():
            script = element["startScript"]
            script_start = convertScripts(script)

        if len(script_start) > 0:
            code_elements.append(f"trigger_{actor_count:02d}['startScript'] = [\n        " + ",\n        ".join(script_start) + "\n    ]")

        script_main = []
        if "script" in element:
            script = element["script"]
            script_main = convertScripts(script)
            if script[0]["command"] == "EVENT_SWITCH_SCENE":
                pass # TODO: detect template flags

        if len(script_main) > 0:
            code_elements.append(f"trigger_{actor_count:02d}['script'] = [\n        " + ",\n        ".join(script_main) + "\n    ]")

        actor_name_list.append(f"trigger_{actor_count:02d}")

    code_elements.append("trigger_list = [" + ", ".join(actor_name_list) + "]")
    return code_elements

def convertActors(actor_list, proj_data):
    code_elements = []
    actor_name_list = []
    for actor_count, element in enumerate(actor_list):

        sprites = proj_data["spriteSheets"]
        find_sprite = [s for s in sprites if s['id'] == element['spriteSheetId']]
        if (len(find_sprite) < 1):
            logging.error(f"Missing sprite with id of {element['spriteSheetId']}")
        a_sprite = find_sprite[0]
        anim_element = ""
        if 'animate' in element.keys():
            anim_element += "animate=" + str(element['animate']) + ", "
        if 'moveSpeed' in element.keys():
            anim_element += "moveSpeed=" + str(element['moveSpeed']) + ", "
        if 'animSpeed' in element.keys():
            anim_element += "animSpeed=" + str(element['animSpeed']) + ", "
        if 'direction' in element.keys():
            anim_element += "direction='" + str(element['direction']) + "', "


        code_elements.append(f"actor_{actor_count:02d} = generator.makeActor(None, {element['x']}, {element['y']}, '{element['movementType']}', {anim_element}script=[], sprite_id=findSpriteByName('{a_sprite['name']}')['id'])")
        script_start = []
        if "startScript" in element.keys():
            script = element["startScript"]
            script_start = convertScripts(script)

        if len(script_start) > 0:
            code_elements.append(f"actor_{actor_count:02d}['startScript'] = [\n        " + ",\n        ".join(script_start) + "\n    ]")

        script_main = []
        if "script" in element:
            script = element["script"]
            script_main = convertScripts(script)

        if len(script_main) > 0:
            code_elements.append(f"actor_{actor_count:02d}['script'] = [\n        " + ",\n        ".join(script_main) + "\n    ]")
        actor_name_list.append(f"actor_{actor_count:02d}")

    code_elements.append("actor_list = [" + ", ".join(actor_name_list) + "]")
    return code_elements

def importSprite(sprite_sheet_data):
    code_spritesheet = f"generator.makeSpriteSheet('{sprite_sheet_data['filename']}', name='{sprite_sheet_data['name']}', type='{sprite_sheet_data['type']}', frames={sprite_sheet_data['numFrames']})"
    return code_spritesheet

scene_num = 0
def importScene(scene_data, proj_data):
    global scene_num
    scene_num += 1
    template = copy.deepcopy(scene_data)
    scene_original_id = template.pop("id")
    if "template" in template["name"]:
        print(f"{bcolors.OKBLUE}Found template:{bcolors.ENDC} {template['name']}")

    generated_scene_name = "_gen_" + template["name"]
    if ' ' in generated_scene_name:
        generated_scene_name = generated_scene_name.replace(' ', '_')
    # TODO: sanity-check generated_scene_name to make sure it's valid as a
    # Python function name.

    #start_script = template.pop("startScript")

    code_actors = [f"actor_list = []"]
    code_triggers = [f"trigger_list = []"]

    actors = template.pop("actors")
    triggers = template.pop("triggers")
    #print(actors)
    #print(triggers)
    code_actors = convertActors(actors, proj_data)
    code_triggers = convertTriggers(triggers, proj_data)

    #print(code_actors)

    collision_data = template.pop("collisions")
    background_file_id = template.pop("backgroundId")
    background_filename = findFilenameById(proj_data, background_file_id)

    # Create the lines of source code
    code_func_name = f"scene{generated_scene_name}_{scene_num:05d}"

    code_col = f"collision_data_list = {collision_data}"
    code_bkg = f"gen_scene_bkg = generator.makeBackground(\"{background_filename}\")"
    code_scn = f"gen_scene_scn = generator.makeScene(\"{generated_scene_name}\", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label={code_func_name})"
    code_con = f"gen_scene_connections = []"

    code_scn_data = 'scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "tags": []}'

    generate_lines = ["def " + code_func_name+ "(callback):",
                        code_actors + code_triggers + [code_col, code_bkg, code_scn, code_con, code_scn_data, "return scene_data"]]
    generated_code = generateCode(generate_lines)
    # print(generated_code)

    print(template)
    return generated_code, code_func_name, scene_original_id

code_catalog_func = '''
def catalog():
    """
    Returns a list of scene functions from this part of the library.
    """
    return '''

appendix = '''
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

'''

import collections.abc
# def replaceKeyInData(data, target_key, replace_func, recursion_level=0):
#     print(recursion_level)
#     if recursion_level > 3:
#         print(data)
#         if recursion_level > 13:
#             breakpoint()
#     if (isinstance(data, list)):
#         for scn_idx, scn_val in enumerate(data):
#             data[scn_idx] = replaceKeyInData(data[scn_idx], target_key, replace_func, recursion_level+1)
#     if (isinstance(data, collections.abc.Mapping)):
#         for scn_idx, scn_val in data.items():
#             if target_key == scn_idx:
#                 data[scn_idx] = replace_func
#             else:
#                 data[scn_idx] = replaceKeyInData(data[scn_idx], target_key, replace_func, recursion_level+1)
#     return data


def replaceInDataByKey(data, target_key, replace_func, recursion_level=0):
    if (isinstance(data, list)):
        for scn_idx, scn_val in enumerate(data):
            data[scn_idx] = replaceInDataByKey(data[scn_idx], target_key, replace_func, recursion_level+1)
    if (isinstance(data, collections.abc.Mapping)):
        for scn_idx, scn_val in data.items():
            if target_key == scn_idx:
                data[scn_idx] = replace_func(data[scn_idx])
            else:
                data[scn_idx] = replaceInDataByKey(data[scn_idx], target_key, replace_func, recursion_level+1)

    return data

def importFromGBS(filename):
    proj_data = {}
    with open(filename, "r", encoding="utf-8") as proj_file:
        proj_data = json.load(proj_file)
    logging.debug(json.dumps(proj_data, sort_keys=True, indent=3))
    #pprint.pprint(proj_data)

    scene_indexes = {v["id"]: k for k, v in enumerate(proj_data["scenes"])}

    template_connections = []

    # Find scene ids in scripts and notate them.
    for scn_idx, scn_val in enumerate(proj_data["scenes"]):
        current_scene_id = scn_val["id"]
        print(current_scene_id)
        replacement_func = lambda scn_id: "INSERT*STRING*HERE"
        def scene_id_replace(s_id):
            logging.info(f"{s_id}\t{current_scene_id}\t{str(s_id)} == {str(current_scene_id)}")
            if str(s_id) == str(current_scene_id):
                return "♔SCENE_REFERENCE_TO_SELF"
            else:
                return "♔SCENE_REFERENCE_TO_ANOTHER_SCENE"
        proj_data["scenes"][scn_idx] = replaceInDataByKey(proj_data["scenes"][scn_idx], 'sceneId', scene_id_replace)

    # for scn_idx, scn_val in enumerate(proj_data["scenes"]):
    #     current_scene_id = scn_val["id"]
    #     def sceneIdReplace(s_id):
    #         if s_id == current_scene_id:
    #             return "<♔SCENE_REFERENCE_SELF♔>"
    #         return s_id # "<♔SCENE_REFERENCE_" + proj_data["scenes"][scene_indexes[s_id]]["name"] + "♔>"
    #     proj_data["scenes"][scn_idx] = replaceKeyInData(proj_data["scenes"], 'sceneId', "sceneIdReplace")
    #

    #breakpoint()

    # Sprites
    spritesheet_code = []
    sheets = proj_data["spriteSheets"]
    for sheet in sheets:
        sprite_code = importSprite(sheet)
        spritesheet_code.append(sprite_code)

    code_load_sprites = "sprite_sheet_data = [\n        " + ",\n        ".join(spritesheet_code) + "]"
    code_find_sprite = """
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
    """

    #breakpoint()

    # Backgrounds
    bkgs = proj_data["backgrounds"]

    # Scenes
    scenes = proj_data["scenes"]
    scene_templates = []
    scene_func_names = []
    scene_original_ids = []
    for scene in scenes:
        scene_code, scene_func_name, scene_original_id = importScene(scene, proj_data)
        scene_templates.append(scene_code)
        scene_func_names.append(scene_func_name)
        scene_original_ids.append(scene_original_id)

    # def findSceneByOriginalId(orig_id):
    #     return scene_func_names[scene_original_ids.index(orig_id)]
    #
    # for s_index, s_template in enumerate(scene_templates):
    #     revised_string = s_template
    #     while True:
    #         id_references = (m for m in re.finditer("<♔.*♔>", revised_string))
    #         first_ref = next(id_references, None)
    #         if first_ref is None:
    #             break
    #         new_target_id = "'000-0000-000'"
    #         old_target_id_pos = re.search("\|'.*'♔>", revised_string[first_ref.start():first_ref.end()])
    #         old_target_id = revised_string[first_ref.start():first_ref.end()][old_target_id_pos.start():old_target_id_pos.end()][2:-3]
    #         print(revised_string[first_ref.start():first_ref.end()])
    #         print(old_target_id)
    #         new_target_id = findSceneByOriginalId(old_target_id)
    #         print(new_target_id)
    #         search_func_call = f"getBySceneLabel('{new_target_id}')"
    #         revised_string = revised_string[:first_ref.start()] + search_func_call + revised_string[first_ref.end():]
    #     scene_templates[s_index] = revised_string


    # TODO:
    # - customEvents
    # music
    # variables

    func_list = f",\n{indent_string}{indent_string}".join(scene_func_names)
    code_catalog = "\n" + code_catalog_func + f"[{func_list}]\n"

    output_filename = os.path.basename(filename).split(".")[0] + ".py"
    generated_code = f"""# Generated Scene Functions\n# {output_filename}\n\nfrom rom_generator import generator\nfrom rom_generator import script_functions as script\n\n"""
    generated_code += "def scene_generation():\n"
    generated_code += indent_string + code_load_sprites + "\n"
    generated_code += indent_string + code_find_sprite + "\n"
    generated_code += textwrap.indent("\n\n".join(scene_templates) + str(code_catalog) + "\nreturn catalog, sprite_sheet_data", indent_string)

    generated_code += "\n\n\n" + appendix
    return generated_code

def exportTemplates(generated_code, folder):
    print(f"generated_code: {generated_code}")
    try:
        codelines = generated_code.splitlines()
    except:
        breakpoint()
    filename = codelines[1][2:]
    print(f"<{filename}>")
    with open(folder + filename, 'w', encoding='utf-8') as py_file:
        py_file.write(generated_code)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Import gbsproj file and translate it into generator templates")
    parser.add_argument('--import_file', '-i', type=str, help="gbsproj file to import", default="gbs_projects/scene_templates_test_halls.gbsproj")
    parser.add_argument('--export_folder', '-e', type=str, help="folder to export to", default="rom_generator/scenes/imported/")
    args = parser.parse_args()
    templates = importFromGBS(args.import_file)
    #print(templates)
    exportTemplates(templates, args.export_folder)
