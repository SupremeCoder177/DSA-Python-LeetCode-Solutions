# median of two sorted arrays

from math import ceil

def findMedianSortedArrays(num1 : list[int], num2 : list[int]) -> float:
	num1.extend(num2)
	if len(num1) % 2 == 0:
		return num1[(len(num1) - 1) // 2] + num1[ceil((len(num1) - 1) / 2)] / 2
	else:
		return num1[(len(num1) // 2)]


print(findMedianSortedArrays([1, 3], [2]))