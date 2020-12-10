import re

input = open('input.txt', 'r').read().split("\n")

first_color_re = re.compile(r"(\w+ \w+) bags contain")
contain_bags_re = re.compile(r"(\d) (\w+ \w+)")

noBags = lambda r: r.endswith("no other bags.")

bags = {}

for rule in input:
    match = first_color_re.match(rule)
    color = match.group(1)
    dep_matches = contain_bags_re.findall(rule)
    bags[color] = dep_matches

count_shiny_gold = 0
contains_shiny_gold = []
for bag in bags:
    for content in bags[bag]:
        color = content[1]
        if color == "shiny gold":
            contains_shiny_gold.append(bag)

for bag in bags:
    for content in bags[bag]:
        color = content[1]
        if color in contains_shiny_gold:
            count_shiny_gold += 1

print(str(count_shiny_gold))