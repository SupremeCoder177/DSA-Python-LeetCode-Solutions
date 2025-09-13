# palimdrome number checker

def isPalindrome(x : int) -> bool:
	return str(x) == ''.join(reversed(str(x)))


print(isPalindrome(121))