import math
from functools import reduce

def solve(busses, earliest):
    delays = [bus - earliest % bus for bus in busses]
    delay = min(delays)
    return busses[delays.index(delay)], delay

"""
Chinese remainder theorem.

https://fangya.medium.com/chinese-remainder-theorem-with-python-a483de81fbb8
"""
def chinese_remainder(n, a):
    sum=0
    prod=reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n,a):
        p=prod//n_i
        sum += a_i* mul_inv(p, n_i)*p
    return sum % prod
def mul_inv(a, b):
    b0= b
    x0, x1= 0,1
    if b== 1: return 1
    while a>1 :
        q=a// b
        a, b= b, a%b
        x0, x1=x1 -q *x0, x0
    if x1<0 : x1+= b0
    return x1

def solve_part2(busses):
    n = [bus for bus in busses if bus]
    a = [busses[i] - i for i in range(len(busses)) if busses[i]]
    return chinese_remainder(n,a)

with open('input', 'r') as f:
    earliest = int(f.readline())
    busses = [int(bus) if bus != 'x' else None for bus in f.readline().split(',')]

    bus, delay = solve(list(filter(None, busses)), earliest)
    print(f"The bus ID multiplied by the waiting time is {bus * delay}.")

    timestamp = solve_part2(busses)
    print(f"The earliest timestamp is {timestamp}.")
