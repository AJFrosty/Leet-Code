# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sString = [x for x in s]
        tString = [z for z in t]

        if len(sString) != len(tString):
            return False
        
        for i in range(len(sString)):
            if sString[i] in tString:
                index = tString.index(sString[i])
                tString.pop(index)
            else:
                return False
        return True  