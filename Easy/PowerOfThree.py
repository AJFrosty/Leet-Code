# https://leetcode.com/problems/power-of-three/description/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def powerOf(n):
            if n == 3:
                return True
            if n == 1:
                return True
            if n < 3:
                return False
            if n%3 == 0:
                n = n//3
                return powerOf(n)
            return False
        return powerOf(n)