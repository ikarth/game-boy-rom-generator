##### Imports scenes from a gbsproj #####

import json
import copy
import logging
import os
import textwrap
import keyword
import re
import pprint
import itertools
from pathlib import Path
import collections.abc
from ..utilities import bcolors, translateScriptCommandNames
from rom_generator.meta import scripting

indent_string = "    "

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

def getDataByPath(data, path):
    if path == []:
        return data
    if (isinstance(data, list)):
        if (isinstance(path[0], int)):
            return getDataByPath(data[path[0]], path[1:])
    if (isinstance(data, collections.abc.Mapping)):
        return getDataByPath(data[path[0]], path[1:])
    return None

def replaceInDataByPath(data, path, replace_func):
    if (isinstance(data, str)) or (isinstance(data, int)):
        if path == []:
            return replace_func(data)
    if (isinstance(data, list)):
        if (isinstance(path[0], int)):
            data[path[0]] = replaceInDataByPath(data[path[0]], path[1:], replace_func)
            return data
    if (isinstance(data, collections.abc.Mapping)):
        data[path[0]] = replaceInDataByPath(data[path[0]], path[1:], replace_func)
    return data

code_line_num = 0
def generateCode(code_tree, indent_depth=0):
    global code_line_num
    code_line_num += 1
    code_string = ""
    if isinstance(code_tree, str):
        return code_tree + "\n"
    for code_line in code_tree:
        if isinstance(code_line, str):
            for n in range(indent_depth):
                code_line = textwrap.indent(code_line, indent_string)
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

script_converion = {}

def convertFuncCallToTemplate(script_entry):
    if script_entry["command"] in script_converion.keys():
        return script_converion[script_entry["command"]](script_entry)
    return None

def scenesInProject(proj_data):
    scene_list = [(s['id'], s['name']) for s in proj_data["scenes"]]
    scene_id_conversion = {}
    for s in scene_list:
        scene_id_conversion.update({s[0] : f"REFERENCE_TO_SCENES_{s[1]}"})
    return scene_id_conversion

def referencesInProject(proj_data):
    ref_types = ["scenes", "spriteSheets", "backgrounds", "music", "customEvents"]
    ref_id_conversion = {}
    for r in ref_types:
        data_list = [(s['id'], s['name']) for s in proj_data[r]]
        for s in data_list:
            ref_id_conversion.update({s[0] : f"REFERENCE_TO_{r.upper()}_<{s[1]}>"})
    return ref_id_conversion

def convertIdToRef(conversion_table, id):
    result = None
    try:
        result = conversion_table[id]
    except KeyError as err:
        return None
    return result


child_count = 0
def convertScripts(scripts, reference_translation_func=None, proj_data=None):
    if proj_data is not None:
        references_in_project = referencesInProject(proj_data)

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
                        if "♔" in v_arg:
                            if None != reference_translation_func:
                                v_arg = reference_translation_func(v_arg)
                        v_arg = cleanString(v_arg)
                    k_str = str(k_arg)
                    if keyword.iskeyword(k_arg):
                        k_str = "do_" + str(k_arg)
                    if k_str == "sceneId":
                        v_arg = v_arg #f"<♔sceneId|{v_arg}♔>"
                        # TODO: have way to point sceneId at new target
                    arg_text.append(f"{k_str}={v_arg}")
            if "children" in scr:
                child_scripts = {}
                for k_arg, v_arg in scr["children"].items():
                    child_args = convertScripts(v_arg, proj_data=proj_data)
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
        func_call_text = convertFuncCallToTemplate(scr)
        if func_call_text is None:
            func_call_text = "script." + translateScriptCommandNames(scr["command"]) + "("
            if len(arg_text) > 0:
                func_call_text += ", ".join(arg_text)
            func_call_text += ")"
        if func_call_text is not None:
            converted_scripts.append(func_call_text)
    return converted_scripts

def containsReference(script_data, path=[], script_reference_list=[], parent_command=None, recursion_depth=0):
    """
    returns list of non-bound references found in the script and its children.
    """
    ref_list = copy.deepcopy(script_reference_list)
    if (isinstance(script_data, str)):
        if "♔" in script_data:
            ref_list.append((path, script_data, parent_command))
    if (isinstance(script_data, list)):
        for scn_idx, scn_val in enumerate(script_data):
            ref_list = containsReference(scn_val, path + [scn_idx], ref_list, parent_command, recursion_depth=recursion_depth+1)
    if (isinstance(script_data, collections.abc.Mapping)):
        if "command" in script_data.keys():
            parent_command = script_data["command"]
        for scn_idx, scn_val in script_data.items():
            ref_list = containsReference(scn_val, path + [scn_idx], ref_list, parent_command, recursion_depth=recursion_depth+1)
    return ref_list

def recordCommandTemplate(script, reference, path):
    return [script]

slot_classification = {
(lambda slot: ((slot["command"] == "EVENT_SWITCH_SCENE") and (slot["reference"] == "♔REFERENCE_SCENE_SELF♔")), "SLOT_CONNECTION")
#,
#(lambda slot: ((slot["command"] == "EVENT_SWITCH_SCENE") and (slot["reference"] == "♔REFERENCE_SCENE♔")), "SLOT_CONNECTION")
}
#slot_reference_definitions = {
#"SLOT_CONNECTION": ["SLOT_CONNECTION", "direction"]
#}

def addConnection(script, destination, entrance_location, direction):
    return

def slotConnection(slot_template):
    location_x = getDataByPath(slot_template["script"], slot_template["path"][:-1] + ["x"])
    location_y = getDataByPath(slot_template["script"], slot_template["path"][:-1] + ["y"])
    location_direction = getDataByPath(slot_template["script"], slot_template["path"][:-1] + ["direction"])
    slot_template["script"] = replaceInDataByPath(slot_template["script"], slot_template["path"], lambda _: "♔REFERENCE_CONNECTION_DESTINATION♔")
    slot_template["script"] = replaceInDataByPath(slot_template["script"], slot_template["path"][:-1] + ["x"], lambda _: "♔REFERENCE_CONNECTION_ENTRANCE_X♔")
    slot_template["script"] = replaceInDataByPath(slot_template["script"], slot_template["path"][:-1] + ["y"], lambda _: "♔REFERENCE_CONNECTION_ENTRANCE_Y♔")
    slot_template["script"] = replaceInDataByPath(slot_template["script"], slot_template["path"][:-1] + ["direction"], lambda _: "♔REFERENCE_CONNECTION_ENTRANCE_DIRECTION♔")
    return slot_template, {"direction": location_direction, "location": (location_x, location_y)} #["destination_id", "entrance_location", "entrance_direction"]

slot_converstion = {
"SLOT_CONNECTION": lambda slot: slotConnection(slot)
}

def prepareTemplateScript(script, template_slots):
    processed_templates = []
    for slot in template_slots:
        slot_type = slot["command"] + "_" + slot["reference"]
        for classify in slot_classification:
            if classify[0](slot):
                slot_type = classify[1]
                break

        if slot_type[:4] == "SLOT":
            slot_template, slot_arguments = slot_converstion[slot_type](slot)
            p_template = {"type": slot_type,
                        "script": slot_template,
                        "args": slot_arguments}
            processed_templates.append(p_template)
    return processed_templates

def convertTriggers(trigger_list, proj_data):
    code_elements = []
    actor_name_list = []
    template_slots = []
    for actor_count, element in enumerate(trigger_list):
        # TODO: pattern-matching on triggers
        code_elements.append(f"trigger_{actor_count:02d} = generator.makeTrigger('trigger_{actor_count:02d}', {element['x']}, {element['y']}, {element['width']}, {element['height']})")

        script_list = []
        if "startScript" in element:
            script_list.append((element["startScript"], "startScript"))
        if "script" in element:
            script_list.append((element["script"], "script"))

        for script, script_type in script_list:
            ref_list = containsReference(script)
            template_slots_pre = []
            code_for_slot = []

            conversion_table = {
                "♔REFERENCE_CONNECTION_DESTINATION♔": "destination_scene_id",
                "♔REFERENCE_CONNECTION_ENTRANCE_X♔": "destination_location[0]",
                "♔REFERENCE_CONNECTION_ENTRANCE_Y♔": "destination_location[1]",
                "♔REFERENCE_CONNECTION_ENTRANCE_DIRECTION♔": "destination_direction"}

            def translateReferences(source_text):
                for pre, post in conversion_table.items():
                    source_text = source_text.replace(f"\'{pre}\'", post)
                return source_text


            if len(ref_list) > 0:
                for ref in ref_list:
                    template_slots_pre.append({"script": script, "reference": ref[1], "path": ref[0], "command": ref[2]})
                template_slots_post = prepareTemplateScript(script, template_slots_pre)

                for slot in template_slots_post:
                    slot_name = ""
                    if (slot["type"] == "SLOT_CONNECTION"):
                        con_func_begin = [f"def addConnection_{actor_count:02d}(source_location, source_size, destination_scene_id, destination_location, destination_direction):"]
                        con_func_begin.append(f"{indent_string}trigger_{actor_count:02d} = generator.makeTrigger('trigger_connection', source_location[0], source_location[1], source_size[0], source_size[1])")
                        con_func_begin.append(f"{indent_string}trigger_{actor_count:02d}['script'] = [")
                        con_func_end = f"{indent_string}return trigger_{actor_count:02d}"
                        con_func_code = translateReferences(textwrap.indent(",\n".join(convertScripts(script)), indent_string))

                        code_for_slot = code_for_slot + con_func_begin + [[con_func_code]] + [f"{indent_string}]"] + [con_func_end]

                        slot_dir = slot['args']['direction']
                        if slot_dir == '':
                            slot_dir='up'
                        slot_name = f"connection_{actor_count:02d}"
                        slot_args = f"'exit_location': {slot['args']['location']}, 'exit_direction': \'{slot_dir}\', 'entrance': gen_scene_scn['id'], 'entrance_location': {(element['x'], element['y'])}, 'entrance_size': {(element['width'], element['height'])} "
                        slot_conn = f"{slot_name} = {{'type': 'SLOT_CONNECTION', 'creator': addConnection_{actor_count:02d}, 'args': {{ {slot_args} }} }}"

                        code_for_slot.append(slot_conn + "\n")
                        template_slots.append({"code": code_for_slot, "name": slot_name})

            else:
                script_main = convertScripts(script)
                if len(script_main) > 0:
                    code_elements.append(f"trigger_{actor_count:02d}['script'] = [\n        " + ",\n        ".join(script_main) + "\n    ]")
                    actor_name_list.append(f"trigger_{actor_count:02d}")

    code_elements.append("trigger_list = [" + ", ".join(actor_name_list) + "]")


    return code_elements, template_slots

def convertActors(actor_list, proj_data):
    code_elements = []
    actor_name_list = []
    actor_data_list = []
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
        actor_data_list.append({
            "name" : f"actor_{actor_count:02d}",
            "sprite": a_sprite
            })

    code_elements.append("actor_list = [" + ", ".join(actor_name_list) + "]")
    return code_elements, actor_data_list

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

    code_actors = [f"actor_list = []"]
    code_triggers = [f"trigger_list = []"]
    template_slots = []
    actors = template.pop("actors")
    triggers = template.pop("triggers")
    code_actors, actor_data_list = convertActors(actors, proj_data)
    code_triggers, template_slots = convertTriggers(triggers, proj_data)

    code_scene_script = ""
    add_script_to_scene = ""
    if "script" in template.keys():
        script_data = template.pop("script")
        code_script = convertScripts(script_data, proj_data=proj_data)
        #print(code_script)
        code_scene_script = f"scene_script = [\n" + ", ".join(code_script) + "\n]\n"
        add_script_to_scene = "gen_scene_scn['script'] = scene_script"
        #breakpoint()

    collision_data = template.pop("collisions")
    background_file_id = template.pop("backgroundId")
    background_filename = findFilenameById(proj_data, background_file_id)

    # Create the lines of source code
    code_func_name = f"scene{generated_scene_name}_{scene_num:05d}"

    code_col = f"collision_data_list = {collision_data}"
    code_bkg = f"gen_scene_bkg = generator.makeBackground(\"{background_filename}\")"
    code_scn = f"gen_scene_scn = generator.makeScene(\"{generated_scene_name}\", gen_scene_bkg, collisions=collision_data_list, actors=actor_list, triggers=trigger_list, scene_label={code_func_name})"

    code_scn_data = 'scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}'
    code_for_templates = "\n".join([str(x) for x in [t["code"] for t in template_slots]])
    code_for_templates = [t["code"] for t in template_slots]
    code_con = f"gen_scene_connections = [" + ", ".join([t["name"] for t in template_slots]) + "]"

    code_for_refs = [""]
    code_ref = ""#f"gen_scene_references = [" + ", ".join([t["name"] for t in ref_template_slots]) + "]"
    generate_lines = ["def " + code_func_name+ "(callback):",
                        code_actors + code_triggers + [code_col, code_bkg, code_scene_script, code_scn, add_script_to_scene],
                        *code_for_templates,
                        [code_con] + [code_scn_data, "return scene_data"]]

    # for line_index, line in enumerate(generate_lines):
    #     print(line)
    #     print('-')
    #     some_references_remain = True
    #     while some_references_remain:
    #         if "♔" in line:
    #             search_pattern = r"♔REFERENCE_TO_SCENES_\<(.*?<ref>)\>"
    #             match = re.search(search_pattern)
    #             found_id = "XXXXXXXXXXXXXXXXXX"
    #             new_line = re.sub(search_pattern, found_id, line, count=1)
    #             print(f"\t{utilities.bcolors.OKBLUE} {match}")
    #             line = new_line
    #             continue
    #         generate_lines[line_index] = line
    #         some_references_remain = False
    #         #breakpoint()

    generated_code = generateCode(generate_lines)

    print("remaining data in template")
    pprint.pprint(template)
    #breakpoint()

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

'''



def getEntityIds(data, path=[], id_list=[]):
    if (isinstance(data, list)):
        for scn_idx, scn_val in enumerate(data):
            id_list = getEntityIds(scn_val, path + [scn_idx], id_list)
    if (isinstance(data, collections.abc.Mapping)):
        for scn_idx, scn_val in data.items():
            if "id" == scn_idx:
                name = str(path[0]) + "_" + str(path[-1])
                if "name" in data:
                    name = data["name"]
                if "filename" in data:
                    name = data["filename"]
                id_list.append([path, data["id"], name])
            id_list = getEntityIds(scn_val, path + [scn_idx], id_list)
    return id_list

def importFromGBS(filename):
    proj_data = {}
    with open(filename, "r", encoding="utf-8") as proj_file:
        proj_data = json.load(proj_file)
    logging.debug(json.dumps(proj_data, sort_keys=True, indent=3))

    scene_indexes = {v["id"]: k for k, v in enumerate(proj_data["scenes"])}

    entity_ids = getEntityIds(proj_data)
    map_ids_to_names = {i:n for p,i,n in entity_ids}
    map_names_to_ids = {n:i for p,i,n in entity_ids}

    template_connections = []

    conversion_table = referencesInProject(proj_data)
    reference_table = []

    # Find scene ids in scripts and notate them.
    for scn_idx, scn_val in enumerate(proj_data["scenes"]):
        current_scene_id = scn_val["id"]
        print(current_scene_id)
        replacement_func = lambda scn_id: "INSERT*STRING*HERE"
        def scene_id_replace(s_id):
            logging.info(f"{s_id}\t{current_scene_id}\t{str(s_id)} == {str(current_scene_id)}")
            converted_ref = convertIdToRef(conversion_table, s_id)
            if str(s_id) == str(current_scene_id):
                return "♔REFERENCE_SCENE_SELF♔"
            else:
                if converted_ref == None:
                    return "♔REFERENCE_SCENE♔"
                return f"♔{converted_ref}♔"
            return s_id
        def actor_id_replace(s_id):
            logging.info(f"{s_id}\t{current_scene_id}\t{str(s_id)} == {str(current_scene_id)}")
            converted_ref = convertIdToRef(conversion_table, s_id)
            if converted_ref != None:
                return f"♔{converted_ref}♔"
            return s_id
        proj_data["scenes"][scn_idx] = replaceInDataByKey(proj_data["scenes"][scn_idx], 'sceneId', scene_id_replace)
        #proj_data["scenes"][scn_idx] = replaceInDataByKey(proj_data["scenes"][scn_idx], 'actorId', actor_id_replace)

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
    exportTemplates(templates, args.export_folder)
