from itertools import combinations_with_replacement

def numSquares(n):
        """
        :type n: int
        :rtype: int
        """
        square_list = []
        generate_squares(square_list, n)
        
        count = 1
        while True:
            for combi in combinations_with_replacement(square_list, count):
                if sum(combi) == n:
                    print count
                    return
            count += 1
    
def generate_squares(list, n):
    index = 1
    while index**2 < n:
        list.append(index**2)
        index += 1
    
def find_sum(n, list_, count):
    min(list_, key=lambda x:abs(x-n))
    print key

numSquares(13)
numSquares(12)