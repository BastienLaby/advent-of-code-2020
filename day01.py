import itertools
import math

# read input

input_file = __file__.replace(".py", ".input")
input = None
with open(input_file) as f:
    input = [
        int(line)
        for line in f.readlines()
        if line
    ]

# find the two factors

def get_sum_factor(numbers, target, factor_count=2):
    for combination in itertools.combinations(numbers, factor_count):
        if sum(combination) == target:
            return combination

print(math.prod(get_sum_factor(input, 2020)))
print(math.prod(get_sum_factor(input, 2020, 3)))