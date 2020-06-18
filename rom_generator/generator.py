import json
import types
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

def makeElement():
  element = {}
  element["id"] = str(uuid.uuid4())
  return element.copy()

def write_project_to_disk(gb_project, filename="test.gbsproj", output_path="../gbprojects/projects/"):
  generated_project = json.dumps(gb_project.__dict__, indent=4)
  print(generated_project)
  Path(output_path).mkdir(parents=True, exist_ok=True)
  with open(f"{output_path}{filename}", "w") as wfile:
    wfile.write(generated_project)


if __name__ == '__main__':
  project = types.SimpleNamespace(**base_gb_project)
  project.settings = default_project_settings.copy()
  write_project_to_disk(project)
