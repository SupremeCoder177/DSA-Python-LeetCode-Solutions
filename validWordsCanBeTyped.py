# maximum no. of words you can type

class Solution:
	
	def canBeTypedWords(self, text : str, brokenLetter : str) -> int:
		words = text.split(' ')
		output = 0
		for word in words:
			valid = True
			for ch in word.lower():
				if ch in brokenLetter.lower():
					valid = False
					break
			if valid: output += 1
		return output


print(Solution().canBeTypedWords("Hello there my name is Something", "h"))	