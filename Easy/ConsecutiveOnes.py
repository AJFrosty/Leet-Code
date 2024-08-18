# https://leetcode.com/problems/max-consecutive-ones/description/

def findMaxConsecutiveOnes(nums: list[int]) -> int:
    count = 0
    tempCount = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            tempCount += 1
            if tempCount > count:
                count = tempCount
        else:
            tempCount = 0
    return count
