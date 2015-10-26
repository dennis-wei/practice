import numpy as np

def construct_spiral(spiral, n):
	spiral[n/2][n/2] = 1
	cur_num = 2
	cur_step = 1
	i = n/2
	j = n/2
	while 0 in spiral:
		for k in range(1, cur_step + 1):
			i += 1
			if i > (len(spiral[0])-1):
				break
			spiral[j][i] = cur_num
			cur_num += 1
		for k in range(1, cur_step + 1):
			if i > (len(spiral[0])-1):
				break
			j += 1
			spiral[j][i] = cur_num
			cur_num += 1
		cur_step += 1

		for k in range(1, cur_step + 1):
			if i > (len(spiral[0])-1):
				break
			i -= 1
			spiral[j][i] = cur_num
			cur_num += 1
		for k in range(1, cur_step + 1):
			if i > (len(spiral[0])-1):
				break
			j -= 1
			spiral[j][i] = cur_num
			cur_num += 1
		cur_step += 1

	diag_sum = 0
	for k in range(0, len(spiral)):
		diag_sum += spiral[k][k]
		diag_sum += spiral[k][len(spiral)-k-1]

	return (diag_sum - spiral[n/2][n/2])

sp_mat = np.zeros((1001, 1001))
print(construct_spiral(sp_mat, 1001))