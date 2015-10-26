import math as math

def getTriNum(i):
	return i*(i+1)/2

def isPrime(n):
	for i in range (2, int(math.floor(math.sqrt(n)+1))):
		if n%i==0:
			return 0
	return 1

def getDiv(n):
	myfactors = []
	mycounts = []
	num = n
	j=2
	primecount = 0
	while(num!=1):
		if isPrime(j):
			primecount+=1
			if num%j == 0:
				numCount = myfactors.count(j)
				if numCount!=0:
					index = myfactors.index(j)
				else:
					index = -1

				if index != -1:
					mycounts[index] += 1
				else:
					myfactors.append(j)
					mycounts.append(1)

				num/=j
				j=1
		
		j+=1
	
	numDiv = 1
	for elem in mycounts:
		numDiv *= (elem+1)

	return numDiv

numDiv = 1
i = 1

while(numDiv<500):
	print "Testing: %d" % (i)
	n = getTriNum(i)
	print "    Num: %d" % (n)
	numDiv = getDiv(n)
	print "    Div: %d" % (numDiv)
	i += 1
