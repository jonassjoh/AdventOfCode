
def solve(program):
    accumulator = 0
    pointer = 0
    executed = set()

    while pointer not in executed and pointer < len(program):
        instruction, argument = program[pointer]

        executed.add(pointer)
        pointer += 1

        if instruction == 'acc':
            accumulator += argument

        if instruction == 'jmp':
            pointer += argument - 1

    return accumulator, pointer

def solve_part1(program):
    accumulator, _ = solve(program)
    return accumulator

def solve_part2(program):
    for i in range(len(program)):
        instruction, argument = program[i]
        if instruction != 'acc':
            program[i] = ('jmp' if instruction == 'nop' else 'nop', argument)

        accumulator, pointer = solve(program)
        program[i] = (instruction, argument)

        if pointer == len(program):
            return accumulator

    return None

with open('input', 'r') as f:
    program = [line.strip().split( ) for line in f.readlines()]
    program = [(line[0], int(line[1])) for line in program]

    result = solve_part1(program)
    print(f"The accumulator contains the value {result} (part1).")

    result = solve_part2(program)
    print(f"The accumulator contains the value {result} (part2).")
