import json
import types
import uuid
import time
from pathlib import Path


base_gb_project = {
"settings": {},
"scenes": [],
"_version": "1.2.0",
"author": "Generator",
"name": "GenerationTest",
"variables": [],
"backgrounds": [],
"spriteSheets": [],
"music": [],
"customEvents": []
}

default_project_settings = {
        "showCollisions": True,
        "showConnections": True,
        "worldScrollX": 0,
        "worldScrollY": 0,
        "zoom": 100,
        "customColorsWhite": "E8F8E0",
        "customColorsLight": "B0F088",
        "customColorsDark": "509878",
        "customColorsBlack": "202850",
        "startX": 9,
        "startY": 9,
        "startDirection": "down",
        "startSceneId": "",
        "playerSpriteSheetId": "581d34d0-9591-4e6e-a609-1d94f203b0cd"
    }

### Create a basic GBS element, with a unique ID

def makeElement():
  element = {}
  element["id"] = str(uuid.uuid4())
  return element.copy()


def makeSpriteSheet(name, frames, type, filename):
  element = makeElement()
  element["name"] = name
  element["frames"] = frames
  element["type"] = type
  element["filename"] = filename
  element["_v"] = int(round(time.time() * 1000.0)) # set creation time (for versioning?)
  return element

def makeBackground(name, filename, width, height, imageWidth, imageHeight):
  element = makeElement()
  element["name"] = name
  element["width"] = width
  element["height"] = height
  element["imageWidth"] = imageWidth
  element["imageHeight"] = imageHeight
  element["filename"] = filename
  element["_v"] = int(round(time.time() * 1000.0))
  return element

def makeScene(name, background, width, height, x, y, collisions=[], actors=[], triggers=[]):
  element = makeElement()
  element["name"] = name
  element["backgroundId"] = background
  element["width"] = width
  element["height"] = height
  element["x"] = x
  element["y"] = y
  element["collisions"] = collisions
  element["actors"] = actors
  element["triggers"] = triggers
  return element





### Writing the project to disk

def write_project_to_disk(gb_project, filename="test.gbsproj", output_path="../gbprojects/projects/"):
  generated_project = json.dumps(gb_project.__dict__, indent=4)
  print(generated_project)
  Path(output_path).mkdir(parents=True, exist_ok=True)
  with open(f"{output_path}{filename}", "w") as wfile:
    wfile.write(generated_project)


if __name__ == '__main__':
  project = types.SimpleNamespace(**base_gb_project)
  project.settings = default_project_settings.copy()
  a_rock = makeSpriteSheet("rock", 1, "static", "rock.png")
  project.spriteSheets.append(a_rock)
  default_bkg = makeBackground("placeholder", "placeholder.png", 20, 18, 160, 144)
  a_scene = makeScene("Scene 0", default_bkg["id"], 20, 18, 228, 172)
  a_scene["actors"].append(a_rock)
  project.scenes.append(a_scene)
  write_project_to_disk(project)
