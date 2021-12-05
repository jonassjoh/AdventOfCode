import numpy as np
from itertools import combinations

class Tile:
    def __init__(self, tile):
        id, tile = tile[0], tile[1:]
        self.id = int(id.split(' ')[-1][:-1])
        self.tile = np.array([list(t) for t in tile])

    def trim(self):
        self.tile = self.tile[1:-1, 1:-1]

    def fits(self, right_of, under):
        ok = True
        if right_of is not None:
            ok = ok and all(right_of.tile[:, -1] == self.tile[:, 0])
        if under is not None:
            ok = ok and all(under.tile[-1, :] == self.tile[0, :])
        return ok

    def flip(self, axis):
        self.tile = np.flip(self.tile, axis)

    def rotate(self, n=1):
        self.tile = np.rot90(self.tile, n)

def fits_in_image(image, tile):
    left = image[-1][-1] if len(image) > 0 and len(image[-1]) > 0 else None
    above = None
    if len(image) > 1 and len(image[-2]) > len(image[-1]):
        above = image[-2][len(image[-1])]
    return tile.fits(left, above)

def is_uniform_image(image):
    return len(set(map(len, image))) == 1

def possible_options_that_fit(tiles, image):
    for tile, rest in zip(reversed(tiles), combinations(tiles, len(tiles) - 1)):
        for axis in range(2):
            tile.flip(axis)
            for _ in range(4):
                tile.rotate()
                if fits_in_image(image, tile):
                    yield tile, rest

def build_image(tiles, image):
    if len(tiles) == 0 and is_uniform_image(image):
        return True

    no_options = True
    for tile, rest in possible_options_that_fit(tiles, image):
        no_options = False
        image[-1].append(tile)
        if build_image(rest, image):
            return True
        image[-1].pop()

    if no_options and is_uniform_image(image):
        image.append([])
        if build_image(tiles, image):
            return True
        image.pop()

    return False

def trim_image(image):
    for row in image:
        for tile in row:
            tile.trim()

    image = [ [ tile.tile for tile in row ] for row in image ]
    image = [ np.concatenate(row, 1) for row in image ]
    image = np.concatenate(image)
    return image

def find_roughness(image):
    monster = [list("                  # "), \
               list("#    ##    ##    ###"), \
               list(" #  #  #  #  #  #   ")]
    monster = [ (x, y) for y, row in enumerate(monster) for x, col in enumerate(row) if col == '#' ]
    dimensions = tuple(map(max, zip(*monster)))

    for axis in range(2):
        image = np.flip(image, axis)
        for _ in range(4):
            image = np.rot90(image, 1)
            monsters = 0

            for x in range(image.shape[0] - dimensions[0]):
                for y in range(image.shape[1] - dimensions[1]):
                    is_monster = True
                    for pos in monster:
                        if image[x + pos[0], y + pos[1]] != '#':
                            is_monster = False
                            break
                    if is_monster:
                        monsters += 1

            if monsters > 0:
                return (image == '#').sum() - len(monster) * monsters
    return -1

def solve(tiles):
    image = [[]]
    build_image(tiles, image)
    res = image[0][0].id * image[0][-1].id * image[-1][-1].id * image[-1][0].id

    image = trim_image(image)
    roughness = find_roughness(image)

    return res, roughness

tiles = [Tile(t.split('\n')) for t in open('input', 'r').read().split('\n\n')]

part_1, part_2 = solve(tiles)

print(f"The product of the four corner tiles is {part_1}.")
print(f"The habitat's water roughness is {part_2}.")
