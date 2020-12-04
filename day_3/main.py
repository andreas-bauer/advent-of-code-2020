lines = []
with open("input.txt") as f:
    lines = f.readlines()

width = 31

def calc_hits(right_steps, down_steps, lines):
    right_pos = right_steps
    down_pos = down_steps
    trees_hit = 0
    while down_pos < len(lines):
        if lines[down_pos][right_pos] == '#':
            trees_hit += 1

        down_pos += down_steps
        right_pos = (right_pos + right_steps) % width

    return trees_hit

print("Hit trees on the way down (1 right, 1 down): " + str(calc_hits(1, 1, lines)))
print("Hit trees on the way down (3 right, 1 down): " + str(calc_hits(3, 1, lines)))
print("Hit trees on the way down (5 right, 1 down): " + str(calc_hits(5, 1, lines)))
print("Hit trees on the way down (7 right, 1 down): " + str(calc_hits(7, 1, lines)))
print("Hit trees on the way down (1 right, 2 down): " + str(calc_hits(1, 2, lines)))
