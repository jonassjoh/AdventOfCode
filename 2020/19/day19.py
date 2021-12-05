import re

def build_regex(rules, rule):
    if rules[rule] in 'ab':
        return rules[rule]
    regex = rules[rule].split(' | ')
    regex = [ f"({''.join([ build_regex(rules, c) for c in r.split(' ') ])})" for r in regex ]
    return f"({'|'.join(regex)})"

rules, messages = list(map(lambda x: x.split('\n'), open('input', 'r').read().replace('"', '').split('\n\n')))
rules = { r[0]: r[1] for r in list(map(lambda x: x.split(': '), rules)) }

regex = f"^{build_regex(rules, '0')}$"
matches_part1 = [ re.match(regex, message) is not None for message in messages ].count(True)

longest = max([len(a) for a in messages])

rules['8'] =  '| '.join(['42 ' * i for i in range(1, longest)]).strip()
rules['11'] =  '| '.join(['42 ' * i + '31 ' * i for i in range(1, longest // 2)]).strip()

regex = f"^{build_regex(rules, '0')}$"
# Only takes about 1m 20s to run!! Fast like the wind.
matches_part2 = [ re.match(regex, message) is not None for message in messages ].count(True)

print(f"{matches_part1} messages completley match rule 0 (part1).")
print(f"{matches_part2} messages completley match rule 0 (part2).")
