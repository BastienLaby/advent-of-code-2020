from os.path import dirname, join


_ressources_folder = join(dirname(dirname(__file__)), "ressources")


def read_input(day, ignore_blank_lines=True):
    filename = join(_ressources_folder, day + ".input")
    with open(filename) as f:
        return [
            line
            for line in f.readlines()
            if (not ignore_blank_lines or line)
        ]