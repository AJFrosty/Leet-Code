# https://leetcode.com/problems/hand-of-straights/description/

def isNStraightHand(hand: list[int], groupSize: int) -> bool:
    
    if len(hand)%groupSize != 0:
        return False
    
    if groupSize == 1:
        return True
    
    final = []
    hand.sort()
    
    for i in range(len(hand)//groupSize):
        final.append([hand[i]])
        amt = hand[i]+1
        hand[i] = -1
        size = 1

        for j in range(len(hand)):
            
            if size == groupSize:
                break

            if amt in hand:
                index = hand.index(amt)
                final[i] += [hand[index]]
                hand[index] = -1
                size += 1
                amt += 1
            else:
                return False
            
    if sum(hand) != len(sum)*-1:
        return False     

    return final

print(isNStraightHand([1,2,3,6,2,3,4,7,8],3))