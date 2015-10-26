f = open ( 'input.txt' , 'r')
num_list = f.read().splitlines()

sum = 0
for num_str in num_list:
	sum += int(num_str)

print sum