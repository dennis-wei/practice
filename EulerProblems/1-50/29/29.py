exp_list = []

for a,b in [(a,b) for a in range(2, 101) for b in range(2, 101)]:
	if a**b not in exp_list:
		exp_list.append(a**b)

print len(exp_list)