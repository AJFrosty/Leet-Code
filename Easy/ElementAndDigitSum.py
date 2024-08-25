# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/

class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        esum = 0
        dsum = 0

        for x in nums:
            esum += x
            stri = str(x)
            for i in range(len(stri)):
                dsum += int(stri[i])
        
        return abs(esum-dsum)