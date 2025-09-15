# making a valid parenthesis program
# takes in an input of an int, and returns a string of n pairs of all possible valid parenthesis


class Soluton:

	def check_parenthesis(self, string):
		temp = 0
		for ch in string:
			if ch == "(": 
				temp += 1
			else:
				temp -= 1
				if temp < 0: return False
		return temp == 0

	def genSingleParen(self) -> str:
		pass

	def generateParenthesis(self, n : int) -> list[str]:
		if n == 0: return []
		if n == 1: return ["()"]

		possibles = []

		for i in range(2 ** n):
			temp = self.genSingleParen()
			if check_parenthesis(temp): possibles.append(temp)
		return possibles



