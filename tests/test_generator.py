from rom_generator.generator import initializeGenerator, createExampleProject, writeProjectToDisk

def test_example_project_01(tmpdir):
    initializeGenerator(asset_folder = "assets/")
    project = createExampleProject()
    writeProjectToDisk(project, output_path=tmpdir)

def test_example_project_02(tmpdir):
    initializeGenerator(asset_folder = "assets/")
    project = createExampleProject()
    assert(project.scenes[0]["x"] == 200)
    assert(project.scenes[0]["actors"][0]["movementType"] == "static")
    assert(project.scenes[0]["triggers"][0]["script"][1]["command"] == "EVENT_END")
    assert(project.spriteSheets[1]["name"] == "rock")
    assert(project.backgrounds[0]["name"] == "placeholder")
    assert(project.backgrounds[0]["height"] == 18)
