import re

input = open('input.txt', 'r').read()

passports = input.split('\n\n')

r_byr = re.compile("(byr:)")
r_iyr = re.compile("(iyr:)")
r_eyr = re.compile("(eyr:)")
r_hgt = re.compile("(hgt:)")
r_hcl = re.compile("(hcl:)")
r_ecl = re.compile("(ecl:)")
r_pid = re.compile("(pid:)")

def has_all_fields(passport):
    return (
        r_byr.search(passport) and
        r_iyr.search(passport) and
        r_eyr.search(passport) and
        r_hgt.search(passport) and
        r_hcl.search(passport) and
        r_ecl.search(passport) and
        r_pid.search(passport)
    )

valid_passports = 0
for p in passports:
    if has_all_fields(p):
        valid_passports += 1


print("Valid passports: " + str(valid_passports))
