class Solution:
    def twoEditWords(self, queries: list[str], dictionary: list[str]) -> list[str]:
        final = []
        
        for i in range(len(queries)):
            for j in range(len(dictionary)):
                count = 0
                for k in range(len(queries[0])):
                    q = queries[i][k]
                    d = dictionary[j][k]
                    if queries[i][k] != dictionary[j][k]:
                        count += 1
                    if count > 2:
                        break
                if count <= 2:
                    final.append(queries[i])
                    break
        
        return final