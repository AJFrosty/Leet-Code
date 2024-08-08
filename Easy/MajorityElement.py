# https://leetcode.com/problems/majority-element

class Solution(object):
    def majorityElement(self, nums):
        unique = []
        max = 0
        for i in range(len(nums)):
            if nums[i] not in unique:
                unique.append(nums[i])
        for i in range(len(unique)):
            count = 0
            for j in range(len(nums)):
                if unique[i] == nums[j]:
                    count += 1
            unique[i] = [unique[i],count]

        for i in range(len(unique)):
            if unique[i][1] >= unique[max][1]:
                max = i

        return unique[max][0]
        