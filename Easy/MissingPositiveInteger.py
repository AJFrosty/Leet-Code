# https://leetcode.com/problems/kth-missing-positive-number/description/

class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        larg = max(arr)
        largArr = [i for i in range(1,larg+1)]

        for i in range(larg):
            if largArr[i] in arr:
                largArr[i] = 0
        
        final = [x for x in largArr if x != 0]

        if len(final) == 0:
            return larg+k

        if len(final) < k:
            get = k-len(final)
            return larg+get
        
        return final[k-1]