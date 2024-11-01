# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        s = s.strip()
        n = ""
        for x in s:
            if x in alpha:
                n += x
        n = n.lower()
        return n == n[::-1]