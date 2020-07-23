##### Imports scenes from a gbsproj #####

import json

def importFromGBS(filename):
    proj_data = ""
    with open(filename, "r", encoding="utf-8") as proj_file:
        proj_data = json.load(proj_file)
    print(json.dumps(proj_data, sort_keys=True, indent=3))
    #print(proj_data)
    breakpoint()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Import gbsproj file and translate it into generator templates")
    parser.add_argument('--import_file', '-i', type=str, help="gbsproj file to import", default="gbs_projects/scene_templates_test_halls.gbsproj")
    args = parser.parse_args()
    importFromGBS(args.import_file)
