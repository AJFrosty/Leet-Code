# https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num: int) -> int:
        final = ""
        #negative nums
        if num < 0:
            num = -num
            count = len(str(num))
            array = [int(str(num)[i]) for i in range(count)]
            array.sort(reverse=True)
            array[0] = -array[0]
            for i in range(len(array)):
                final += str(array[i])
            return int(final)
        
        # positive nums
        count = len(str(num))
        array = [int(str(num)[i]) for i in range(count)]
        array.sort()
        for i in range(len(array)):
            if array[0] == 0:
                if array[i] > 0:
                    array[0] = array[i]
                    array[i] = 0        
        for i in range(len(array)):
                final += str(array[i])
        return int(final)