
def destination_cup(n, cup, picked):
    dest = cup - 1
    if dest < 0: dest = n - 1
    while dest in picked:
        dest -= 1
        if dest < 0: dest = n - 1
    return dest

def pick_cups(cups, cup):
    c1 = cups[cup]
    c2 = cups[c1]
    c3 = cups[c2]
    cups[cup] = cups[c3]
    return [c1, c2, c3]

def place_cups(cups, picked, dest):
    # dest -> c1 -> c2 -> c3 -> dest(prev)
    #            ^     ^  do not need to be changed.
    cups[picked[-1]] = cups[dest]
    cups[dest] = picked[0]

def solve(cups, start, moves):
    current = start
    for _ in range(moves):
        picked = pick_cups(cups, current)
        dest = destination_cup(len(cups), current, picked)
        place_cups(cups, picked, dest)
        current = cups[current]
    return cups

def convert(cups):
    """
    Converts the list of cups such that the index 0 represents cup 1 and the
    value is whichever cup that follows cup 1.
    So if you have cups: 132 it would convert to 210.
    """
    cw_cups = [-1] * len(cups)
    for i in range(len(cups) - 1):
        cw_cups[cups[i] - 1] = cups[i + 1] - 1
    cw_cups[cups[-1] - 1] = cups[0] - 1
    return cw_cups

def solve_part1(cups, moves):
    cups = solve(convert(cups), cups[0] - 1, moves)
    res, curr = [], 0
    for i in range(len(cups) - 1):
        curr = cups[curr]
        res.append(curr + 1)
    return ''.join(map(str, res))

def part2_input(cups):
    cups = list(map(int, cups))
    cups = cups + list(range(len(cups) + 1, 1_000_000 + 1))
    return cups

def solve_part2(cups, moves):
    cups = solve(convert(cups), cups[0] - 1, moves)
    a = cups[0]
    b = cups[a]
    return (a + 1) * (b + 1)

input = (list(map(int, "739862541")), 100)
input_part2 = (part2_input("739862541"), 10_000_000)
input0 = (list(map(int, "389125467")), 10)
input1 = (list(map(int, "389125467")), 100)

part_1 = solve_part1(*input)
part_2 = solve_part2(*input_part2)

print(f"The labels on the cup after 1 is {part_1}.")
print(f"The labels after cup 1 multipled together yields {part_2}.")