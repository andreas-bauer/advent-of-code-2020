import re

passports = []
for line in open('input.txt', 'r').read().split('\n\n'):
    passport = line.replace('\n', ' ')
    passports.append(passport)

r_hgt = re.compile("hgt:([0-9]{2,3})(cm|in)")
r_hcl = re.compile("hcl:(#[0-9a-f]{6})")
r_ecl = re.compile("ecl:(amb|blu|brn|gry|grn|hzl|oth)")
r_pid = re.compile(r"pid:([0-9]{9})\b")


def is_valid_date_field(passport, field, min_year, max_year):
    pattern = field + ":([0-9]{4})"
    match = re.search(pattern, passport)
    if not match:
        return False

    year = int(match.group(1))
    return min_year <= year <= max_year


def is_valid_height(passport):
    match = r_hgt.search(passport)
    if not match:
        return False

    unit = match.group(2)
    value = int(match.group(1))
    if unit == "cm":
        return 150 <= value <= 193

    return 59 <= value <= 76


def is_valid(passport):
    return (
        is_valid_date_field(passport, "byr", 1920, 2002)
        and is_valid_date_field(passport, "iyr", 2010, 2020)
        and is_valid_date_field(passport, "eyr", 2020, 2030)
        and is_valid_height(passport)
        and r_hcl.search(passport)
        and r_ecl.search(passport)
        and r_pid.search(passport)
    )


valid_passports = 0
for p in passports:
    if is_valid(p):
        valid_passports += 1

print("Valid passports: " + str(valid_passports))
