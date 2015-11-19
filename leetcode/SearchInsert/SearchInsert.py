def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.append(target)
        index = 0
        
        if target < nums[0]:
            return 0
        
        while index < len(nums):
            if nums[index] == target:
                return index
            elif nums[index+1] > target:
                return index+1
            index += 1
            print index
        
        return index

num_list = [1, 3, 5, 6]
print "final: %d" % (searchInsert(num_list, 5))
print "\n"
num_list = [1, 3, 5, 6]
print "final: %d" % (searchInsert(num_list, 0))
print "\n"
num_list = [1, 3, 5, 6]
print "final: %d" % (searchInsert(num_list, 7))
print "\n"
num_list = [1, 3, 5, 6]
print "final: %d" % (searchInsert(num_list, 4))