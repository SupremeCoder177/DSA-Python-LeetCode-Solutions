# longest comman prefix finder in a list of strings

def longestCommonPrefix(strs : list[str]) -> str:
	shotest_str_len = len(strs[0])
	pref = ""
	if len(strs) == 1 or len(strs[0]) == 0: return strs[0]
	else:
		for string in strs:
			if len(string) < shotest_str_len: shotest_str_len = len(string)
			if len(string) == 0: return ""
			if string[0] != strs[0][0]: return ""

	i = 0
	while i < shotest_str_len:
		curr = strs[0][i]
		for string in strs:
			if string[i] != curr:
				return pref
		pref += strs[0][i]
		i += 1
	return pref


print(longestCommonPrefix(["ab", "a"]))
	
		
