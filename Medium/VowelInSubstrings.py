# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxi = 0
        for i in range(len(s)):
            if (i+k) > len(s):
                break
            sub = s[i:i+k]
            total = sub.count("a") + sub.count("e") + sub.count("i") + sub.count("o") + sub.count("u")
            if total > maxi:
                maxi = total
        return maxi
