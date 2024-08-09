# https://leetcode.com/problems/count-the-number-of-fair-pairs/

class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        
        for i in range(n):
            left = i + 1
            right = n
            
            while left < right:
                mid = (left + right) // 2
                if nums[i] + nums[mid] < lower:
                    left = mid + 1
                else:
                    right = mid
            
            start = left
            left = i + 1
            right = n
            
            while left < right:
                mid = (left + right) // 2
                if nums[i] + nums[mid] > upper:
                    right = mid
                else:
                    left = mid + 1
            
            end = left   
            count += end - start
        
        return count