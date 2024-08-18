# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/

class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        order = [i for i in range(len(mat))]
        minIndex = 0
        index=0
        switches = 0
        for i in range(len(mat)):
            if switches == k:
                return order[:k]
            min = mat[i].count(1)
            index=i
            for j in range(i,len(mat)):
                if mat[j].count(1) < min:
                    min = mat[j].count(1)
                    index = j
                if mat[j].count(1) == min and order[index] > order[j]:
                    min = mat[j].count(1)
                    index = j
            if index != 0:
                order[minIndex], order[index] = order[index], order[minIndex]
                mat[minIndex], mat[index] = mat[index], mat[minIndex]
            minIndex = i+1
            switches += 1
        return order[:k]