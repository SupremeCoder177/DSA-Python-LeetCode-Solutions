# implementing a cusine system of foodratings

from typing import List

class FoodRatings:

	def __init__(self, foods : List[str], cuisines : List[str], ratings : List[int]):
		self.ratings = dict()
		self.categories = dict()

		for cuisine in cuisines:
			if cuisine not in self.categories:
				self.categories[cuisine] = list()

		for i in range(len(cuisines)):
			self.categories[cuisines[i]].append(foods[i])
			self.ratings[foods[i]] = ratings[i]

	def changeRating(self, food : str, newRating : int) -> None:
		self.ratings[food] = newRating

	def highestRated(self, cuisine : str) -> str:
		max_rating = 0
		index = 0
		for i in range(len(self.categories[cuisine])):
			if self.ratings[self.categories[cuisine][i]] > max_rating:
				max_rating = self.ratings[self.categories[cuisine][i]]
				index = i
			elif self.ratings[self.categories[cuisine][i]] == max_rating:
				if self.categories[cuisine][i] < self.categories[cuisine][index]:
					index = i
		return self.categories[cuisine][index]


food_ratings = FoodRatings(['kimchi', 'miso', 'sushi', 'moussaka', 'ramen', 'bulgogi'], ['korean', 'japanese', 'japanese', 'greek', 'japanese', 'korean'], [9, 12, 8, 15, 14, 7])
print(food_ratings.highestRated('japanese'))
food_ratings.changeRating('sushi', 11)
print(food_ratings.highestRated("japanese"))