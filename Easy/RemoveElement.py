# https://leetcode.com/problems/remove-element

class Solution(object):
    def removeElement(self, nums, val):
        count = 0
        new = []
        for i in range(len(nums)):
            if nums[i] != val:
                new.append(nums[i])
                count += 1

        for i in range(len(nums)):
            if i < (len(new)):
                nums[i] = new[i]
        
        return count

        