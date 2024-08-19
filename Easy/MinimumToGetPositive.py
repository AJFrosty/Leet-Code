# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/description/

def minStartValue(nums: list[int]) -> int:
    valid = False
    count = 1
    startCount = 1

    while not valid:
        count = startCount
        for i in range(len(nums)):
            count += nums[i]
            if count < 1:
                break
        if count > 0:
            valid = True
        else:
            startCount += 1
    return startCount

print(minStartValue([-3,2,-3,4,2]))
