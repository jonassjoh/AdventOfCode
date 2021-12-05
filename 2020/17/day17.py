from collections import defaultdict
from itertools import product, repeat

def neighbouring_points(point):
    offsets = list(product(*[range(-1, 2)] * len(point)))
    offsets.remove((0,) * len(point))
    neighbours = list(map(lambda p: tuple(map(sum, zip(*p))), zip(offsets, repeat(point)))) # lol
    return neighbours

def simulate(points, cycles):
    for cycle in range(1, cycles + 1):
        neighbour_count = defaultdict(int)
        new_points = []

        for point in points:
            neighbours = neighbouring_points(point)
            alive_neighbours = 0
            for neighbour in neighbours:
                neighbour_count[neighbour] += 1
                if neighbour in points:
                    alive_neighbours += 1
            if alive_neighbours in [2, 3]:
                new_points.append(point)

        for point, no_neighbours in neighbour_count.items():
            if point not in points:
                if no_neighbours == 3:
                    new_points.append(point)

        points = new_points

    return len(points)

points_part1 = []
points_part2 = []
with open('input', 'r') as f:
    y = 0
    for line in f:
        line = list(line)
        for x, c in enumerate(line):
            if c == '#':
                points_part1.append((x, y, 0))
                points_part2.append((x, y, 0, 0))
        y += 1

alive = simulate(points_part1, 6)
print(f"{alive} cubes are alive after 6 cycles (3-d space).")

alive = simulate(points_part2, 6)
print(f"{alive} cubes are alive after 6 cycles (4-d space).")
