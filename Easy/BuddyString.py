# https://leetcode.com/problems/buddy-strings/description/

# NOT COMPLETED
def buddyStrings(s: str, goal: str) -> bool:
    # if s == goal:
    #     return False
    
    if len(s) != len(goal):
        return False
    sList = []
    gList = []

    for i in range(len(s)):
        sList.append(s[i])
        gList.append(goal[i])

    index = [0,1]
    ind = 0

    for i in range(len(s)):

        if s[i] == goal[i]:
            continue
        else:
            if ind > 1:
                return False
            index[ind] = i
            ind += 1
        

    sList[index[0]], sList[index[1]] = sList[index[1]], sList[index[0]]
    if sList == gList:
        return True
    return False

print(buddyStrings("aaaaaaabc","aaaaaaacb"))