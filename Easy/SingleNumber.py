# https://leetcode.com/problems/single-number/description/

def singleNumber(nums: list[int]) -> int:
    for i in range(len(nums)):
        ct = nums.count(nums[i])
        if ct == 1:
            return nums[i]
