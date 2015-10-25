def string_length(num):
	if num/100!=0:
		digit = num/100
		if digit == 1:
			cursum = len("onehundredand")
		elif digit == 2:
			cursum = len("twohundredand")
		elif digit == 3:
			cursum = len("threehundredand")
		elif digit == 4:
			cursum = len("fourhundredand")
		elif digit == 5:
			cursum = len("fivehundredand")
		elif digit == 6:
			cursum = len("sixhundredand")
		elif digit == 7:
			cursum = len("sevenhundredand")
		elif digit == 8:
			cursum = len("eighthundredand")
		elif digit == 9:
			cursum = len("ninehundredand")
		else:
			print "error: %d" % num
			return -1
		if num%100 == 0:
			return cursum - 3
		return string_length(num%100) + cursum
	if num/10 != 0:
		if num/10 == 1:
			if num == 10:
				cursum = len("ten")
			elif num == 11:
				cursum = len("eleven")
			elif num == 12:
				cursum = len("twelve")
			elif num == 13:
				cursum = len("thirteen")
			elif num == 14:
				cursum = len("fourteen")
			elif num == 15:
				cursum = len("fifteen")
			elif num == 16:
				cursum = len("sixteen")
			elif num == 17:
				cursum = len("seventeen")
			elif num == 18:
				cursum = len("eighteen")
			elif num == 19:
				cursum = len("nineteen")
			else:
				print "error: %d" % num
				return -1
			return cursum
		else:
			digit = num/10
			if digit == 2:
				cursum = len("twenty")
			elif digit == 3:
				cursum = len("thirty")
			elif digit == 4:
				cursum = len("forty")
			elif digit == 5:
				cursum = len("fifty")
			elif digit == 6:
				cursum = len("sixty")
			elif digit == 7:
				cursum = len("seventy")
			elif digit == 8:
				cursum = len("eighty")
			elif digit == 9:
				cursum = len("ninety")
			else:
				print "error: %d" % num
				return -1
			return string_length(num%10) + cursum
	if num/10 == 0:
		digit = num%10
		if digit == 0:
			cursum = 0
		elif digit == 1:
			cursum = len("one")
		elif digit == 2:
			cursum = len("two")
		elif digit == 3:
			cursum = len("three")
		elif digit == 4:
			cursum = len("four")
		elif digit == 5:
			cursum = len("five")
		elif digit == 6:
			cursum = len("six")
		elif digit == 7:
			cursum = len("seven")
		elif digit == 8:
			cursum = len("eight")
		elif digit == 9:
			cursum = len("nine")
		else:
			print "error: %d" % num
			return -1
		return cursum



sum = 0
for i in range (1, 1000):
	sum += string_length(i)
	print "%d has length %d" % (i, string_length(i))
sum += len("onethousand")

print sum