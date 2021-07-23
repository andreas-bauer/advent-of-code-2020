input = open('input.txt', 'r').read().split("\n")

preamble_length = 25

for i in range(preamble_length, len(input)):
	current = int(input[i])
	found = False
	for j in range(i - preamble_length, i):
		for k in range (j + 1, i):
			sum = int(input[j]) + int(input[k])
			if sum == current:
				found = True
				print(input[i] + " = " + input[j] + " + " + input[k])
	if not found:
		print("No match found for " + input[i])
		break
