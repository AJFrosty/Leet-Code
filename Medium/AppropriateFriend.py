# https://leetcode.com/problems/friends-of-appropriate-ages/description/
# NOT COMPLETED

def numFriendRequests(ages: list[int]) -> int:
    ages.sort()
    count = 0
    front = 0
    back = len(ages)-1

    while front < back:
        if front == back:
            if back == ((len(ages)-1)-(len(ages)-2)):
                break
            front = 0
            back -= 1
    
        else:
            if ages[front] <= 0.5*ages[back]+7 or ages[front]>ages[back] or (ages[front] >100 and ages[back] <100):
                front += 1
            elif ages[front] == ages[back]:
                count += 2
                front += 1
            else:
                count += 1
                front += 1

    return count

print(numFriendRequests([20,30,100,110,120]))