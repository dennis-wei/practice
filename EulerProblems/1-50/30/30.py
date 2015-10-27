def get_digits(n):
	num = n
	digit_list = []
	while num != 0:
		digit_list.append(num%10)
		num /= 10
	return digit_list

exp_list = []
for i in range (1, 10000000):
	lst = get_digits(i)
	digit_sum = 0
	for digit in lst:
		digit_sum += digit**5

	if digit_sum == i and len(lst) != 1:
		exp_list.append(i)
		print "num: %d" % (i)
		print "sum: %d" % (sum(exp_list))

print exp_list
print sum(exp_list)