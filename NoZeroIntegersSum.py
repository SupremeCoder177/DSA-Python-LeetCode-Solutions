# returning a list of 2 no-zero integers

class Solution:

	def getNoZeroInteger(self, num):
		temp = "1"
		while True:
			checked_temp = True
			checked_diff = True
			for ch in temp:
				if ch == "0":
					temp = str(int(temp) + 1)
					checked_temp = False
			if checked_temp:
				for ch in str(num - int(temp)):
					if ch == "0":
						temp = str(int(temp) + 1)
						checked_diff = False

			if checked_temp and checked_diff:
				return [int(temp), num - int(temp)]


print(Solution().getNoZeroInteger(1007))