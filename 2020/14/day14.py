from itertools import product

class Part1:
    def __init__(self):
        self.memory = {}
        self.mask = {
            'and': None,
            'or': None
        }

    def update_mask(self, mask_string):
        self.mask['or'] = int(mask_string.replace('X', '0'), 2)
        self.mask['and'] = int(mask_string.replace('X', '1'), 2)

    def update_memory(self, address, value):
        value = value | self.mask['or']
        value = value & self.mask['and']
        self.memory[address] = value

class Part2:
    def __init__(self):
        self.memory = {}
        self.mask = None

    # Modified version of https://stackoverflow.com/a/52383460/6273410
    def generate_possible_addresses(self, address):
        # Convert mask string into a list so we can easily substitute letters
        seq = list(self.mask)

        for i, c in enumerate(reversed(bin(address)[2:])):
            if seq[-i - 1] == '0':
                seq[-i - 1] = c

        # Find indices of 'X' in seq
        indices = [i for i, c in enumerate(seq) if c == 'X']

        # Generate combinations of 0 and 1 & place them into the list
        for t in product('01', repeat=len(indices)):
            for i, c in zip(indices, t):
                seq[i] = c
            yield int(''.join(seq), 2)

    def update_mask(self, mask_string):
        self.mask = mask_string

    def update_memory(self, address, value):
        for new_address in self.generate_possible_addresses(address):
            self.memory[new_address] = value

part1 = Part1()
part2 = Part2()

with open('input', 'r') as f:
    for line in f:
        lhs, value = line.strip().split(' = ')
        if lhs == 'mask':
            part1.update_mask(value)
            part2.update_mask(value)
        else:
            address = int(lhs.split('[')[1][:-1])
            part1.update_memory(address, int(value))
            part2.update_memory(address, int(value))

value_sum = sum(part1.memory.values())
print(f"The values in the memory sum to {value_sum} (part 1).")

value_sum = sum(part2.memory.values())
print(f"The values in the memory sum to {value_sum} (part 2).")
