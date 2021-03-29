import random

from rom_generator import generator
from rom_generator import script_functions as script

def scene_generation():
    sprite_sheet_data = [
        generator.makeSpriteSheet('actor.png', name='actor', type='actor', frames=3),
        generator.makeSpriteSheet('actor_animated.png', name='actor_animated', type='actor_animated', frames=6),
        generator.makeSpriteSheet('static.png', name='static', type='static', frames=1)]

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

    def scene_gen_sachita_maze(callback):
        actor_name_table = {}
        actor_list = []
        #trigger_00 = generator.makeTrigger('trigger_00', 9, 4, 2, 1)
        #trigger_01 = generator.makeTrigger('trigger_01', 0, 6, 1, 2)
        #trigger_02 = generator.makeTrigger('trigger_02', 9, 17, 2, 1)
        #trigger_03 = generator.makeTrigger('trigger_03', 19, 11, 1, 2)
        trigger_list = []

        default_bkg = generator.makeBackground("stars.png", "stars")
        bkg_x = default_bkg["imageWidth"]
        bkg_y = default_bkg["imageHeight"]
        bkg_width = default_bkg["width"]
        bkg_height = default_bkg["height"]

        amount = random.randint(1, 5)
        arr = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        increment = 0
        #for x in range(amount): #choosing a random point and making a line of sprites. The amount is the loop #
          # increment = increment + 2
           #actor = makeActor(a_rock_sprite, xPos, increment, "static")
           #a_scene['actors'].append(actor)
         #amount = random.randint(1, 10)

        print("begin maze generation")

        for i in range(1, 20):
            print(i)
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
                #actor = makeActor(a_rock_sprite, xPos - increment, yPos - increment, "static")
                #a_scene['actors'].append(actor)
                increment = increment + 2

            print("while loops start")

            xPos = random.randint(3, 29)
            yPos = random.randint(3, 29)
            if arr[0][xPos-1] == 1 or arr[0][xPos + 1] == 1 or arr[0][xPos-3] == 1:
                xPos = random.randint(3, 29)
            if arr[1][yPos-1] == 1 or arr[1][yPos + 1] == 1 or arr[1][yPos - 3] == 1:
                yPos = random.randint(3, 29)

            # while arr[0][xPos-1] == 1 or arr[0][xPos + 1] == 1 or arr[0][ xPos - 3] == 1:
            #     xPos = random.randint(3, 29)
            #     print("X: " + str(xPos))
            # while arr[1][yPos-1] == 1 or arr[1][yPos + 1] == 1 or arr[1][yPos - 3] == 1:
            #     yPos = random.randint(3, 29)
            #     print("Y:" + str(yPos))

            print("start quads")
            print(xPos, yPos)
            print(len(arr[1]))
            print(yPos-1 + increment)
            print(arr[1])
            print(arr[1][yPos-1 + increment])

            if(0 <= xPos <= 15) and (0 <= yPos <= 15):
                choose = random.randint(1,2)
                if(choose == 1):
                    for a in range(amount):
                        increment = increment + 2
                        #actor = makeActor(a_rock_sprite, xPos, yPos + increment, "static")
                        #a_scene['actors'].append(actor)
                        arr[0][ xPos-1] = 1
                        arr[1][ yPos-1 + increment] = 1
                if(choose == 2):
                    for b in range(amount):
                        increment = increment + 2
                        #actor = makeActor(a_rock_sprite, xPos + increment, yPos, "static")
                        #a_scene['actors'].append(actor)
                        arr[0][xPos-1 + increment] = 1
                        arr[1][yPos-1] = 1

            if(0 <= xPos <= 15) and (15 <= yPos <= 28):
                choose = random.randint(1,2)
                if(choose == 1):
                    for c in range (amount):
                        increment = increment + 2
                        #actor = makeActor(a_rock_sprite, xPos + increment, yPos, "static")
                        #a_scene['actors'].append(actor)
                        arr[0][xPos -1 + increment] = 1
                        arr[1][yPos-1] = 1
                if(choose == 2):
                    for d in range (amount):
                        increment = increment + 2
                        #actor = makeActor(a_rock_sprite, xPos, yPos - increment, "static")
                        #a_scene['actors'].append(actor)

                        arr[0][xPos-1] = 1
                        print(yPos-1 + increment)
                        arr[1][yPos-1 + increment] = 1

            if(15 <= xPos <= 28) and (15 <= yPos <= 28):
                choose = random.randint(1,2)
                if(choose == 1):
                    for e in range (1, amount):
                        #actor = makeActor(a_rock_sprite, xPos, yPos - increment, "static")
                        #a_scene['actors'].append(actor)
                        arr[0][xPos-1] = 1
                        arr[1][yPos-1 - increment] = 1
                if(choose == 2):
                    for f in range (1, amount):
                        increment = increment + 2
                        #actor = makeActor(a_rock_sprite, xPos - increment, yPos, "static")
                        #a_scene['actors'].append(actor)
                        arr[0][xPos-1 - increment] = 1
                        arr[1][yPos-1] = 1
                        increment = increment + 2

            if(15 <= xPos <= 28) and (0 <= yPos <= 15):
                choose = random.randint(1,2)
                if(choose == 1):
                    for g in range (1, amount):
                        #actor = makeActor(a_rock_sprite, xPos, yPos + increment, "static")
                        #a_scene['actors'].append(actor)
                        arr[0][xPos-1] = 1
                        arr[1][yPos -1 - increment] = 1
                        increment = increment + 2
                if(choose == 2):
                      for h in range (1, amount):
                            #actor = makeActor(a_rock_sprite, xPos - increment, yPos, "static")
                            #a_scene['actors'].append(actor)
                            arr[0][xPos -1 + increment] = 1
                            arr[1][yPos-1] = 1
                            increment = increment + 2

        print(arr)
        tile_list = getTileList(["black_tile.png", "white_tile.png"])
        tile_array = makeCheckerboardArray(14, 14)
        background_image = generateBackgroundImageFromTiles(tile_array, tile_list)

        breakpoint()

        gen_scene_connections = []#[connection_00, connection_01, connection_02, connection_03]
        scene_data = {"scene": gen_scene_scn, "background": gen_scene_bkg, "sprites": [], "connections": gen_scene_connections, "references": [], "tags": []}
        return scene_data



    def catalog():
        """
        Returns a list of scene functions from this part of the library.
        """
        return [scene_gen_sachita_maze]

    return catalog, sprite_sheet_data



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
    destination = "../gbprojects/generated_export_test_sachita/"
    runTest(destination)
