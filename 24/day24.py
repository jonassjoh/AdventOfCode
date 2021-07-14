# HAPPY NEW YEAR... or something.
import re
from collections import defaultdict
from itertools import repeat

DIRECTIONS = {
    'se': (.5, 1),
    'sw': (-.5, 1),
    'nw': (-.5, -1),
    'ne': (.5, -1),
    'e': (1, 0),
    'w': (-1, 0),
}

def find_tile(reference):
    reference = re.findall('se|sw|nw|ne|e|w', reference)

    pos = (0, 0)
    for step in reference:
        pos = tuple(map(sum, zip(pos, DIRECTIONS[step])))

    return pos

def get_neighbours(tile):
    return map(lambda p: tuple(map(sum, zip(*p))), zip(DIRECTIONS.values(), repeat(tile)))

def game_of_life(black_tiles, days=100):
    for _ in range(days):
        new_tiles = set()
        neighbour_count = defaultdict(int)

        for tile in black_tiles:
            neighbours = set(get_neighbours(tile))
            black_neighbours = len(black_tiles & neighbours)

            for neighbour in neighbours:
                if neighbour not in black_tiles:
                    neighbour_count[neighbour] += 1
            if black_neighbours in [1, 2]:
                new_tiles.add(tile)

        for white_tile, black_neighbours in neighbour_count.items():
            if black_neighbours == 2:
                new_tiles.add(white_tile)

        black_tiles = new_tiles

    return black_tiles

def solve(references):
    black_tiles = set()
    for reference in references:
        tile = find_tile(reference)
        black_tiles ^= { tile }
    return len(black_tiles), len(game_of_life(black_tiles))

references = open('input', 'r').read().split('\n')

part_1, part_2 = solve(references)

print(f"{part_1} tiles are left with the black side up.")
print(f"{part_2} tiles are black after 100 days.")
