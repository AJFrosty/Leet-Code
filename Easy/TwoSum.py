# https://leetcode.com/problems/two-sum/

class Solution:
    def check(self,list,i,j,target):
        if list[i] + list[j] == target and (i != j):
            return True
        return False

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if self.check(nums,i,j,target):
                    return [i,j]
        