# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

class Solution:
    def minimumSum(self, num: int) -> int:
        sNums =  [int(i) for i in str(num)]
        newList = []
        while len(sNums) > 0 : 
            min = 9
            max = 0
            index = 0
            mindex = 0
            for i in range(len(sNums)):
                if min > sNums[i]:
                    min = sNums[i]
                    index = i
            sNums.pop(index)
            for i in range(len(sNums)):
                if max < sNums[i]:
                    max = sNums[i]
                    mindex = i
            sNums.pop(mindex)
            newList.append(int(str(min) + str(max)))
        return newList[0] + newList[1] 