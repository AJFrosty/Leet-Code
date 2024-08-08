# https://leetcode.com/problems/jump-game/submissions/

class Solution(object):
    def canJump(self, nums):
        furthest = 0
        max = len(nums) - 1

        if max == 0:
            return True

        if nums[0] == 0:
            return False
            
        for i in range(len(nums)-1):
            if i > furthest:
                return False
            
            if nums[i] + i >= furthest:
                furthest = nums[i] + i

            if furthest >= max:
                return True
        return False
    

    