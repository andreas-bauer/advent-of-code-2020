input = open('input.txt', 'r').read().split("\n")

accumulator = 0
pointer = 0
history = []

while pointer not in history:
	history.append(pointer)
	cmd = input[pointer].split()[0]
	arg = input[pointer].split()[1]

	print("["+str(pointer)+"] " + input[pointer])
	if cmd == "acc":
		accumulator += int(arg)
		pointer += 1
	if cmd == "jmp":
		pointer += int(arg)
	if cmd == "nop":
		pointer += 1
	print("ACC: " + str(accumulator))

print("***\nLast accumulator value: " + str(accumulator))