import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir,"rom_generator")))
print(sys.path)

from rom_generator.generator import initializeGenerator, makeBasicProject, writeProjectToDisk, addSpriteSheet, makeBackground, makeScene, makeActor, makeElement, makeMusic, getImage
from rom_generator.background import generateBackground, getTileList, makeCheckerboardArray, makeBackgroundCollisions, generateBackgroundImageFromTiles
from PIL import Image

def test_background_generator():

    initializeGenerator()

    project = makeBasicProject()

    # Create sprite sheet for the player sprite
    player_sprite_sheet = addSpriteSheet(project, "actor_animated.png", "actor_animated", "actor_animated")
    project.settings["playerSpriteSheetId"] = player_sprite_sheet["id"]

    # add a sprite we can use for the rocks
    a_rock_sprite = addSpriteSheet(project, "rock.png", "rock", "static")
    a_dog_sprite = addSpriteSheet(project, "dog.png", "dog", "static")

    # Add a background image
    default_bkg = makeBackground("placeholder.png", "placeholder")
    project.backgrounds.append(default_bkg)

    checker_background_tile_list = getTileList(["black_tile.png", "white_tile.png"])
    checker_background_tile_array = makeCheckerboardArray(14, 14)
    checker_background_collisions = makeBackgroundCollisions(checker_background_tile_array)
    checker_background_image_path = generateBackgroundImageFromTiles(checker_background_tile_array, checker_background_tile_list)
    checker_background = makeBackground(checker_background_image_path, "checker_background")
    project.backgrounds.append(checker_background)
    a_scene = makeScene(f"Scene", checker_background)
    project.scenes.append(a_scene)

    checker_background2 = generateBackground("checker_background", checker_background_tile_array, checker_background_tile_list)
    b_scene = makeScene(f"Scene", checker_background2, collisions=checker_background_collisions)
    project.scenes.append(b_scene)

    actor = makeActor(a_rock_sprite, 9, 8)
    a_scene['actors'].append(actor)

    dog_actor = makeActor(a_dog_sprite, 5, 5)

    dog_script = []
    element = makeElement()
    element["command"] = "EVENT_ACTOR_EMOTE"
    element["args"] = {
      "actorId": "player",
      "emoteId": "1"
    }
    dog_script.append(element)
    element = makeElement()
    element["command"] = "EVENT_END"
    dog_script.append(element)
    dog_actor["script"] = dog_script


    a_scene['actors'].append(dog_actor)

    # Add some music
    project.music.append(makeMusic("template", "template.mod"))

    # Set the starting scene
    project.settings["startSceneId"] = project.scenes[0]["id"]

    writeProjectToDisk(project, output_path="../gbprojects/test_background")

    # check the project data
    assert("checker_background" == project.backgrounds[1]["name"])
    assert(224 == project.backgrounds[1]["imageWidth"])

    print(checker_background)
    print(checker_background2)
    # check the generated background image file...
    background_image_filename = "../gbprojects/test_background/assets/backgrounds/" + checker_background["filename"]
    print(background_image_filename)
    assert(os.path.isfile(background_image_filename))
    bkg_img_from_file = Image.open(background_image_filename)
    bkg_img_from_file.close()
