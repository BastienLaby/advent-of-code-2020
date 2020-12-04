import importlib

mod = importlib.import_module("04")
is_field_valid = getattr(mod, "is_field_valid")
is_passport_valid = getattr(mod, "is_passport_valid")


def check_field_validation():
    assert is_field_valid("byr", "2002")
    assert not is_field_valid("byr", "2003")
    assert is_field_valid("hgt", "60in")
    assert is_field_valid("hgt", "190cm")
    assert not is_field_valid("hgt", "190in")
    assert not is_field_valid("hgt", "190")
    assert is_field_valid("hcl", "#123abc")
    assert not is_field_valid("hcl", "#123abz")
    assert not is_field_valid("hcl", "123abc")
    assert is_field_valid("ecl", "brn")
    assert not is_field_valid("ecl", "wat")
    assert is_field_valid("pid", "000000001")
    assert not is_field_valid("pid", "0123456789")


def todict(passport):
    d = {}
    for field in passport:
        k, v = field.split(":")
        d[k] = v
    return d


def check_passport_validation():
    assert not is_passport_valid(todict("eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926".split()))
    assert not is_passport_valid(todict("iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946".split()))
    assert not is_passport_valid(todict("hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277".split()))
    assert not is_passport_valid(todict("hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007".split()))
    assert is_passport_valid(todict("pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f".split()))
    assert is_passport_valid(todict("eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm".split()))
    assert is_passport_valid(todict("hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022".split()))
    assert is_passport_valid(todict("iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719".split()))

if __name__ == "__main__":
    check_field_validation()
    check_passport_validation()