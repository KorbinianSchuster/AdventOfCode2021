import numpy as np


def simulateFish(days=80):
    possibleAges = [x for x in range(9)]  # to guarantee every number
    _, cnt = np.unique(content + possibleAges, return_counts=True)
    cnt -= 1
    for day in range(days):
        tmp = cnt[0]             # breed fish
        cnt = np.roll(cnt, -1)   # age fish
        cnt[6] += tmp            # reset parent fish
    return cnt.sum()


content = [int(num) for num in open("input.txt").read().split(",") if num.strip() != '']
count = simulateFish(256)  # part1 : no argument
print(count)