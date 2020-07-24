##### Imports scenes from a gbsproj #####

import json
import copy
import logging
import os
from pathlib import Path
from ..utilities import bcolors, translateScriptCommandNames
from rom_generator.meta import scripting

indent_string = "   "

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

def convertScripts(scripts):
    converted_scripts = []
    for scr in scripts:
        print(scr)
        # [s for s in scripting.script_commands where s["command"] = scr["command"]]
        func_call_text = translateScriptCommandNames(scr["command"]) + "("

        arg_text = []
        for k_arg, v_arg in scr["args"].items():
            if isinstance(v_arg, str):
                v_arg = f"'{v_arg}'"
            arg_text.append(f"'{k_arg}'={v_arg}")
        print(scr)
        if "children" in scr:
            for k_arg, v_arg in scr["children"].items():
                print(k_arg, v_arg)
            breakpoint()
        func_call_text += ", ".join(arg_text) + ")"
        print(func_call_text)
        converted_scripts.append(func_call_text)
    breakpoint()
    return converted_scripts


def convertTriggers(trigger_list):
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

def convertActors(actor_list):
    elements = []
    for element in actor_list:
        #print(element)
        #print()
        # pattern-matching on triggers

        if "startScript" in element.keys():
            script = element["startScript"]
            convertScripts(script)

        if "script" in element.keys():
            script = element["script"]
            convertScripts(script)


        if script[0]["command"] == "EVENT_SWITCH_SCENE":
            pass
    return elements

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

    actors = template.pop("actors")
    triggers = template.pop("triggers")
    print(actors)
    print(triggers)
    code_actors = convertActors(actors)
    code_triggers = convertTriggers(triggers)

    collision_data = template.pop("collisions")
    background_file_id = template.pop("backgroundId")
    background_filename = findFilenameById(proj_data, background_file_id)

    # Create the lines of source code
    code_act = f"actor_list = []"
    code_col = f"collision_data_list = {collision_data}"
    code_bkg = f"gen_scene_bkg = generator.makeBackground(\"{background_filename}\")"
    code_scn = f"gen_scene_scn = generator.makeScene(\"{generated_scene_name}\", gen_scene_bkg, collisions=collision_data_list)"
    code_con = f"gen_scene_connections = []"

    code_scn_data = 'scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "tags": []}'
    code_func_def = f"scene{generated_scene_name}_{scene_num:05d}"
    generate_lines = ["def " + code_func_def + "(callback):",
                        [code_act, code_col, code_bkg, code_scn, code_con, code_scn_data, "return scene_data"]]
    generated_code = generateCode(generate_lines)
    # print(generated_code)
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
    for s in catalog():
        scene_data_list.append(s(None))

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

# test creating scenes...
if __name__ == '__main__':
    destination = "../gbprojects/generated_export_test/"
    generator.initializeGenerator()
    project = createExampleProject()
    generator.writeProjectToDisk(project, output_path = destination)

'''

def importFromGBS(filename):
    proj_data = {}
    with open(filename, "r", encoding="utf-8") as proj_file:
        proj_data = json.load(proj_file)
    print(json.dumps(proj_data, sort_keys=True, indent=3))
    #print(proj_data)
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
    generated_code = f"# Generated Scene Functions\n# {output_filename}\n\nfrom rom_generator import generator\n\n" + "\n\n".join(scene_templates) + code_catalog + "\n\n\n" + appendix
    return generated_code

def exportTemplates(generated_code, folder):
    codelines = generated_code.splitlines()
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
