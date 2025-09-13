# longest valid parentheses substring

def longestValidParentheses(string : str) -> int:
	if len(string) == 0: return 0
	open_count = 0
	counts = []
	temp = 0
	for ch in string:
		if ch == "(":
			open_count += 1
		else:
			open_count -= 1
			temp += 2
	if open_count:
