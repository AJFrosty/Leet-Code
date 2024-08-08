# https://leetcode.com/problems/construct-product-matrix/description/
#INCOMPLETE
def constructProductMatrix(grid: list[list[int]]) -> list[list[int]]:
    row = len(grid)
    col = len(grid[0])
    pre = [[1 for x in range(col)] for x in range(row)]
    fin = [[1 for x in range(col)] for x in range(row)]
    product = 1

    for i in range(row):
            for j in range(col):
                pre[i][j] = product
                product *= grid[i][j]
    
    product = 1
    for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                fin[i][j] = (pre[i][j] * product) % 12345
                product *= grid[i][j]
                
    return fin

print(constructProductMatrix([[1,2,3],[4,5,6]]))