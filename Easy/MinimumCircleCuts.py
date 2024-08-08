# https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/

class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n < 2 :
            return 0
        if n % 2 == 0:
            return n//2
        if n % 2 == 1:
            return n
        
    