# https://leetcode.com/problems/sort-array-by-parity/description/

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                save = nums.pop(i)
                nums.insert(0,save)
        return nums