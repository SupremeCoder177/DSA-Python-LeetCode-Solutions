# returning the first occurence of a sub-string in a string

def strStr(haystack : str, needle : str) -> int:
	for i in range(len(haystack)):
		if haystack[i:i + len(needle)] == needle:
			return i
	return -1

print(strStr("adbutsad", "sad"))
