# https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = list(s)
        unique = set(letters)
        counter = []
        final = 0
        for x in unique:
            counter.append(letters.count(x))
        
        for y in range(len(counter)):
            curr = counter[y]//2
            final += curr*2
            counter[y] -= curr*2
        if 1 in counter:
                final += 1    

        return final