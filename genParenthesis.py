# making a valid parenthesis program
# takes in an input of an int, and returns a string of n pairs of all possible valid parenthesis

from random import randint
from typing import List

class Solution:

	def generateParenthesis(self, n : int) -> List[str]:
		result = []

		def backtrack(curr : str, open_count : int, close_count : int):
			if open_count == 0 and close_count == 0:
				result.append(curr)
				return

			if open_count > 0:
				backtrack(curr + "(", open_count - 1, close_count)

			if close_count > open_count:
				backtrack(curr + ")", open_count, close_count - 1)

		backtrack("", n, n)
		return result

print(Solution().generateParenthesis(3))

