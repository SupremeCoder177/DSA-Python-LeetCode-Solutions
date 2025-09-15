# group anagrams

from typing import List

class Solution:

	def groupAnagrams(self, strs : List[str]) -> List[List[str]]:
		anagrams = dict()
		for word in strs:
			chars = []
			for ch in word:
				chars.append(ch)
			chars = tuple(sorted(chars))
			
			if chars in anagrams:
				anagrams[chars].append(word)
			else:
				anagrams[chars] = [word]
				
		output = []
		for val in anagrams.values():
			output.append(val)
		return output


print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

