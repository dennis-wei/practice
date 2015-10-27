def isPalindrome(n):
	num = n
	digits = []
	while num != 0:
		digits.insert(0, num % 10)
		num /= 10
	for i in range(0, len(digits)/2):
		if digits[i] != digits[len(digits)-i-1]:
			return False
	return True

def isBinaryPalindrome(s):
	for i in range(0, len(s)/2):
		if s[i] != s[len(s)-i-1]:
			return False
	return True

def toBinary(n):
	s = bin(n)
	s = s[2:]
	return s

sum = 0
for i in range(1, 1000000):
	if isPalindrome(i) and isBinaryPalindrome(toBinary(i)):
		sum += i
print sum