import math

from utils import read_input


TREE = "#"


def part01(input, slope):
    width = len(input[0])
    height = len(input)
    i, j, tree_count = 0, 0, 0
    while j < height:
        cell = input[j][i % width]
        if cell == TREE:
            tree_count += 1
        i += slope[0]
        j += slope[1]
    return tree_count


def part02(input, slopes):
    return math.prod((
        part01(input, slope)
        for slope in slopes
    ))


if __name__ == "__main__":

    input = [
        line.strip("\n")
        for line in read_input("03")
    ]

    print(part01(input, (3, 1)))
    print(part02(input, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))