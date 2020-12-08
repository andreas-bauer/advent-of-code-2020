groups = []
for line in open('input.txt', 'r').read().split('\n\n'):
    answers = line.split('\n')
    groups.append(answers)

# Part 1
yes_in_group = []
for group in groups:
    yes_answ = set()
    for answers in group:
        for a in answers:
            yes_answ.add(a)
    yes_in_group.append(len(yes_answ))

print("Solution part 1: "+str(sum(yes_in_group)))

# Part 2
yes_per_group = []
for group in groups:
    yes_answ_group = [0]*27
    for answers in group:
        for a in answers:
            yes_answ_group[ord(a) - ord("a")] += 1
    all_yes = list(filter(lambda x: x == len(group), yes_answ_group))
    yes_per_group.append(len(all_yes))

print("Solution part 2: "+str(sum(yes_per_group)))
