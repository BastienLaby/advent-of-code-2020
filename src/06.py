from itertools import groupby
from collections import Counter

from utils import read_input


def get_distincts_answers(group_anwsers):
    counter = Counter()
    for people_anwser in group_anwsers:
        counter.update(people_anwser)
    return len(counter.keys())


def get_unified_anwsers(group_anwsers):
    counter = Counter()
    for people_anwser in group_anwsers:
        counter.update(people_anwser)
    return len([
        answer
        for answer, count in counter.items()
        if count == len(group_anwsers)
    ])


def part01(groups_answers):
    return sum((
        get_distincts_answers(group_anwsers)
        for group_anwsers in groups_answers
    ))


def part02(groups_answers):
    return sum((
        get_unified_anwsers(group_anwsers)
        for group_anwsers in groups_answers
    ))


if __name__ == "__main__":

    input = [
        line.strip("\n")
        for line in read_input("06", ignore_blank_lines=False)
    ]

    groups_answers = [
        " ".join(list(group)).split(" ")
        for is_empty, group in groupby(input, key=lambda x: x == "")
        if not is_empty
    ]

    print(part01(groups_answers))
    print(part02(groups_answers))
