def moveZeroes(nums):
	"""
	:type nums: List[int]
	:rtype: void Do not return anything, modify nums in-place instead.
	"""

	end_index = len(nums)
	index = 0

	while index < end_index:
		if nums[index] == 0:
			nums.remove(0)
			nums.append(0)
			index -= 1
			end_index -= 1
		index += 1

list_ = [0]
print list_
moveZeroes(list_)
print list_