import numpy as np

f = open ( 'input.txt' , 'r')
l = [ map(int,line.split(' ')) for line in f ]
npl = np.array(l)
maxNum = 0
for i in range(3, 23):
	for j in range(3, 23):
		row  = npl[i][j] * npl[i+1][j] * npl[i+2][j] * npl[i+3][j]
		column = npl[i][j] * npl[i][j+1] * npl[i][j+2] * npl[i][j+3]
		diagonal1 = npl[i][j] * npl[i+1][j+1] * npl[i+2][j+2] * npl[i+3][j+3]
		diagonal2 = npl[i][j] * npl[i+1][j-1] * npl[i+2][j-2] * npl[i+3][j-3]
		curMax = max(row, column, diagonal1, diagonal2)
		if maxNum < curMax:
			maxNum = curMax
			print(maxNum)
			print "%d %d %d" % (i-3, j-3, npl[i][j])
			print "%d %d %d %d" % (row, column, diagonal1, diagonal2)


print(maxNum)