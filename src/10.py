from collections import defaultdict

from utils import read_input


_counts = defaultdict(int)


def count_paths(nums):
    if nums[0] in _counts:
        return _counts[nums[0]]

    if len(nums) == 1:
        return _counts.setdefault(nums[0], 1)

    previous_nums = [n for n in nums[1:4] if nums[0] - n <= 3]
    return _counts.setdefault(nums[0], sum([
        count_paths(nums[1 + i:])
        for i, _ in enumerate(previous_nums)
    ]))


def part02(input):
    numbers = sorted([0] + input, reverse=True)
    return count_paths(numbers)

if __name__ == "__main__":

    input = [
        int(line)
        for line in read_input("10")
    ]

    print(part02(input))

