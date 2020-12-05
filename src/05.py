from utils import read_input


def decode_part(partition, targets, lower_char, upper_char):
    while len(targets) > 1:
        if partition[0] == lower_char:
            targets = targets[:len(targets) // 2]
        elif partition[0] == upper_char:
            targets = targets[len(targets) // 2:]
        partition = partition[1:]
    return targets[0]


def decode_bsp(bsp):
    assert len(bsp) == 10
    return 8 * decode_part(bsp[:7], range(0, 128), "F", "B") + decode_part(bsp[7:], range(0, 8), "L", "R")


def part01(input):
    return max((
        decode_bsp(bsp)
        for bsp in input
    ))

def part02(input):
    seats_ids = sorted([
        decode_bsp(bsp)
        for bsp in input
    ])
    for idx, seat_id in enumerate(seats_ids):
        if idx - 1 >= 0 and seat_id - 1 not in seats_ids:
            return seat_id - 1


if __name__ == "__main__":
    input = [
        line.strip("\n")
        for line in read_input("05")
    ]

    print(part01(input))
    print(part02(input))
