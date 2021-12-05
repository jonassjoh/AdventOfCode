from math import prod

def play(p1, p2):
    if not len(p1) or not len(p2): return p1 + p2
    c1, c2 = p1.pop(0), p2.pop(0)
    return play(p1 + [c1, c2], p2) if c1 > c2 else play(p1, p2 + [c2, c1])

def rcombat(p1, p2):
    history = set()

    while p1 and p2:
        h = tuple(p1), tuple(p2)
        if h in history:
            return 0
        history.add(h)

        c1, c2 = p1.pop(0), p2.pop(0)
        subgame, p2_won = (True, rcombat(p1[:c1], p2[:c2])) if len(p1) >= c1 and len(p2) >= c2 else (False, False)

        if (subgame and not p2_won) or (not subgame and c1 > c2):
            p1.extend([c1, c2])
        else:
            p2.extend([c2, c1])

    return 0 if p1 else 1

def score(deck):
    return sum(map(prod, zip(deck, reversed(range(1, len(deck) + 1)))))

def solve(decks):
    p1, p2 = map(list, decks)
    rcombat(p1, p2)
    return score(play(*map(list, decks))), score(p1 + p2)

decks = [ list(map(int, deck.split('\n')[1:])) for deck in open('input', 'r').read().split('\n\n')]

part_1, part_2 = solve(decks)

print(f"The winning player's score is {part_1} (part 1).")
print(f"The winning player's score is {part_2} (part 2).")
