# https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/description/

class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        n = 1
        for i in range(len(matrix)):
            if max(matrix[i]) > n:
                n = max(matrix[i])
        newMatrix = list(range(1, n + 1))
        column =[[] for _ in range(1, n + 1)]

        if n == 1 and len(matrix) > 1:
            return False
        
        if len(matrix) != n:
            return False
        
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                column[j].append(matrix[i][j])
                if newMatrix[j] in matrix[i]:
                    continue
                else:
                    return False
                
        for x in range(n-1):
            column[x] = set(column[x])
            if len(column[x]) != n:
                return False
        return True
        