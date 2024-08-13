# https://leetcode.com/problems/find-the-winner-of-an-array-game/description/

def getWinner(arr: list[int], k: int) -> int:
    wins = 0
    index = 1

    while wins != k:
        if index == len(arr) and wins == index:
            return arr[0]
        
        if index == len(arr):
            index = 1

        if arr[0] > arr[index]:
            wins += 1
            index += 1
        else:
            save = arr.pop(0)
            arr.append(save)
            wins = 1
            index = 1
    return arr[0]

print(getWinner([1,11,22,33,44,55,66,77,88,99],100))