input = open('input.txt', 'r').read().split("\n")

preamble_length = 25
invalid = 0

for i in range(preamble_length, len(input)):
	current = int(input[i])
	found = False
	for j in range(i - preamble_length, i):
		for k in range (j + 1, i):
			sum = int(input[j]) + int(input[k])
			if sum == current:
				found = True
	if not found:
		invalid = int(input[i])
		print("No match found for " + input[i])
		break


def find_sequence(search):
	for i in range(0, len(input)) :
		sum_window = []
		sum = 0
		for k in range(i, len(input)):
			value = int(input[k])
			sum += value
			sum_window.append(value)
			if sum == search:
				return sum_window
			if sum > search:
				break

sequence = find_sequence(invalid)
min_val = min(sequence)
max_val = max(sequence)
print(sequence)
print("min = " + str(min_val))
print("max = " + str(max_val))
print("min + max = " + str(min_val + max_val))