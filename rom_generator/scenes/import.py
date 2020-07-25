##### Imports scenes from a gbsproj #####

import json
import copy
import logging
import os
import textwrap
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

child_count = 0
def convertScripts(scripts):
    global child_count
    print("============")
    print(scripts)
    converted_scripts = []
    for scr in scripts:
        print(scr)
        arg_text = []
        for k_arg, v_arg in scr["args"].items():
            if isinstance(v_arg, str):
                v_arg = f"'{v_arg}'"
            arg_text.append(f"{k_arg}={v_arg}")
        if "children" in scr:
            child_scripts = {}
            for k_arg, v_arg in scr["children"].items():
                print(k_arg, v_arg)
                child_args = convertScripts(v_arg)
                child_scripts.update({k_arg: child_args})
                print("children:")
            print(child_scripts)
            #converted_scripts.append(f"code_children_{child_count:05d} = {child_scripts}")
            #arg_text.append(f"code_children_{child_count:05d}")
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
        func_call_text += ", ".join(arg_text) + ")"
        converted_scripts.append(func_call_text)
        print('=>')
        print(func_call_text)
        print()
    print(converted_scripts)
    #breakpoint()
    return converted_scripts


def convertTriggers(trigger_list, proj_data):
    elements = []
    for element in trigger_list:
        #print(element)
        #print()
        # pattern-matching on triggers

        # Connection
        script = element["script"]
        convertScripts(script)
        if script[0]["command"] == "EVENT_SWITCH_SCENE":
            pass
    return element

def convertActors(actor_list, proj_data):
    elements = []
    code_elements = []
    actor_name_list = []
    for actor_count, element in enumerate(actor_list):
        # pattern-matching on triggers

        sprites = proj_data["spriteSheets"]
        find_sprite = [s for s in sprites if s['id'] == element['spriteSheetId']]
        if (len(find_sprite) < 1):
            logging.error(f"Missing sprite with id of {element['spriteSheetId']}")
        a_sprite = find_sprite[0]
        # code_create_sprite = f"generator.makeSpriteSheet('{a_sprite['filename']}', name='{a_sprite['name']}', type='{a_sprite['type']}', frames={a_sprite['numFrames']})"
        # code_elements.append(f"act_sprite_{sprite_count:04d} = " + copy.copy(code_create_sprite))
        # code_sprites.append(copy.copy(code_create_sprite))
        # code_elements.append(f"generator.makeActor(None, {element['x']}, {element['y']}, {element['movementType']}, {element['animate']}, {element['moveSpeed']}, {element['animSpeed']}, script=script_data, sprite_id=act_sprite_{sprite_count:04d}['id'])")

        code_elements.append(f"actor_{actor_count:02d} = generator.makeActor(None, {element['x']}, {element['y']}, '{element['movementType']}', {element['animate']}, {element['moveSpeed']}, {element['animSpeed']}, script=[], sprite_id=findSpriteByName('{a_sprite['name']}')['id'])")
        # sprite_count += 1

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

        if script[0]["command"] == "EVENT_SWITCH_SCENE":
            pass
        #print(script_start, script_main)
        #code_elements += script_start
        #code_elements += script_main
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
    template.pop("id")
    if "template" in template["name"]:
        print(f"{bcolors.OKBLUE}Found template:{bcolors.ENDC} {template['name']}")

    generated_scene_name = "_gen_" + template["name"]
    # TODO: sanity-check generated_scene_name to make sure it's valid as a
    # Python function name.

    #start_script = template.pop("startScript")

    code_actors = [f"actor_list = []"]

    actors = template.pop("actors")
    triggers = template.pop("triggers")
    print(actors)
    print(triggers)
    code_actors = convertActors(actors, proj_data)
    code_triggers = convertTriggers(triggers, proj_data)

    print(code_actors)

    collision_data = template.pop("collisions")
    background_file_id = template.pop("backgroundId")
    background_filename = findFilenameById(proj_data, background_file_id)

    # Create the lines of source code

    code_col = f"collision_data_list = {collision_data}"
    code_bkg = f"gen_scene_bkg = generator.makeBackground(\"{background_filename}\")"
    code_scn = f"gen_scene_scn = generator.makeScene(\"{generated_scene_name}\", gen_scene_bkg, collisions=collision_data_list, actors=actor_list)"
    code_con = f"gen_scene_connections = []"

    code_scn_data = 'scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "tags": []}'
    code_func_def = f"scene{generated_scene_name}_{scene_num:05d}"
    generate_lines = ["def " + code_func_def + "(callback):",
                        code_actors + [code_col, code_bkg, code_scn, code_con, code_scn_data, "return scene_data"]]
    generated_code = generateCode(generate_lines)
    # print(generated_code)

    print(template)
    return generated_code, code_func_def

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

def importFromGBS(filename):
    proj_data = {}
    with open(filename, "r", encoding="utf-8") as proj_file:
        proj_data = json.load(proj_file)
    print(json.dumps(proj_data, sort_keys=True, indent=3))
    #print(proj_data)

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
    """

    #breakpoint()

    # Backgrounds
    bkgs = proj_data["backgrounds"]

    # Scenes
    scenes = proj_data["scenes"]
    scene_templates = []
    scene_func_names = []
    for scene in scenes:
        scene_code, scene_func_name = importScene(scene, proj_data)
        scene_templates.append(scene_code)
        scene_func_names.append(scene_func_name)

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
    parser.add_argument('--export_folder', '-e', type=str, help="gbsproj file to import", default="rom_generator/scenes/imported/")
    args = parser.parse_args()
    templates = importFromGBS(args.import_file)
    #print(templates)
    exportTemplates(templates, args.export_folder)
