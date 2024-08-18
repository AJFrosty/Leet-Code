# https://leetcode.com/problems/can-convert-string-in-k-moves/

def canConvertString(s: str, t: str, k: int) -> bool:
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    movesLeft = [i+1 for i in range(k)]
        
    if len(s) != len(t):
        return False
        
    for i in range(len(s)):
        if s[i] != t[i]:
            tIndex = letters.index(t[i])
            sIndex = letters.index(s[i])

            #This encompasses the wrap around as well!!!
            moves = ((tIndex - sIndex)+26) % 26

            if moves in movesLeft :
                movesLeft.remove(moves)
            elif (26 - moves) in movesLeft:
                movesLeft.remove(26 - moves)
            else:
                return False
    return True


print(canConvertString("mrqlqefo","fufvyvmf",46))