# https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/description/

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        increment = 0
        for i in range(len(nums)-1):
            if nums[i+1] <= nums[i]:
                increment += (nums[i]-nums[i+1])+1
                nums[i+1] += (nums[i]-nums[i+1])+1
        return increment