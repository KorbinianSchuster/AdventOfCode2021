import numpy as np
import timeit

content = [int(num) for num in open("input.txt").read().split()]


def part1(array):
    diff = np.convolve(array, [1, -1], mode='valid')
    numIncreased = np.count_nonzero(diff[diff > 0])
    return numIncreased


def part2(array):
    slidingWindow = np.convolve(array, np.ones(3), mode='valid')
    numIncreased = part1(slidingWindow)
    return numIncreased


def time(func, args):
    start = timeit.default_timer()
    ret = func(args)
    print("time {}: {}".format(func.__name__, start - timeit.default_timer()))
    return ret


print("Part1:", time(part1, content))
print("Part2:", time(part2, content))
