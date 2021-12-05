from collections import Counter

with open('input', 'r') as f:
    answers = f.read().split('\n\n')
    answerPart1 = [len(set(group) - set('\n')) for group in answers]

    answers = [Counter(group) for group in answers]
    answers = [Counter(group.values())[group['\n']+1] for group in answers]

    print(f"The sum of the counts (part1) is {sum(answerPart1)}.")
    print(f"The sum of the counts (part2) is {sum(answers)}.")
