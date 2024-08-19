# https://leetcode.com/problems/reverse-string/description/

def reverseString(s: list[str]) -> None:
    for i in range(len(s)-1):
        save = s.pop(-1)
        s.insert(i,save)
