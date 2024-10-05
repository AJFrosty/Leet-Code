# https://leetcode.com/problems/the-kth-factor-of-n/description/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = [1,n]

        for i in range(2,(n//2)+1):
            if n%i == 0:
                factors.append(i)
        
        factors.sort()

        if k > len(factors):
            return -1
        return factors[k-1]