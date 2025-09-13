# see if text is plagiarised

from typing import List

class PlagiarismDetector:

	def __init__(self):
		pass

	def check_plagiarism_line(self, text1 : str, text2 : str) -> bool:
		self.ptr = 0

		words_similar = 0

		words_l1 = text1.split(' ')
		words_l2 = text2.split(' ')
		len1 = len(words_l1)
		len2 = len(words_l2)

		while self.ptr < min(len1, len2) - 1:

			chars_similar = 0
			for i in range(min(len(words_l1[self.ptr]), len(words_l2[self.ptr]))):
				if words_l1[self.ptr][i] == words_l2[self.ptr][i]: chars_similar += 1

			if chars_similar >= (min(len(words_l1[self.ptr]), len(words_l2[self.ptr])) // 3) * 2:
				words_similar += 1

			self.ptr += 1

		return words_similar >= (min(len1, len2) // 3) * 2	

	def check_plagiarism_paragraph(self, para1 : List[str], para2 : List[str]) -> bool:
		plagiarism_count = 0
		for i in range(min(len(para1), len(para2))):
			if self.check_plagiarism_line(para1[i], para2[i]): plagiarism_count += 1

		if plagiarism_count >= min(len(para1), len(para2)) // 2:
			return True
		else:
			return False



text1 = "The poem captures the fleeting beauty of autumn, where golden leaves drift silently to the ground, painting the earth in a tapestry of warmth before the cold silence of winter arrives. Each line reflects both nostalgia and inevitability, reminding the reader that even beauty must surrender to time. The poet’s imagery of trees shedding their crowns is not just about nature but also about letting go gracefully when change becomes unavoidable."
text2 = "The poem describes the fading charm of autumn, as yellow and orange leaves gently fall, covering the soil in a soft, colorful blanket before the chill of winter takes over. Through these verses, the reader senses both longing and acceptance, as the season’s splendor gives way to its end. By portraying trees losing their leaves, the poet subtly conveys that beauty must bow to the passage of time and that release can also carry dignity."

print(PlagiarismDetector().check_plagiarism_paragraph(text1.split('.'), text2.split('.')))