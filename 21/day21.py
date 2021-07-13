from functools import reduce

class Food:
    def __init__(self, line):
        self.ingredients, self.allergens = line.split(' (')
        self.ingredients = set(self.ingredients.split(' '))
        self.allergens = set(self.allergens[len('contains '): -1].split(', '))

def solve_part2(allergens):
    changed = True
    while changed:
        changed = False
        for allergen in allergens:
            if len(allergens[allergen]) == 1:
                for other in allergens:
                    if other != allergen:
                        if allergens[allergen].issubset(allergens[other]):
                            changed = True
                            allergens[other] -= allergens[allergen]

    allergens = { k: next(iter(allergens[k])) for k in sorted(allergens.keys()) }
    return ','.join(allergens.values())

def solve(foods):
    ingredients = set()
    allergens = dict()

    for food in foods:
        ingredients |= food.ingredients
        for allergen in food.allergens:
            if allergen in allergens:
                allergens[allergen] &= food.ingredients
            else:
                allergens[allergen] = set(food.ingredients)

    contains_allergen = set(reduce(lambda a, b: a | b, allergens.values()))
    no_allergen = ingredients ^ contains_allergen
    no_allergen_occurances = 0

    for food in foods:
        no_allergen_occurances += len(no_allergen & food.ingredients)

    return no_allergen_occurances, solve_part2(allergens)

foods = list(map(Food, open('input', 'r').read().split('\n')))

part_1, part_2 = solve(foods)

print(f"Ingredients that can't contain any allergens appear {part_1} times.")
print(f"The canonical ingredient list is {part_2}.")
