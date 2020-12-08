import copy

from utils import read_input


class LoopForever(Exception):
    def __init__(self, acc):
        self.acc = acc


class EndOfCode(Exception):
    def __init__(self, acc):
        self.acc = acc


def part01(code):
    i, acc, register = 0, 0, set()
    while True:
        opp, arg = code[i].split(" ")
        if i == len(code) - 1:
            raise EndOfCode(acc=acc)
        if i in register:
            raise LoopForever(acc=acc)
        register.add(i)
        if opp == "nop":
            i += 1
        elif opp == "jmp":
            i += int(arg)
            i = i % len(code)
        elif opp == "acc":
            acc += int(arg)
            i += 1


def part02(code):

    for i, line in enumerate(code):

        if "jmp" not in line and "nop" not in line:
            continue

        # replace jmp by nop and nop by jmp
        src = line.split(" ")[0]
        dst = "jmp" if src == "nop" else "nop"

        code[i] = line.replace(src, dst)
        try:
            part01(code)
        except LoopForever:
            code[i] = code[i].replace(dst, src)
        except EndOfCode as e:
            return e.acc


if __name__ == "__main__":

    code = [
        line.replace("\n", "")
        for line in read_input("08")
    ]

    try:
        part01(code)
    except LoopForever as e:
        print(e.acc)

    print(part02(code))