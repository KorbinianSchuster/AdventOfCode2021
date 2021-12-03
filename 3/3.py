from copy import deepcopy

import numpy as np

content = [line for line in open("input.txt").read().split("\n") if line.strip() != '']
numBits = content[0].__len__()
maxBit = 2 ** numBits - 1
halfLen = content.__len__() / 2.


def checkIfMajority(array, bitPos):
    curr = [num for num in array if num[bitPos] == '1']
    return curr.__len__() >= halfLen


def part1():
    gamma = 0
    for bit in range(numBits):
        if checkIfMajority(content, bit):
            gamma |= (1 << (numBits - bit - 1))

    epsilon = np.uint(~gamma & maxBit)
    power = epsilon * gamma
    return gamma, epsilon, power


def getMajorityArray(array, bitPos, bReturnMaj=True):
    if array.__len__() == 1:
        return array

    maj = np.array([])
    sec = np.array([])
    for num in array:
        if num[bitPos] == '1':
            maj = np.append(maj, num)
        else:
            sec = np.append(sec, num)

    if sec.__len__() > maj.__len__():
        return sec if bReturnMaj else maj
    return maj if bReturnMaj else sec


def part2():
    for bit in range(numBits):
        newMajority = content
        newMinority = content

        for bit in range(numBits):
            newMajority = getMajorityArray(newMajority, bit, bReturnMaj=True)
            newMinority = getMajorityArray(newMinority, bit, bReturnMaj=False)
    lifeSupport = int(newMajority[0], 2) * int(newMinority[0], 2)
    return newMajority, newMinority, lifeSupport



def printRatings(gamma, epsilon, power, oxygen, co2, lifeSupport):
    print("Final Gamma Rate is: {}".format(gamma))
    print("Epsilon Rate: {}".format(epsilon))
    print("Power Comsumption = {}".format(power))
    print("\n oxygen rating: {} || {} ".format(oxygen, int(oxygen[0], 2)))
    print("Co2 Scrubber: {} || {}".format(co2, int(co2[0], 2)))
    print("Life Support Rating: ", lifeSupport)


gamma, epsilon, power = part1()
oxygen, co2, lifeSupport = part2()
printRatings(gamma, epsilon, power, oxygen, co2, lifeSupport)
