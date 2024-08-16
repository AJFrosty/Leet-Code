# https://leetcode.com/problems/make-number-of-distinct-characters-equal/

def isItPossible(word1: str, word2: str) -> bool:
        first = ["" for x in word1]
        second = ["" for y in word2]

        word1List = [x for x in word1]
        word2List = [y for y in word2]

        firstUnique = []
        secondUnique = []

        firstIndex = 0
        secondIndex = 0

        count = 0
        for x in word1:
            if x not in firstUnique:
                firstUnique.append(x)
                count += 1
            else:
                first[count] = x
                firstIndex = count
                count += 1
                break
        
        count = 0
        for x in word2:
            if x not in secondUnique:
                secondUnique.append(x)
                count += 1
            else:
                second[count] = x
                secondIndex = count
                count += 1
                break

        if len(firstUnique) == len(word2List) and len(secondUnique) == len(word1List):
            return True
        
        firstUnique = []
        secondUnique = []

        entry1 = word2List[secondIndex]
        entry2 = word1List[firstIndex]
        word1List[firstIndex] = entry1
        word2List[secondIndex] = entry2

        for i in range(len(word1List)):
            if word1List[i] not in firstUnique:
                firstUnique.append(word1List[i])
        
        for i in range(len(word2List)):
            if word2List[i] not in secondUnique:
                secondUnique.append(word2List[i])

        if len(firstUnique) == len(secondUnique):
            return True
        else:
            return False 


print(isItPossible("aab", "bccd"))