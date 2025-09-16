# longest valid parentheses substring

class Solution:

	def check_parenthesis(self, s : str) -> bool:
		tmp = 0
		for ch in s:
			if ch == "(": tmp += 1
			else:
				tmp -= 1
				if tmp < 0: return False
		return tmp == 0

	def longestValidParentheses(self, s : str) -> int:
		if len(s) == 0 or len(s) == 1: return 0
			
		max_len = 0
		for i in range(len(s)):
			for j in range(1, len(s)):
				if self.check_parenthesis(s[i : j + 1]):
					if (j + 1) - i > max_len: max_len = (j + 1) - i
		return max_len


print(Solution().longestValidParentheses(")(())))(())())"))