def candy(ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """
    if len(ratings) == 0:
        return 0

    print ratings
    max_index = ratings.index(max(ratings))
    print "Max Index: %d" % (max_index)
        
    depth = get_max_depth(ratings, max_index) + 1
    print "Depth: %d" % (depth)

    candy_dist = [0]*len(ratings)
    candy_dist[max_index] = depth
    curr_dist = depth
    for i in range (max_index+1, len(ratings)):
        if()
    
def get_max_depth(ratings, start_index):
    return max(get_left_depth(ratings, start_index), get_right_depth(ratings, start_index))
    
def get_left_depth(ratings, start_index):
    curr_depth = 0
    max_depth = 0
    curr_rate = ratings[start_index]
    for i in range(start_index, -1, -1):
        if ratings[i] < curr_rate:
            curr_depth += 1
            if curr_depth > max_depth:
                max_depth = curr_depth
            curr_rate = ratings[i]
            print "curr_depth: %d" % (curr_depth)
            print "max_depth: %d" % (max_depth)
        if ratings [i] > curr_rate:
            curr_depth -= 1
            curr_rate = ratings[i]
            print "curr_depth: %d" % (curr_depth)
    print "final left max_depth: %d" % (max_depth)
    return max_depth
    
def get_right_depth(ratings, start_index):
    curr_depth = 0
    max_depth = 0
    curr_rate = ratings[start_index]
    for i in range(start_index, len(ratings)):
        if ratings[i] < curr_rate:
            curr_depth += 1
            if curr_depth > max_depth:
                max_depth = curr_depth
            curr_rate = ratings[i]
            print "curr_depth: %d" % (curr_depth)
            print "max_depth: %d" % (max_depth)
        if ratings [i] > curr_rate:
            curr_depth -= 1
            curr_rate = ratings[i]
            print "curr_depth: %d" % (curr_depth)
    print "final right max_depth: %d" % (max_depth)
    return max_depth

# candy([5, 4, 3, 2, 1])
# candy([])
candy([1, 3, 2, 5, 4])
# candy([1, 2, 3, 4, 5])