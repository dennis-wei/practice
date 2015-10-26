chain = 0
chain_num = 0

for i in range(1, 1000000):
#	print i
	curr_chain = 1
	num = i
	while num!=1:
		if num%2==0:
			num/=2
		else:
			num = 3*num+1
		curr_chain+=1
#		print "    %d" % (num)
	if curr_chain>chain:
		chain = curr_chain
		chain_num = i
		print "%d has chain %d" % (chain_num, chain)