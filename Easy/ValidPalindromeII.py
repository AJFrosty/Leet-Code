# https://leetcode.com/problems/valid-palindrome-ii/

def validPalindrome(s: str) -> bool:
    letters = list(s)
    
    for x in range(len(letters)):
        if (letters[x] != letters[-(1+x)]):
            index = x
            save = letters.pop(x)
            if letters == letters[::-1]:
                return True
            else:
                letters.insert(index,save)
                letters.pop(-(1+x))
                if letters == letters[::-1]:
                    return True
                else:
                    return False
    return True

print(validPalindrome("aba"))