def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    matrix = [[0 for x in xrange(n)] for y in xrange(n)]
        
    construct_ring(0, 0, 1, n, matrix)
    
    myprint(matrix)   
    return matrix
        
def construct_ring(start_row, start_column, start_n, size, matrix):
    if size >= 0:
        curr_row = start_row
        curr_column = start_column
        curr_n = start_n

        for i in range(0, size):
            matrix[curr_row][curr_column] = curr_n
            curr_column += 1
            curr_n += 1
        curr_column -= 1
        curr_row += 1

        for i in range(0, size - 1):
            matrix[curr_row][curr_column] = curr_n
            curr_row += 1
            curr_n += 1
        curr_row -= 1
        curr_column -= 1

        for i in range(0, size - 1):
            matrix[curr_row][curr_column] = curr_n
            curr_column -= 1
            curr_n += 1
        curr_column += 1
        curr_row -= 1

        for i in range(0, size - 2):
            matrix[curr_row][curr_column] = curr_n
            curr_row -= 1
            curr_n += 1
        
        myprint(matrix)
        construct_ring(curr_row+1, curr_column + 1, curr_n, size - 2, matrix)

def myprint(matrix):
	for row in matrix:
		print row
		print

generateMatrix(0)
generateMatrix(5)
generateMatrix(10)