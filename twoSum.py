# two-sum

# my solution
# apparently the "in" operator for a list is O(n) but O(1) for dicts
def twoSum(nums : list[int], target : int) -> list[int]:
	for i in range(len(nums)):
		if target - nums[i] in nums:
			if nums.index(target - nums[i]) != i:
				return [i, nums.index(target - nums[i])]


# chatGpt solution using hashmaps
def twoSum(nums : list[int], target : int) -> list[int]:
	num_map = {}

	for i, num in enumerate(nums):
		complement = target - num
		if complement in num_map and num_map[complement] != i:
			return [i, num_map[complement]]

		num_map[num] = i


