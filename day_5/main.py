passes = []
with open("input.txt") as f:
    passes = f.readlines()

# Part 1
highest_seat_id = 0
for pas in passes:
    row_bin = pas[:7].replace("F", "0").replace("B", "1")
    row = int(row_bin, 2)

    col_bin = pas[7:].replace("L", "0").replace("R", "1")
    col = int(col_bin, 2)

    seat_id = row * 8 + col
    if seat_id > highest_seat_id:
        highest_seat_id = seat_id

print("Highest seat id: " + str(highest_seat_id))

# Part 2
plane = [[0 for i in range(8)] for j in range(128)]
for pas in passes:
    row_bin = pas[:7].replace("F", "0").replace("B", "1")
    row = int(row_bin, 2)

    col_bin = pas[7:].replace("L", "0").replace("R", "1")
    col = int(col_bin, 2)
    plane[row][col] = 1

your_seat_id = 0
for row in range(128):
    print(str(row) + "\t " + str(plane[row]))
    for col in range(8):
        if plane[row][col] == 0:
            if 0 < col < 8 and plane[row][col-1] == 1 and plane[row][col+1] == 1:
                your_seat_id = row * 8 + col

print("\nYour seat id is " + str(your_seat_id))
