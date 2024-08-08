# https://leetcode.com/problems/a-number-after-a-double-reversal/

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if len(str(num)) == 1 : 
            return True
        sNums =  [int(i) for i in str(num)]
        if sNums[-1] == 0:
            return False
        return True
