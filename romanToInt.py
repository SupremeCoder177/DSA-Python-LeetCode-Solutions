# roman to int converter

def romanToInt(s : str) -> int:
	roman_map = {
	"I" : 1,
	"V" : 5,
	"X" : 10,
	"L" : 50,
	"C" : 100,
	"D" : 500,
	"M" : 1000
	}
	valid_dec = {
	"I" : ["V", "X"],
	"X" : ["L", "C"],
	"C" : ["D", "M"]
	}

	output = 0
	s = s.upper()
	for i in range(len(s)):
		output += roman_map[s[i]]
		if i > 0:
			if roman_map[s[i - 1]] < roman_map[s[i]] and s[i] in valid_dec[s[i - 1]]:
				output -= 2 * roman_map[s[i - 1]]

	return output


print(romanToInt("MCMXCIV"))
