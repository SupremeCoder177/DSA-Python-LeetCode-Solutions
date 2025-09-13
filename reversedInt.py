# reversing a 32 bit integer

def reverse(x : int) -> int:
	if x == 0: return 0
	return int(''.join(list(reversed(str(abs(x)))))) * int(x / abs(x)) if -2 ** 31 <= int(''.join(list(reversed(str(abs(x)))))) * int(x / abs(x)) <= 2 ** 31 - 1 else 0
	


print(reverse(-123))