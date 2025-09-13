# find missing postive integer

from typing import List

class Solution:

	def firstMissingPositive(self, nums : List[int]) -> int:

		curr_min = 1
		for num in sorted(nums):
			if num == curr_min:
				curr_min += 1

		return curr_min


print(Solution().firstMissingPositive([1000000, 3, 4000, 2, 15, 1, 99999]))
