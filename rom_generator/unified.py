import random
import copy

from rom_generator import generator
from rom_generator import script_functions as script
from rom_generator.scenes import title
from rom_generator.scenes import scene_library
from rom_generator.scenes.imported import VictoryScreen
from rom_generator.scenes.imported import SaveTheWorld

from rom_generator.goexplore import runExploration
import random

class IncompatibleRooms(Exception):
    pass

import datetime
import time
import collections
def RecordRooms(proj_name, scene_data_list, success):
    timestamp = str(time.time())
    with open("log_room_choice.txt", "a") as f:
        for s in scene_data_list:
            nnm = s["scene"]["name"]
            conn = [c["tags"] for c in s["connections"]]
            f.write(f"{timestamp}, {proj_name}, {success}, {nnm}, \"{conn}\"\n")

def createExampleProject(proj_title="generated", macguffin_title="MacGuffin", use_seam_carving=True, r_seed=None, CONNECTION_HEURISTIC = "random"):
    """
    Demonstration of how the scene generators in this file can be used.
    """
    project = generator.makeBasicProject()
    project.name = proj_title
    random.seed(r_seed)

    # Create sprite sheet for the player sprite
    pssi_buckets = collections.Counter()
    for n in range(300):
        player_sprite_sheet_image = random.choice(["actor_animated.png", "player.png", "npc001_walk.png", "npc003.png"])
        pssi_buckets[player_sprite_sheet_image] += 1
    #print(pssi_buckets)
    print(player_sprite_sheet_image)

    player_sprite_sheet = generator.addSpriteSheet(project, player_sprite_sheet_image, "actor_animated_"+player_sprite_sheet_image, "actor_animated")
    project.settings["playerSpriteSheetId"] = player_sprite_sheet["id"]

    scene_data_list = []

    # Add title screen
    catalog, sprites = title.title_scene_generation(proj_title, use_seam_carving=use_seam_carving)
    for scn_func in catalog():
        scene_data_list.append(scn_func(None))
    for element_sprite in sprites:
        project.spriteSheets.append(element_sprite)

    # Add victory screen
    win_catalog, win_sprites = VictoryScreen.scene_generation(proj_title, macguffin_title)
    for scn_func in win_catalog():
        scene_data_list.append(scn_func(None))
    for element_sprite in win_sprites:
        project.spriteSheets.append(element_sprite)

    world_catalog, world_sprites, key_room_name, mentor_sage_name = SaveTheWorld.scene_generation(proj_title, macguffin_title)
    for scn_func in world_catalog():
        scene_data_list.append(scn_func(None))
    for element_sprite in world_sprites:
        project.spriteSheets.append(element_sprite)

    scn_library, spr_library = scene_library.getLibrary()
    for scn_func in scn_library:
        npc_sprite = generator.makeNPCSprite()
        generated_scene = generator.mixinNPC(scn_func(None), npc_sprite, macguffin_title, mentor_sage_name)
        project.spriteSheets.append(npc_sprite)
        scene_data_list.append(generated_scene)
    for element_sprite in spr_library:
        project.spriteSheets.append(element_sprite)

    # Hack to try to make sure the game is able to be completed...
    current_scene_data_list = copy.deepcopy(scene_data_list)
    attempts_to_make = 5
    for n in range(attempts_to_make):
        print(f"connecting attempt {n}")
        if CONNECTION_HEURISTIC == "random":
            generator.connectScenesRandomlySymmetric(scene_data_list)
        if CONNECTION_HEURISTIC == "region":
            generator.connectScenesByRegion(scene_data_list)
        steps_to_solve = generator.testConnections(scene_data_list)
        print(steps_to_solve)
        steps_to_key = generator.testConnections(scene_data_list, key_room_name)
        print("key_room_name")
        print(steps_to_key)
        #steps_to_key = 1 # hack to ignore this check for now...
        if (steps_to_solve < 0) or (steps_to_key < 0):
            if n == (attempts_to_make - 1):
                print("Can't make map with these rooms.")
                for s in scene_data_list:
                    nnm = s["scene"]["name"]
                    conn = [c["tags"] for c in s["connections"]]
                    print(nnm + "\t\t" + str(conn))
                # import pdb; pdb.set_trace()
                RecordRooms(proj_title, scene_data_list, False)
                raise IncompatibleRooms
            print("Solve failed. Trying again...")
            scene_data_list = copy.deepcopy(current_scene_data_list)
        else:
            print("Scenes connected.")
            RecordRooms(proj_title, scene_data_list, True)
            current_scene_data_list = copy.deepcopy(scene_data_list)
            break
    scene_data_list = copy.deepcopy(current_scene_data_list)
    print("### ### ###")

    # actually add the scenes to the project
    for sdata in scene_data_list:
        generator.addSceneData(project, generator.translateReferences(sdata, scene_data_list))

    # Add some music
    project.music.append(generator.makeMusic("template", "template.mod"))

    # Set the starting scene
    project.settings["startSceneId"] = project.scenes[0]["id"] # Assumes that the logo is the first scene
    project.settings["startX"] = 0
    project.settings["startY"] = 0

    return project

def generateWebpageCatalog(catalog_of_roms, destination):
    css_style = '''
        body {
           background-color: #040904;
           font-family: sans-serif;
           color: #f3f3f3;
           text-align: center;
        }
        .container {
          padding: 2em;
          display: grid;
          grid-template: none;
          margin: auto;
          text-align: center;
          gap: 1em;
          align-items: center;
          grid-template-columns: repeat(auto-fit, minmax(21.2em, 1fr));
        }
        .item {
          margin: auto;
          margin-top: 0;
          text-align: center;
          display: inline-block;
          align-self: start;
        }
        a {
          padding: 1em;
          background-color: #545458;
          color: #f3f3f3;
          width: 20em;
          height: 21em;
          display: inline-block;
          font-family: sans-serif;
          text-decoration: none;

          font-weight: bold;
          border-radius: 1em;
        }
        a:hover {
          background-color: #DDD;
          color: #131313;
        }
        img {
          width: 20em;
        }
    '''
    catalog_html = f'<html>\n  <head>\n    <meta content="text/html;charset=utf-8" http-equiv="Content-Type">\n    <title>Generated Game Boy ROMs</title>\n    <style>{css_style}</style>\n  </head>\n  <body>\n    <h1>Generated Game Boy ROMs</h1><p>Controls:<br><b>A button:</b> Z, J, or Alt<br><b>B button:</b> X, K, or Ctrl<br><b>Start:</b> Enter<br><b>Select:</b> Shift</p>\n<p><a style="height:1.5em;" href="https://forms.gle/CZNdgsGUNnq9MDgY6">Want to give me feedback?</a></p>\n    <div class="container">\n'
    for rom_path, full_path in catalog_of_roms:
        webpage = rom_path + "/build/web/index.html"
        with open(full_path + "/metadata.json") as rfile:
            metadata = json.load(rfile)
        print(metadata)
        entry = f'''
        <div class="item">
          <a href="{webpage}">
            <img src="./{rom_path}/box_cover.png" alt="{metadata["title"]}">
            <p>{metadata["title"]}</p>
          </a>
        </div>
        '''
        catalog_html += entry
    catalog_html += "\n    </div>  </body></html>"
    print(catalog_html)

    catalog_filename = str(uuid.uuid4()) + ".html"
    with open(pathlib.Path(destination).joinpath(catalog_filename), "w") as wfile:
        wfile.write(catalog_html)


if __name__ == '__main__':
    import subprocess
    import pathlib
    import os
    import json
    import uuid
    root_path = pathlib.Path(__file__).parent.absolute()
    print(root_path)

    RUN_AUTOEXPLORE = False
    RUN_GB_STUDIO = True
    use_seam_carving = True
    CONNECTION_HEURISTIC = "random"

    generated_roms = []
    number_of_roms_to_generate = 1
    path_to_last_generated_rom = ""
    for n in range(number_of_roms_to_generate):
        random.seed(None)
        proj_title, macguffin_title = title.generateTitle()
        print(proj_title)
        print(macguffin_title)
        if macguffin_title == "":
            macguffin_title = "MacGuffin"

        title_munged = proj_title.replace(" ", "").replace(":", "_").replace("'", "_").replace("&", "and").replace("]|[","3").replace("]","I").replace("|","I").replace("[","I")
        destination = f"../gbprojects/generated/{title_munged}"
        generator.initializeGenerator()
        project_generated = 0
        while project_generated >= 0:
            try:
                project = createExampleProject(proj_title, macguffin_title, use_seam_carving=use_seam_carving, CONNECTION_HEURISTIC=CONNECTION_HEURISTIC)
                project_generated = -1
            except IncompatibleRooms as e:
                project_generated += 1
                print(f"Generation Attempt {project_generated} failed.")

        generator.writeProjectToDisk(project, filename=f"{title_munged[:28]}.gbsproj", output_path = destination)
        if RUN_GB_STUDIO:
            print("Invoking compile for " + os.path.abspath(r'.\compile_rom.bat') + ' ' + os.path.abspath(destination + "/" + f"{title_munged[:28]}.gbsproj"))
            subprocess.call([os.path.abspath(r'.\compile_rom.bat'), os.path.abspath(destination + "/" + f"{title_munged[:28]}.gbsproj")])
            path_to_last_generated_rom = os.path.abspath(destination + "/build/web/rom/game.gb")
            generated_roms.append([title_munged, destination])

    if RUN_AUTOEXPLORE:
        runExploration(path_to_last_generated_rom, destination)
    if RUN_GB_STUDIO:
        generateWebpageCatalog(generated_roms, "../gbprojects/generated/")
        subprocess.call(["pyboy", path_to_last_generated_rom])
