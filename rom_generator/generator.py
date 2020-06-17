import json
from pathlib import Path


def write_project_to_disk(gb_project, filename="test.gbsproj", output_path="../gbprojects/projects/"):
  generated_project = json.dumps(gb_project, indent=4)
  print(generated_project)
  Path(output_path).mkdir(parents=True, exist_ok=True)
  with open(f"{output_path}{filename}", "w") as wfile:
    wfile.write(generated_project)


if __name__ == '__main__':
  project = {}
  write_project_to_disk(project)
