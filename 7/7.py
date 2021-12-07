import numpy as np


def part1():
    median = np.median(content)  # L1
    print("Lowest linear fuel possible is: ", sum(abs(content-median)))


def part2():
    LUT = np.array([(x*(x+1))/(2) for x in range(0, content.max())])  # Triangle Numbers
    mean = content.mean()
    numLower = content[content < mean].__len__()
    numHigher = content[content > mean].__len__()
    sgn = (numHigher - numLower) / (2 * len(content))  # derivation of Fuel
    steps = (abs(content - np.round(content.mean() + sgn))).astype(int)
    print("Lowest triangle fuel possible is: ", sum(LUT[steps]))


def part2BruteFoce():
    LUT = np.array([(x * (x + 1)) / (2) for x in range(0, content.max())])
    stepsC = (abs(content - np.ceil(content.mean()))).astype(int)  # L2 +- 0.5
    stepsF = (abs(content - np.floor(content.mean()))).astype(int)
    print("Lowest triangle fuel possible is: ", min(sum(LUT[stepsC]), sum(LUT[stepsF])))


content = np.array([int(num) for num in open("input.txt").read().split(",") if num.strip() != ''])
part1()  # 340987
part2()  # 96987874
part2BruteFoce()
