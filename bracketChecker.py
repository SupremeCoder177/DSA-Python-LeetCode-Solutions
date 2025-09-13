# is string closed by brackets checker

def isValid(s : str) -> bool:
	brack_map = {
	"[" : "]",
	"{" : "}",
	"(" : ")"
	}
	bracks = []
	for ch in s:
		if ch in brack_map: bracks.append(ch)
		if ch in brack_map.values():
			if len(bracks) == 0: return False
			if brack_map[bracks[len(bracks) - 1]] != ch:
				return False
			else:
				bracks.pop()

	if not bracks: return True
	else: return False


print(isValid("(Hello there{my name is this})"))