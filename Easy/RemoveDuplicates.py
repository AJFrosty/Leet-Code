# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums):
        count = 0
        new = []
        for i in range(len(nums)):
            if nums[i] not in new:
                new.append(nums[i])
                count += 1

        for i in range(len(nums)):
            if i < (len(new)):
                nums[i] = new[i]
        return count

        