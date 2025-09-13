# making a valid parenthesis program

def check_parenthesis(string):
	temp = 0
	for ch in string:
		if ch == "(": 
			temp += 1
		else:
			temp -= 1
			if temp < 0: return False
	return temp == 0

def generateParenthesis(n : int) -> list[str]:
	if n == 1: return ["()"]
	if n == 0: return []
	open_count = close_count = n

generateParenthesis(3)