def exists_pair_that_sum_to(numbers, target_sum):
    complements = set()
    for number in numbers:
        complement = target_sum - number
        if complement in complements and complement != number:
            return True
        complements.add(number)
    return False

def solve_part1(numbers, preamble):
    for i in range(preamble, len(numbers)):
        if not exists_pair_that_sum_to(numbers[i-preamble:i], numbers[i]):
            return numbers[i]
    return -1

def solve_part2(numbers, target):
    nums = []
    for number in numbers:
        nums.append(number)
        while sum(nums) > target:
            nums.pop(0)

        if sum(nums) == target:
            return min(nums), max(nums)

with open('input', 'r') as f:
    numbers = list(map(int, f.readlines()))

    invalid = solve_part1(numbers, 25)
    print(f"The first number that does not follow the property is {invalid}.")

    small, large = solve_part2(numbers, invalid)
    print(f"The numbers {small} and {large} add to {small+large}.")
