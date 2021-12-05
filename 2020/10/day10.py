from collections import defaultdict

MAX_DIFF = 3

def solve(adapters):
    differences = defaultdict(int)
    for i in range(1, len(adapters)):
        differences[adapters[i] - adapters[i-1]] += 1

    return differences[1], differences[3]

def solve_part2(adapters):
    adapters = list(reversed(adapters))
    adapters_set = set(adapters)
    arrangements = { adapters.pop(0): 1 }
    for adapter in adapters:
        possible = set(range(adapter + 1, adapter + 1 + MAX_DIFF)) & adapters_set
        possible = [arrangements[i] for i in possible if i in arrangements]
        arrangements[adapter] = sum(possible)
    return arrangements[0]

with open('input', 'r') as f:
    adapters = list(map(int, f.readlines()))
    adapters = sorted(adapters + [0, max(adapters) + 3])

    d1, d3 = solve(adapters)
    print(f"The 1-jolt diffs multiplied by the 3-jolt diffs yields {d1*d3}.")

    arrangements = solve_part2(adapters)
    print(f"There are {arrangements} different arrangements possible.")
