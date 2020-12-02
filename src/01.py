import itertools
import math

from utils import read_input


def get_sum_factor(numbers, target, factor_count=2):
    for combination in itertools.combinations(numbers, factor_count):
        if sum(combination) == target:
            return combination


if __name__ == "__main__":
    input = [
        int(line)
        for line in read_input("01")
    ]
    print(math.prod(get_sum_factor(input, 2020)))
    print(math.prod(get_sum_factor(input, 2020, 3)))