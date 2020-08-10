import rom_generator.generator as generator
import argparse
import os
import numpy as np
import uuid
import logging
from PIL import Image
from pathlib import Path

def getTileList(list_of_tile_files=[]):
    """
    Takes a list of tile filenames and loads them from assets/tiles as images.

    Returns a list of Pillow image objects.
    """
    tile_list = []
    input_assets_path = "assets"
    for tile in list_of_tile_files:
        tile_image = None
        print(tile)
        tile_image = generator.getImage(tile, image_type="tiles")
        tile_list.append(tile_image)
    return tile_list

def makeCheckerboardArray(width, height):
    """
    Make an array with a checkerboard pattern.

    Originally implemented to have a test background, but can probably be
    used as a basis for other background generation functions.

    The important thing here is that it returns a 2D array with numbers
    that correspond to the tile indexes.
    """
    board = np.zeros([width, height], dtype=int)
    for j in range(height):
        for i in range(width):
            board[i,j] = (i + (j * height) + (j % 2)) % 2
    board = np.fromfunction(lambda i,j: (i + (j * height) + (j % 2)) % 2, (width, height), dtype=int)
    return board.reshape([width, height]).tolist()

def makeBackgroundCollisions(background_array):
    return []

def generateBackground(background_name, array_of_tiles, list_of_sprites):
    """
    Given an array of tiles, generate a background image for them and return
    a Background object to insert into a project.
    """
    image_path = generateBackgroundImageFromTiles(array_of_tiles, list_of_sprites)
    return generator.makeBackground(image_path, "generated_background")

def generateBackgroundImageFromTiles(array_of_tiles, list_of_sprites):
    """
    Given an array of tiles assemble a background image composed of those tiles.

    array_of_tiles - either a 2d array or a numpy array of index numbers.
    list_of_sprites - an ordered list of sprites, with the order corresponding
                      to the index numbers in the array_of_tiles.

    Generates the image, places it in the assets folder, returns the path to
    the new background image.

    Note that it mostly assumes that you'll be using 8x8 tile images, with each
    image occupying one tile in the grid. Tiles images that span multiple tiles
    or have more complicated collisions should be handled prior to this.
    """

    # Use the size of the first sprite to determine how many pixels we need.
    width = list_of_sprites[0].size[0] * len(array_of_tiles[0])
    height = list_of_sprites[0].size[1] * len(array_of_tiles)
    background_image = Image.new('RGB', (width, height))
    for row_index, row in enumerate(array_of_tiles):
        for col_index, col in enumerate(row):
            coords = (list_of_sprites[0].size[1] * col_index, list_of_sprites[0].size[0] * row_index)
            background_image.paste(list_of_sprites[col], coords)

    # Save the image to a file: we only keep the file path as a reference,
    # rather than keeping the image in memory.
    # TODO: The generated background just get dumped in the backgrounds/
    # folder right now; I should figure out the path issues that will let me
    # put them in their own subfolder so they produce less clutter --IJK
    gen_filepath = Path(generator.getAssetFolder()).joinpath("backgrounds/_generated.png")
    local_image_filename = "_generated_" + str(uuid.uuid4()) + ".png"

    abs_gen_filepath = os.path.abspath(Path(os.path.dirname(gen_filepath)))
    Path(abs_gen_filepath).mkdir(parents=True, exist_ok=True)
    Path(abs_gen_filepath).joinpath('__init__.py').touch()
    background_image.save(Path(abs_gen_filepath).joinpath(local_image_filename))
    print(f"Saved generated background to {Path(abs_gen_filepath).joinpath(local_image_filename)}")
    bkg_abspath = Path(abs_gen_filepath).joinpath(local_image_filename)
    bkg_path = os.path.relpath(bkg_abspath)
    return str(bkg_abspath)

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

    tile_array = makeCheckerboardArray(14, 14)
    background_image = generateBackgroundImageFromTiles(tile_array, tile_list)
