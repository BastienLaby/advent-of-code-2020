from itertools import combinations

from utils import read_input


def part01(numbers_list, preamble=25):
    for i, number in enumerate(numbers_list[preamble:]):
        last_numbers = numbers_list[i:i + preamble]
        products = [
            i + j
            for i, j in combinations(last_numbers, 2)
        ]
        if number not in products:
            return number


def part02(numbers_list, invalid_number):
    """Returns a list of consecutives ranges of length 2 and more inside the initial number_list
    """
    ranges = []
    for range_size in range(2, len(numbers_list) + 1):
        start, end = 0, range_size - 1
        print(f"testing solutions of size {range_size}")
        while end < len(numbers_list):
            r = numbers_list[start:end + 1]
            if sum(numbers_list[start:end + 1]) == invalid_number:
                print(f"{r} match !")
                return min(r) + max(r)
            start += 1
            end += 1


if __name__ == "__main__":

    code = [
        int(line.replace("\n", ""))
        for line in read_input("09")
    ]

    invalid_number = part01(code, preamble=25)
    print(invalid_number)
    print(part02(code, invalid_number))