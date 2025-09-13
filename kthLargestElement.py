# find kth largest element in array

from typing import List

class Solution:

	def findKthLargest(self, nums : List[int], k : int) -> int:
		count = 0
		temp = sorted(nums)
		return temp[len(temp) -  k]


print(Solution().findKthLargest([3, 2 ,3, 1, 2, 4, 5, 5, 6], 3))