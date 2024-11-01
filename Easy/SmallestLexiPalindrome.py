# https://leetcode.com/problems/lexicographically-smallest-palindrome/description/

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        letters = list(s)
        
        for x in range(len(letters)):
            if (letters[x] != letters[-(1+x)]):
                if letters[x] < letters[-(1+x)]:
                    letters[-(1+x)] = letters[x]
                else:
                    letters[x] = letters[-(1+x)]
        return "".join(letters)