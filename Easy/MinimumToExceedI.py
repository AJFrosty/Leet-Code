# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/description/

class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] < k:
                count += 1
        return count