from pprint import pprint

bags = {}

class Bag:

    def __init__(self, name):
        self.name = name
        self.containers = []
        self.contents = {}

    def contained_in(self, container):
        self.containers.append(container)

    def add_content(self, content, count):
        create_bag_if_missing(content)
        bags[content].contained_in(self)
        self.contents[content] = int(count)

def create_bag_if_missing(name):
    if name not in bags:
        bags[name] = Bag(name)

def parse_line(line):
    bag, contents = line.strip()[:-1].split(' bags contain ')
    contents = contents.split(', ')

    create_bag_if_missing(bag)

    for content in contents:
        count, content = content.split(' ', 1)
        if count != "no":
            content = content.rsplit(' ', 1)[0]
            bags[bag].add_content(content, count)

def solve_part1(name, checked):
    containers = bags[name].containers

    count = 0
    for container in containers:
        if container.name not in checked:
            checked.add(container.name)
            count += solve_part1(container.name, checked) + 1
    return count

def solve_part2(name):
    contents = bags[name].contents
    total = 0

    for bag, count in contents.items():
        total += count * (solve_part2(bag) + 1)

    return total

with open('input', 'r') as f:
    for line in f:
        if line != "\n":
            parse_line(line)

    # Let's just assume there are no circular references.

    count = solve_part1('shiny gold', set())
    print(f"{count} bag colors can eventually contain the shiny gold bag.")

    count = solve_part2('shiny gold')
    print(f"{count} bags are required inside the shiny gold bag.")
