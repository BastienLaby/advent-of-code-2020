from parse import parse

from utils import read_input


_rule_pattern = "{src} contain {dst}"


def parse_recipe(line):
    """
    Parse the line and return a tuple :
        (src, comps)
        where comps = ((X, Xcount), (Y, Ycount),...)
    """
    res = parse(_rule_pattern, line)
    src = res["src"]
    if "no other bag" in res["dst"]:
        return (src, None)
    comps = []
    for comp in res["dst"].split(","):
        # print(comp)
        count, elt = comp.rstrip(".").rstrip("bags").rstrip("bag").strip().split(" ", 1)
        comps.append((elt, int(count)))
    return (src, comps)


if __name__ == "__main__":

    input = [
        line.strip("\n")
        for line in read_input("07")
    ]

    for rule in input:
        print(parse_recipe(rule))