# https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/

def numberOfRounds(loginTime: str, logoutTime: str) -> int:
    count = 0

    if int(loginTime[:2]) > int(logoutTime[:2]) or (int(loginTime[:2])-int(logoutTime[:2])>1) or (int(loginTime[:2]) == int(logoutTime[:2]) and (int(loginTime[-2:])>int(logoutTime[-2:])) ):
        hours = 24-int(loginTime[:2]) + int(logoutTime[:2])
    else:
        hours = int(logoutTime[:2]) - int(loginTime[:2])
    
    inMins = int(loginTime[-2:])
    if inMins % 15 != 0:
        inMins += (15 - inMins % 15)
    outMins = int(logoutTime[-2:]) - (int(logoutTime[-2:]) % 15)
    
    currentMins = inMins
    if currentMins == 60:
        currentMins = 0

    if inMins > outMins:
        hours -= 1
    count += hours*4
    while currentMins != outMins:
        count += 1
        currentMins += 15
        if currentMins == 60:
            currentMins = 0
    if count < 0:
        count = 0
    return count

print(numberOfRounds("00:01","00:00"))