from operator import add, mul
"""
expr := literal [ operator literal ]*
operator := * | +
literal := ( expr ) | int

mulexpr := addexpr [ + addexpr ]*
addexpr := literal [ * literal ]*
literal := ( mulexpr ) | int
"""

OPS = {
    '*': mul,
    '+': add
}

def expr(expression):
    r = literal(expression)
    while _op := op(expression):
        l = literal(expression)
        r = _op(r, l)
    return r

def literal(expression, part2=False):
    l = expression.pop(0)
    if l == '(':
        r = expr(expression) if not part2 else mulexpr(expression)
        expression.pop(0) # )
        return r
    return int(l)

def op(expression):
    if len(expression) > 0 and expression[0] in OPS.keys():
        return OPS[expression.pop(0)]
    return None

def mulexpr(expression):
    r = addexpr(expression)
    while len(expression) and (_op := expression[0]) and _op == '*':
        expression.pop(0)
        r *= addexpr(expression)
    return r

def addexpr(expression):
    r = literal(expression, part2=True)
    while len(expression) and (_op := expression[0]) and _op == '+':
        expression.pop(0)
        r += literal(expression, part2=True)
    return r

def solve(expression):
    return expr(expression)

def solve_part2(expression):
    return mulexpr(expression)

result_sum_part1 = 0
result_sum_part2 = 0

with open('input', 'r') as f:
    for line in f:
        line = line.strip().replace(' ', '')
        result_sum_part1 += solve(list(line))
        result_sum_part2 += solve_part2(list(line))

print(f"The sum of the resulting values is {result_sum_part1} (part 1).")
print(f"The sum of the resulting values is {result_sum_part2} (part 2).")