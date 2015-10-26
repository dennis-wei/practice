import time

def get_divisors(n):
	mysum = 0
	for i in range(1, n):
		if n%i == 0:
			mysum += i
			if mysum>n:
				return 1
	return 0

def is_abun_sum(num, abun_nums):
	for j in abun_nums:
		if j>num:
			break
		if (i-j) in abun_nums:
			return True
	return False



start = time.time()

abun_nums = []
for i in range (1, 28123):
	if get_divisors(i) > 0:
		abun_nums.append(i)
print abun_nums

remain_nums = []
for i in range(1, 28123):
	if is_abun_sum(i, abun_nums) == False:
		remain_nums.append(i)
		print "Added: %d" % (i)

	

ellapsed = time.time() - start

print sum(remain_nums)
print "Found in %d seconds" % (ellapsed)