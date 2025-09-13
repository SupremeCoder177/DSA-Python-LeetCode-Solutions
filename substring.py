# substring

def lengthOfLongestSubstring(string : str) -> int:
	if not string:  return 0
	if len(string) == 1: return 1

	output = 0
	char_map = {}
	min_dupe = 0
	max_dupe = 0
	second_max_dupe = 0
	first_dupe = False
	for i in range(len(string)):
		if string[i] not in char_map: 
			char_map[string[i]] = {"occurence" : 1, "indexs" : [i]}
		else:
			char_map[string[i]]["occurence"] += 1
			temp = char_map[string[i]]["indexs"]
			temp.append(i)
			char_map[string[i]]["indexs"] = temp

	for info in char_map.values():
		if info["occurence"] > 1:
			min_dupe =  min(info["indexs"]) if not first_dupe else min(min_dupe, min(info["indexs"]))
			max_dupe = max(max_dupe, max(info["indexs"]))
			for ind in info["indexs"]: second_max_dupe = max(second_max_dupe, ind if ind < max_dupe else 0)
			first_dupe = True

	if min_dupe != 0:
		output = max(output, len(string) - min_dupe)		

	if max_dupe != len(string) - 1:
		output = max(output, len(string) - max_dupe)

	duplicates = False
	for char in char_map:
		if char_map[char]["occurence"] > 1:
			duplicates = True
			for i in range(len(char_map[char]["indexs"])):
				temp = char_map[char]["indexs"][i] - char_map[char]["indexs"][max(0, i - 1)]
				if char_map[char]["indexs"][i] == max_dupe and max_dupe == len(string) - 1:
					temp = max_dupe - second_max_dupe + 1
				output = max(output, temp)

	if not duplicates: output = len(string)
	return output if char_map else 0
	

print(lengthOfLongestSubstring("abcba"))