import numpy as np
import re


def parse():
    # regEx = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)\n")
    content = re.split("->|\n", open("testInput.txt").read())
    content = [num.split(',') for num in content]
    content = [[int(a), int(b)] for (a, b) in content]
    start = content[0::2]
    end = content[1::2]
    gridSize = max(max(content))
    return start, end, gridSize


def sortIndices(x1, x2, y1, y2):
    (startX, endX) = (x1,x2) if x1 < x2 else (x2, x1)
    (startY, endY) = (y1,y2) if y1 < y2 else (y2, y1)
    return startX, endX, startY, endY


def part1():  # horizontal & vertical
    for idx, (x1, y1) in enumerate(start):
        x2, y2 = end[idx]
        if x1 != x2 and y1 != y2:
            continue
        startX, endX, startY, endY = sortIndices(x1, x2, y1, y2)
        if startX == endX:
            grid[startY:endY + 1, startX] += 1
        else:
            grid[startY, startX:endX + 1] += 1


def part2():  # diagonal (45°)
    for idx, (x1, y1) in enumerate(start):
        x2, y2 = end[idx]
        if x1 == x2 or y1 == y2:
            continue
        startX, endX, startY, endY = sortIndices(x1, x2, y1, y2)
        gridWindow = grid[startY:endY + 1, startX:endX + 1]
        m = (y2-y1)/(x2-x1)
        if m > 0:
            np.fill_diagonal(gridWindow, gridWindow.diagonal() + 1)
        else:
            tmp = np.zeros_like(gridWindow)
            np.fill_diagonal(tmp, 1)
            gridWindow += np.fliplr(tmp)


start, end, gridSize = parse()
grid = np.zeros([gridSize + 1, gridSize + 1])
part1()
part2()
numOverlaps = sum(sum(grid >= 2))
print(numOverlaps)
