import numpy as np

content = [line.split() for line in open("input.txt").read().split("\n") if line.strip() != '']


def part1():
    hozPos = 0
    depth = 0
    for (cmd, num) in content:
        num = int(num)
        if cmd == 'forward':
            hozPos += num
        elif cmd == 'down':
            depth += num
        elif cmd == 'up':
            depth -= num
        else:
            print("something went wrong parsing: ", cmd, num)
    return depth, hozPos


def part2():
    hozPos = 0
    depth = 0
    aim = 0
    for (cmd, num) in content:
        num = int(num)
        if cmd == 'forward':
            hozPos += num
            depth += (aim * num)
        elif cmd == 'down':
            aim += num
        elif cmd == 'up':
            aim -= num
        else:
            print("something went wrong parsing: ", cmd, num)
    return depth, hozPos


depth, hozPos = part2()
print("Depth: {}, HorizontalPos: {}".format(depth, hozPos))
print("Multiplied = ", depth * hozPos)
