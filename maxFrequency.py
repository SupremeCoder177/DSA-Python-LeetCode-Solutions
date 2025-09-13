class Solution:

	def maxFreqSum(self, s : str) -> int:
		vowels = ['a', 'e', 'i', 'o', 'u']
		consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
		vowel_freq = [0 for _ in range(5)]
		consonat_freq = [0 for _ in range(21)]

		for ch in s:
			if ch in vowels:
				vowel_freq[vowels.index(ch)] += 1
			else:
				consonat_freq[consonants.index(ch)] += 1

		return max(vowel_freq) + max(consonat_freq)


print(Solution().maxFreqSum("successes"))