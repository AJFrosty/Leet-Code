# https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        numlist = []
        for i in x:
            numlist += i
        return (numlist[::-1] == numlist)