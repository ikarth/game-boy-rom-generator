from rom_generator.generator import initializeGenerator, writeProjectToDisk
import rom_generator.generator as generator
import copy
import random

def createExampleProject():
    # Set up a barebones project
    project = generator.makeBasicProject()

    # Create sprite sheet for the player sprite
    player_sprite_sheet = generator.makeSpriteSheet("actor_animated.png", "actor_animated", "actor_animated")
    project.spriteSheets.append(player_sprite_sheet)
    project.settings["playerSpriteSheetId"] = player_sprite_sheet["id"]

    # add a sprite we can use for the rocks
    a_rock_sprite = generator.makeSpriteSheet("rock.png", "rock", "static")
    project.spriteSheets.append(a_rock_sprite)

    # Add a background image
    default_bkg = generator.makeBackground("placeholder.png", "placeholder")
    project.backgrounds.append(default_bkg)

        # Get information about the background
    bkg_x = default_bkg["imageWidth"]
    bkg_y = default_bkg["imageHeight"]
    bkg_width = default_bkg["width"]
    bkg_height = default_bkg["height"]

    # add a sprite to indicate the location of a doorway
    # a better way to do this in the actual levels is to alter the background image instead
    doorway_sprite = generator.makeSpriteSheet("tower.png", "tower", "static")
    project.spriteSheets.append(doorway_sprite)

    # We want to create a bunch of scenes.
    # Here I'm just creating them randomly.
    prior_scenes = 0
    number_of_scenes_to_make = 7
    for make_scene_num in range(number_of_scenes_to_make):
        # Create a scene
        a_scene = copy.deepcopy(generator.makeScene(f"Scene {make_scene_num}", default_bkg))
        # Create an actor
        for x in range(8): # Maximum number of actors in GB Studio is 9
            actor_x = random.randint(1,(bkg_width-3)) # Second value subtracted by 1 to keep sprite within bounds of the screen
            actor_y = random.randint(2,bkg_height-2) # First value added by 1 to keep sprite within bounds of the screen
            example_rock = generator.makeActor(a_rock_sprite, actor_x, actor_y)
            a_scene["actors"].append(example_rock)
        # Add scene to project
        project.scenes.append(copy.deepcopy(a_scene))

    # Add some connections between the scenes.
    # This just throws down a bunch of random connections and tries to
    # make sure that they don't overlap
    scene_connections_translations = {"right":0, "left":1, "up":2, "down":3}
    scene_connections = [[True, True, True, True] for n in range(number_of_scenes_to_make)]
    for y in range(number_of_scenes_to_make):
        for attempts in range(3):
            other_scene = random.randint(0, number_of_scenes_to_make - 2)
            if other_scene >= y:
                other_scene += 1
            chosen_direction = random.choice(["right", "left", "up", "down"])
            if scene_connections[y][scene_connections_translations[chosen_direction]]:
                if scene_connections[other_scene][scene_connections_translations[generator.reverse_direction[chosen_direction]]]:
                    scene_connections[y][scene_connections_translations[chosen_direction]] = False
                    scene_connections[other_scene][scene_connections_translations[generator.reverse_direction[chosen_direction]]] = False
                    generator.addSymmetricSceneConnections(project, project.scenes[y + prior_scenes], project.scenes[other_scene + prior_scenes], chosen_direction, doorway_sprite)
                    break

    # Add some music
    project.music.append(generator.makeMusic("template", "template.mod"))

    # Set the starting scene
    project.settings["startSceneId"] = project.scenes[0]["id"]

    return project

def test_example_project_01(tmpdir):
    initializeGenerator()
    project = createExampleProject()
    writeProjectToDisk(project, output_path=tmpdir)

def test_example_project_02(tmpdir):
    initializeGenerator()
    project = createExampleProject()
    assert(project.scenes[0]["width"] == 20)
    assert(project.scenes[0]["actors"][0]["movementType"] == "static")
    assert(project.scenes[0]["triggers"][0]["script"][1]["command"] == "EVENT_END")
    assert(project.spriteSheets[1]["name"] == "rock")
    assert(project.backgrounds[0]["name"] == "placeholder")
    assert(project.backgrounds[0]["height"] == 18)

def test_collision_map_01(tmpdir):
    collisions = [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    outcome = generator.toByteStrings(collisions)
    print(outcome)
    assert(outcome == [192, 17, 0, 0])

def test_collision_map_02(tmpdir):
    collisions = [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    outcome = generator.toByteStrings(collisions)
    initializeGenerator()

    c_bkg = generator.makeBackground("c_test_3.png", "c_test")
    c_scene = generator.makeScene("c_scene", c_bkg)
    collisions = [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    generator.makeCol(collisions, c_scene)
    print(c_scene["collisions"])
    assert (outcome == c_scene["collisions"])
