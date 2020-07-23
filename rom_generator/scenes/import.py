##### Imports scenes from a gbsproj #####

import json
import copy

"""
def generate_{func_id}():

"""
code_line_num = 0
def generateCode(code_tree, indent_depth=0):
    # global code_line_num
    # code_line_num += 1
    # print(code_line_num)
    # print(code_tree)
    indent_string = "   "
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
                print(f"! {code_line}")
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
    file_id = filtered[0]["id"]
    return filename

def importScene(scene_data, proj_data):
    template = copy.deepcopy(scene_data)
    template.pop("id")
    if "template" in template["name"]:
        print(f"Found template: {template['name']}")

    generated_scene_name = "_gen_" + template["name"]
    # TODO: sanity-check generated_scene_name to make sure it's valid as a
    # Python function name.

    actors = template.pop("actors")

    collision_data = template.pop("collisions")
    background_file_id = template.pop("backgroundId")
    background_filename = findFilenameById(proj_data, background_file_id)


    # Create the lines of source code
    code_act = f"actor_list = []"
    code_col = f"collision_data_list = {collision_data}"
    code_bkg = f"gen_scene_bkg = generator.makeBackground({background_filename})"
    code_scn = f"gen_scene_scn = generator.makeScene({generated_scene_name}, gen_scene_bkg, collisions=collision_data_list)"
    code_con = f"gen_scene_connections = []"

    code_scn_data = 'scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "tags": []}'
    code_func_def = f"def scene{generated_scene_name}():"
    generate_lines = [code_func_def, [code_act, code_col, code_bkg, code_scn, code_con, code_scn_data, "return scene_data"]]
    generated_code = generateCode(generate_lines)
    # print(generated_code)
    return generated_code

def importFromGBS(filename):
    proj_data = {}
    with open(filename, "r", encoding="utf-8") as proj_file:
        proj_data = json.load(proj_file)
    #print(json.dumps(proj_data, sort_keys=True, indent=3))
    #print(proj_data)
    scenes = proj_data["scenes"]
    scene_templates = []
    for scene in scenes:
        scene_templates.append(importScene(scene, proj_data))
    return scene_templates

def makeTemplateFunction():
    return


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Import gbsproj file and translate it into generator templates")
    parser.add_argument('--import_file', '-i', type=str, help="gbsproj file to import", default="gbs_projects/scene_templates_test_halls.gbsproj")
    args = parser.parse_args()
    templates = importFromGBS(args.import_file)
    print(templates)
