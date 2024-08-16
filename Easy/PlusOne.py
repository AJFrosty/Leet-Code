# https://leetcode.com/problems/plus-one/description/

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits)):
            if digits[-(i+1)] != 9:
                digits[-(i+1)] += 1
                return digits
            digits[-(i+1)] = 0

            if digits[0] == 0:
                digits.insert(0,1)
        return digits
