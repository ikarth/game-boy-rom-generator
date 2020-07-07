import generator
import argparse
import os
import numpy as np
from PIL import Image
from pathlib import Path


def getTileList(list_of_tile_files=[]):
    tile_list = []
    for tile in list_of_tile_files:
        tile_image = generator.getImage(tile, image_type="tiles")
        tile_list.append(tile_image)
    return tile_list

def makeCheckerboard(width, height):
    board = np.zeros([width, height], dtype=int)
    for j in range(height):
        for i in range(width):
            board[i,j] = (i + (j * height) + (j % 2)) % 2
    board = np.fromfunction(lambda i,j: (i + (j * height) + (j % 2)) % 2, (width, height), dtype=int)
    return board.reshape([width, height]).tolist()

def generateBackgroundTiles(array_of_tiles, list_of_sprites):
    """
    Given an array of tiles assemble a background image composed of those tiles.

    array_of_tiles - either a 2d array or a numpy array of index numbers.
    list_of_sprites - an ordered list of sprites, with the order corresponding
                      to the index numbers in the array_of_tiles.

    Generates the image, places it in the assets folder, returns the path to
    the new background image.
    """
    print(list_of_sprites)
    width = list_of_sprites[0].size[0] * len(array_of_tiles[0])
    height = list_of_sprites[0].size[1] * len(array_of_tiles)
    background_image = Image.new('RGB', (width, height))
    for row_index, row in enumerate(array_of_tiles):
        for col_index, col in enumerate(row):
            coords = (list_of_sprites[0].size[1] * col_index, list_of_sprites[0].size[0] * row_index)
            print(coords)
            background_image.paste(list_of_sprites[col], coords)
    gen_filepath = "../assets/backgrounds/generated/generated.png"
    Path(os.path.basename(gen_filepath)).mkdir(parents=True, exist_ok=True)
    background_image.save(gen_filepath)
    return gen_filepath

def generate_processing_background():
    return

### Run the generator
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate a background image.")
    parser.add_argument('--destination', '-d', type=str, help="destination folder name", default="../gbprojects/projects/")
    parser.add_argument('--assets', '-a', type=str, help="asset folder name", default="../assets/")
    parser.add_argument('--subfolder', '-s', type=bool, help="asset folder name", default=False)
    args = parser.parse_args()
    tile_list = getTileList(["black_tile.png", "white_tile.png"])

    tile_array = makeCheckerboard(14, 14)
    background_image = generateBackgroundTiles(tile_array, tile_list)
