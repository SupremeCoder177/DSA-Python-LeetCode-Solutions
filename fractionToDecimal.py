# fractio to recurring decimal 

class Solution:

	def fractionToDecimal(self, numerator : int, denominator : int) -> str:
		temp = str(numerator / denominator)
		decimal_index = temp.index('.')

		check_length = 1
		last_highest_recurrence = ""
		last_highest_recurrence_index = 0

		while check_length < len(temp) - decimal_index:
			last_recurr = ""
			recurr_count = 0
			first_recurr_index = 0
			for i in range(decimal_index + 1, len(temp)):
				if temp[i: i + check_length] != last_recurr:
					last_recurr = temp[i: i + check_length]
					print(last_recurr)
					first_recurr_index = i
					recurr_count = 0
				else: recurr_count += 1
			if len(last_recurr) > len(last_highest_recurrence) and recurr_count > 1:
				last_highest_recurrence = last_recurr
				last_highest_recurrence_index = first_recurr_index
			check_length += 1

		if len(last_highest_recurrence) != 0:
			copy_str = str()
			for i in range(len(temp)):
				if i == last_highest_recurrence_index:
					copy_str += "("
				copy_str += temp[i]

				if i == last_highest_recurrence_index + len(last_highest_recurrence):
					copy_str += ")"
			temp = copy_str[:]

		return temp


print(Solution().fractionToDecimal(4, 333))