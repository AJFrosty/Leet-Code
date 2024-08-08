# https://leetcode.com/problems/reverse-words-in-a-string

class Solution:
    def reverseWords(self, s: str) -> str:
        content = s.strip().split(" ")
        content2 = [content[i].strip() for i in range(len(content)-1,-1,-1) ]
        output = []
        for x in content2:
            if len(x.strip()) >0:
                print(x)
                output.append(x)

        return " ".join(output)
        