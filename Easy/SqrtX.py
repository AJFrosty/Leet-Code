# https://leetcode.com/problems/sqrtx/description/

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        prod = 1

        while prod*prod < x:
            if (prod+1)*(prod+1) > x:
                break
            prod += 1

        return prod