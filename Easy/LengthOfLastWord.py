# https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        return len(s[-1].strip())
        