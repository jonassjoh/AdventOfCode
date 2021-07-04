from copy import deepcopy
from pprint import pprint

def clamped(w, h, cell, x, y):
    res = x != 0 or y != 0
    res = res and min(cell[0] + x, cell[1] + y) >= 0
    res = res and cell[0] + x < w and cell[1] + y < h
    return res

def valid(w, h, cell):
    return min(cell[0], cell[1]) >= 0 and cell[0] < w and cell[1] < h

def occupied_neighbours_part2(_map, cell):
    w, h = len(_map), len(_map[0])
    directions = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if x != 0 or y != 0]
    neighbours = 0
    for direction in directions:
        distance = 1
        neighbour = (cell[0] + direction[0] * distance, cell[1] + direction[1] * distance)

        while valid(w, h, neighbour) and _map[neighbour[0]][neighbour[1]] != 'L':
            distance += 1

            if _map[neighbour[0]][neighbour[1]] == '#':
                neighbours += 1
                break

            neighbour = (cell[0] + direction[0] * distance, cell[1] + direction[1] * distance)

    return neighbours

def occupied_neighbours(_map, cell):
    w, h = len(_map), len(_map[0])
    neighbours = adjacent(w, h, cell)
    neighbours = [_map[neighbour[0]][neighbour[1]] for neighbour in neighbours]
    neighbours = [neighbour for neighbour in neighbours if neighbour == '#']
    return len(neighbours)

def adjacent(w, h, cell):
    cells = [(cell[0] + x, cell[1] + y) for x in (-1, 0, 1) for y in (-1, 0, 1) if clamped(w, h, cell, x, y)]
    return cells

def solve(_map, part2=False):
    new_map = []

    while True:
        new_map = deepcopy(_map)

        for x in range(len(_map)):
            for y in range(len(_map[x])):
                if _map[x][y] != '.':
                    if part2:
                        neighbours = occupied_neighbours_part2(_map, (x, y))
                        if neighbours == 0:
                            new_map[x][y] = '#'
                        elif neighbours >= 5:
                            new_map[x][y] = 'L'
                    else:
                        neighbours = occupied_neighbours(_map, (x, y))
                        if neighbours == 0:
                            new_map[x][y] = '#'
                        elif neighbours >= 4:
                            new_map[x][y] = 'L'

        if new_map == _map:
            _map = new_map
            break
        _map = new_map

    occupied = 0
    for x in range(len(_map)):
        for y in range(len(_map[x])):
            if _map[x][y] == '#':
                occupied += 1
    return occupied

with open('input', 'r') as f:
    _map = [list(line.strip()) for line in f.readlines()]
    occupied = solve(_map)
    print(f"{occupied} seats are occupied (part 1).")
    occupied = solve(_map, part2=True)
    print(f"{occupied} seats are occupied (part 2).")
