# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/

def firstPalindrome(self, words: list[str]) -> str:
    for i in range(len(words)):
        if words[i] == words[i][::-1]:
            return words[i]
    return ""