from itertools import groupby
import re

from utils import read_input


_ecl_valid_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
_hcl_regex = "^#[0-9a-f]{6}$"

_fields_checks = {
    "byr": lambda x: "1920" <= x <= "2002",
    "iyr": lambda x: "2010" <= x <= "2020",
    "eyr": lambda x: "2020" <= x <= "2030",
    "hgt": lambda x: (x.endswith("cm") and "150cm" <= x <= "193cm") or (x.endswith("in") and "59in" <= x <= "76in"),
    "hcl": lambda x: re.match(_hcl_regex, x),
    "ecl": lambda x: x in _ecl_valid_colors,
    "pid": lambda x: x.isdigit() and len(x) == 9,
    "cid": lambda x: True,
}
_optionnal_fields = {"cid"}
_mandatory_fields = set(_fields_checks.keys()) - _optionnal_fields


def format_passports(input):
    """ Returns a list of dict representing the passports fields.
    (k, v) where k is the field name and v is the field value.
    Ex : [
        {"eyr":"1972", "cid":"100"}
        {"iyr":"2009", "hcl":"#602927"}
    ]
    """

    passports = [
        " ".join(list(group)).split(" ")
        for is_empty, group in groupby(input, key=lambda x: x == "")
        if not is_empty
    ]

    passports_as_dicts = []
    for passport in passports:
        passport_dict = {}
        for field in passport:
            k, v = field.split(":")
            passport_dict[k] = v
        passports_as_dicts.append(passport_dict)

    return passports_as_dicts


def is_field_valid(name, value):
    return (
        (name in _fields_checks and _fields_checks[name](value))
        or name in _optionnal_fields
    )


def is_passport_valid(passport):
    return all(
        field in passport and is_field_valid(field, passport[field])
        for field in _mandatory_fields
    )


def part01(passports):
    valids_passports = list(filter(
        lambda x: all(field in x for field in _mandatory_fields),
        passports
    ))
    return len(valids_passports)


def part02(passports):
    valids_passports = list(filter(is_passport_valid, passports))
    return len(valids_passports)


if __name__ == "__main__":

    input = [line.strip("\n") for line in read_input("04", ignore_blank_lines=False)]
    passports = format_passports(input)

    # print(passports)
    print(part01(passports))
    print(part02(passports))
