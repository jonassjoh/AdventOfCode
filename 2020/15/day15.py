
def solve(puzzle, end):
    history = {}

    for turn, number in enumerate(puzzle):
        history[number] = turn

    last = 0

    for turn in range(len(puzzle), end - 1):
        number = turn - history[last] if last in history else 0
        history[last], last = turn, number

    return last

puzzle = [10, 16, 6, 0, 1, 17]
puzzle0 = [0, 3, 6]

last = solve(puzzle, 2020)
print(f"The last number spoken was {last} (part 1).")

last = solve(puzzle, 30000000) # Fast like a snail, heck ye.
print(f"The last number spoken was {last} (part 2).")
