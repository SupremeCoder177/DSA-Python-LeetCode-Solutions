# removing duplicates from a sorted array of numbers

def removeDuplicates(nums : list[int]) -> int:
	temp = []
	for val in nums:
		if val not in temp: temp.append(val)
		else:
			nums.remove(val)
	return len(temp), temp

nums = [1, 1, 2]
print(removeDuplicates(nums))
print(nums)