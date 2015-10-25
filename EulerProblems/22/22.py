import shlex

f = open('input.txt')
string = f.readlines()
f.close()

names = sorted(string[0].split(','))

score_sum = 0
for i in range(0, len(names)):
	cumul_sum = 0
	for char in names[i]:
		if ord(char) != 34:
			cumul_sum += (ord(char)-64)
			print "char: %c | value: %d" % (char,ord(char)-64)
	score_sum += ((i+1) * cumul_sum)
	print i
	print cumul_sum

print score_sum
