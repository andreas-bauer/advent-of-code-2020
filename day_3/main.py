lines = []
with open("input.txt") as f:
    lines = f.readlines()

width = 31

next_pos = 3
hit_trees = 0
line_counter = 2

def hit_symbol(char):
    if char == "#":
        return "X"
    return "O"

for line in lines[1:]:
    if line[next_pos] == '#':
        hit_trees += 1

    next_pos = (next_pos + 3) % width
    line_counter += 1
    
    symbol = hit_symbol(line[next_pos])
    hit_line = line[:next_pos] + symbol + line[next_pos + 1:]
    print(hit_line)

print("Hit trees on the way down: " + str(hit_trees))
