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

if isPalndrome(121):
	print "working"