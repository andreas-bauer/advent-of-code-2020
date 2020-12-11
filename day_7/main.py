import re

input = open('input.txt', 'r').read().split("\n")

color_primary_re = re.compile(r"(.+?) bags")
contain_bags_re = re.compile(r"(\d) (\w+ \w+)")

graph = {}

for rule in input:
    match = color_primary_re.match(rule)
    color_primary = match.group(1)
    color_inside = contain_bags_re.findall(rule)
    if len(color_inside) > 0:
        graph[color_primary] = color_inside
    else:
        graph[color_primary] = [("0", "")]


def shiny_gold(color):
    if color == "shiny gold":
        return True
    elif color == "":
        return False
    else:
        return any(shiny_gold(child) for amount, child in graph[color])


shiny_gold_counter = sum(shiny_gold(color) for color in graph.keys()) - 1
print("Part 1: Number of bags that can contain a shiny gold bag: " +
      str(shiny_gold_counter))
