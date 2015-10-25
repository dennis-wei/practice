import time as time
from operator import itemgetter, attrgetter, methodcaller

class DivPair(object):

	def __init__(self, num, div_sum):
		self.num = num
		self.div_sum = div_sum

class AmiPair(object):

	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2

def get_divisors(n):
	mysum = 0
	for i in range(1, n):
		if n%i == 0:
			mysum += i
	return mysum

def get_key(pair):
	return pair.divsum

start = time.time()

pair_list = []
div_list = []
for i in range(1, 10001):
	cur_div_sum = get_divisors(i)
	div_list.append(DivPair(i, cur_div_sum))
	for elem in div_list:
		if (elem.num == cur_div_sum) and (elem.div_sum == i) and (i!=elem.num):
			pair_list.append(AmiPair(elem.num, i))



ami_sum = 0
for pair in pair_list:
	print "(%d, %d)" % (pair.num1, pair.num2)
	ami_sum += (pair.num1 + pair.num2)

ellapsed = time.time() - start
print ami_sum
print "%s ellapsed" % ellapsed