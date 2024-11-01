# https://leetcode.com/problems/power-of-two/description/?envType=problem-list-v2&envId=math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        final = []
        while n > 0:
            final.append(n%2)
            n //=2
        if final.count(1) == 1:
            return True
        return False
    
