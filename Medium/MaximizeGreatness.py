# https://leetcode.com/problems/maximize-greatness-of-an-array/description/
#INCOMPLETE
def maximizeGreatness(nums: list[int]) -> int:
        perm = [0 for x in range(len(nums))]
        hold = sorted(nums)
        count = 0
        passes = 0
        x = 0
        y = 0
        
        while passes < len(nums):
            for i in range(len(hold)):
                if hold[i] > nums[passes]:
                    perm[passes] = hold[i]
                    count += 1
                    hold.pop(i)
                    break
            passes +=1
            
        return count

print(maximizeGreatness([42,8,75,28,35,21,13,21]))