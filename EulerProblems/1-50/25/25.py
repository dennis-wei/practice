import time

def get_num_digits(n):
	num = n
	digits = 0
	while num != 0:
		num /= 10
		digits += 1
	return digits

start = time.time()

index = 2
num1 = 1
num2 = 1
num_digits = 0
while num_digits<1000:
	tmp = num2
	num2 = num1 + num2
	num1 = tmp
	index += 1
	num_digits = get_num_digits(num2)

ellapsed = time.time() - start

print index
print "Found in %d seconds" % (ellapsed)