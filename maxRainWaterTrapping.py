# trapping rain water

from typing import List


class Solution:

	def trap(self, height : List[int]) -> int:
		trapped = 0
		for i in range(len(height) - 1):
			if i == 0 and height[i] == 0: continue
			if i == len(height) - 1 and height[i + 1] == 0: continue
			print(trapped)
			trapped +=  max(height[i], height[i + 1]) - min(height[i], height[i + 1])

		return trapped



print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
