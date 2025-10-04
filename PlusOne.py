from typing import List


class Solution:

    def recusiveAddOne(self, digits : List[int], index : int) -> List[int]:
        if digits[index] != 9:
            digits[index] += 1
            return digits
        else:
            if index != 0:
                digits[index] = 0
                return self.recusiveAddOne(digits, index - 1)
            else:
                digits[index] = 0
                digits.insert(0, 1)
                return digits

    def plusOne(self, digits : List[int]) -> List[int]:
        return self.recusiveAddOne(digits, len(digits) - 1)
    


temp = [9]
temp = Solution().plusOne(temp)

for i in temp:
    print(i, end = "")
print()
