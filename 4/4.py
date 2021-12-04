import numpy as np

boardSize = 5


def parse():
    content = [line for line in open("input.txt").read().split("\n") if line.strip() != '']
    draw = [int(num) for num in content[0].split(',')]
    boardTmp = np.array([list(map(int, num.split())) for num in content[1:]])
    boards = [boardTmp[i:i + boardSize] for i in range(0, len(boardTmp), boardSize)]
    return draw, boards


def checkBoard(currMarked, board, num):
    currMarked[board == num] = 1
    row = currMarked.sum(axis=1)
    col = currMarked.sum(axis=0)
    if boardSize in row or boardSize in col:
        boardSum = np.sum(board[currMarked != 1])
        return boardSum * num
    return -1


def part1():
    marked = np.zeros_like(boards)
    for num in draw:
        for idx, board in enumerate(boards):
            score = checkBoard(marked[idx], board, num)
            if score != -1:
                return score


def part2():
    scores = []
    marked = np.zeros_like(boards)
    for idx in range(len(boards)):
        board = boards[idx]
        for numIdx, num in enumerate(draw):
            score = checkBoard(marked[idx], board, num)
            if score != -1:
                scores.append([numIdx, score])
                break
    return scores[np.argmax(scores,0)[0]][1]


draw, boards = parse()
print(part1())
print(part2())