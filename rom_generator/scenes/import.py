##### Imports scenes from a gbsproj #####


def importFromGBS(filename):
    return













if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Import gbsproj file and translate it into generator templates")
    parser.add_argument('--import', '-i', type=str, help="gbsproj file to import", default="gbs_projects/scene_templates_test_halls.gbsproj")
    args = parser.parse_args()
    importFromGBS(project, output_path = args.import)
