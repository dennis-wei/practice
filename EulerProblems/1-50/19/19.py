def count_days(start_year, end_year, init_mod):
	mod = init_mod
	num_sundays = 0
	for year in range(start_year, end_year+1):

		# January
		if(mod == 0):
			num_sundays += 1
			print "Sunday on January 1st, %d" % (year)
		mod = (mod + 31) % 7

		# February
		if(mod == 0):
			num_sundays += 1
			print "Sunday on February 1st, %d" % (year)
		if(is_leap_year(year)):
			mod = (mod + 29) % 7
		else:
			mod = (mod + 28) % 7

		# March
		if(mod == 0):
			num_sundays += 1
			print "Sunday on March 1st, %d" % (year)
		mod = (mod + 31) % 7

		# April
		if(mod == 0):
			num_sundays += 1
			print "Sunday on April 1st, %d" % (year)
		mod = (mod + 30) % 7

		# May
		if(mod == 0):
			num_sundays += 1
			print "Sunday on May 1st, %d" % (year)
		mod = (mod + 31) % 7

		# June
		if(mod == 0):
			num_sundays += 1
			print "Sunday on June 1st, %d" % (year)
		mod = (mod + 30) % 7

		# July
		if(mod == 0):
			num_sundays += 1
			print "Sunday on July 1st, %d" % (year)
		mod = (mod + 31) % 7

		# August
		if(mod == 0):
			num_sundays += 1
			print "Sunday on August 1st, %d" % (year)
		mod = (mod + 31) % 7

		# September
		if(mod == 0):
			num_sundays += 1
			print "Sunday on September 1st, %d" % (year)
		mod = (mod + 30) % 7

		# October
		if(mod == 0):
			num_sundays += 1
			print "Sunday on October 1st, %d" % (year)
		mod = (mod + 31) % 7

		#November
		if(mod == 0):
			num_sundays += 1
			print "Sunday on November 1st, %d" % (year)
		mod = (mod + 30) % 7

		#December
		if(mod == 0):
			num_sundays += 1
			print "Sunday on December 1st, %d" % (year)
		mod = (mod + 31) % 7

	return num_sundays

def is_leap_year(year):
	if(year % 4 == 0):
		if(year % 100 == 0):
			if (year % 400 == 0):
				return True
			else:
				return False
		else:
			return True
	else:
		return False

print(count_days(1901, 2000, 2))