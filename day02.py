import parse

# read input

input_file = __file__.replace(".py", ".input")
input = None
with open(input_file) as f:
    input = f.readlines()

# 3-4 j: wjlb

_line_pattern = "{min:d}-{max:d} {char}: {pwd}"

def parse_line(line):
    res = parse.parse(_line_pattern, line)
    return res["min"], res["max"], res["char"], res["pwd"]


def part01(input):
    valid_pwd_count = 0
    for line in input:
        min, max, char, pwd = parse_line(line)
        if min >= pwd.count(char) <= max:
            valid_pwd_count += 1
    return valid_pwd_count


def part02(input):
    valid_pwd_count = 0
    for line in input:
        min, max, char, pwd = parse_line(line)
        min_char = pwd[min - 1]
        max_char = pwd[max - 1]
        if (min_char, max_char).count(char) == 1:
            valid_pwd_count += 1
    return valid_pwd_count


print(part01(input))
print(part02(input))