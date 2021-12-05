from math import sin, cos, radians

CARDINALS = { 'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0) }

class Boat:

    def __init__(self):
        self.angle = 0
        self.pos = (0, 0)
        self.waypoint = (10, 1)

    def move(self, direction, distance):
        if direction == 'F':
            self._move((cos(radians(self.angle)), sin(radians(self.angle))), distance)
        elif direction in ['L', 'R']:
            self.angle += distance * (1 if direction == 'L' else -1)
        else:
            self._move(CARDINALS[direction], distance)

    def _move(self, direction, distance):
        self.pos = tuple(map(sum, zip(self.pos, map(lambda x: x * distance, direction))))

    def _move_part2(self, direction, distance):
        self.waypoint = tuple(map(sum, zip(self.waypoint, map(lambda x: x * distance, direction))))

    def rotate_waypoint(self, angle):
        s, c = sin(radians(angle)), cos(radians(angle))
        self.waypoint = (self.waypoint[0] * c - self.waypoint[1] * s,
                         self.waypoint[0] * s + self.waypoint[1] * c)

    def move_part2(self, direction, distance):
        if direction == 'F':
            self._move(self.waypoint, distance)
        elif direction in ['L', 'R']:
            self.rotate_waypoint(distance * (1 if direction == 'L' else -1))
        else:
            self._move_part2(CARDINALS[direction], distance)

    def traveled(self):
        return sum(map(abs, self.pos))

def solve(instructions, part2=False):
    boat = Boat()
    for instruction in instructions:
        action, value = instruction[0], int(instruction[1:])
        if not part2:
            boat.move(action, value)
        else:
            boat.move_part2(action, value)
    return boat.traveled()

with open('input', 'r') as f:
    instructions = [line.strip() for line in f.readlines()]
    distance = solve(instructions)
    print(f"The ship traveled {distance} units (part1).")
    distance = solve(instructions, part2=True)
    print(f"The ship traveled {distance} units (part2).")
