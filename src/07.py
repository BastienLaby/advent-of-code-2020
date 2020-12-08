from parse import parse

from utils import read_input


_rule_pattern = "{src} bags contain {dst}"


def parse_recipe(line):
    """
    Parse the line and return a tuple :
        (src, comps)
        where comps = ((X, Xcount), (Y, Ycount),...)
    """
    res = parse(_rule_pattern, line)
    src = res["src"]
    if "no other bag" in res["dst"]:
        return (src, [])
    comps = []
    for comp in res["dst"].split(","):
        count, elt = comp.rstrip(".").rstrip("bags").rstrip("bag").strip().split(" ", 1)
        comps.append((elt, int(count)))
    return (src, comps)


_bags = {}


def contains_bag(bag, other_bag):
    """Returns True if bag can contains another bag, else returns False.
    :str bag: name of the cotainer bag
    :str other_bag: name of the content bag to check
    """
    bag_content = [
        comp[0]
        for comp in _bags[bag]
    ]
    if other_bag in bag_content:
        return True
    else:
        return any(
            contains_bag(child_bag, other_bag)
            for child_bag in bag_content
        )


def part01():
    return len([
        None
        for bag in _bags
        if contains_bag(bag, "shiny gold")
    ])


def count_bags(bag):
    bag_content =  _bags[bag]
    if not bag_content:
        return 1  # this bag
    total = 1
    for other_bag, count in bag_content:
        total += count * count_bags(other_bag)
    return total


def part02():
    return count_bags("shiny gold") - 1  # shiny gold doesnt count


if __name__ == "__main__":

    input = [
        line.strip("\n")
        for line in read_input("07")
    ]

    for rule in input:
        src, comps = parse_recipe(rule)
        _bags[src] = comps

    print(part01())
    print(part02())
