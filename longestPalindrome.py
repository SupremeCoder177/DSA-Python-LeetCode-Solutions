# returning the longest palindrome from a string

# def longestPalindrome(string):
# 	curr_max_len = string[0] if len(string) != 0 else ""
# 	for i in range(len(string)):
# 		j = 0
# 		while j < len(string):
# 			if i == j: 
# 				j += 1
# 				continue
# 			if i > j:
# 				if string[j:i + 1] == ''.join(reversed(string[j:i + 1])) and len(string[j:i + 1]) > len(curr_max_len):
# 					curr_max_len = string[j:i + 1]
# 			else:
# 				if string[i:j + 1] == ''.join(reversed(string[i:j + 1])) and len(string[i:j + 1]) > len(curr_max_len):
# 					curr_max_len = string[i:j + 1]
# 			j += 1
# 	return curr_max_len



def longestPalindrome(string : str) -> str:
	if len(string) == 1: return string
	curr_max_len = ""
	sub_section_sample_size = 2
	palindromes_found = [string[0]]
	r_string = ''.join(list(reversed(string)))
	while sub_section_sample_size <= len(string):
		temp = palindromes_found.copy() if palindromes_found else temp
		palindromes_found.clear()
		for i in range(len(string)):
			if string[i:i + sub_section_sample_size] == r_string[len(string) - (i + sub_section_sample_size):len(string) - i]:
				palindromes_found.append(string[i:i + sub_section_sample_size])
		sub_section_sample_size += 1
		curr_max_len = palindromes_found[0] if palindromes_found else temp[0]
	return curr_max_len




print(longestPalindrome("ac"))