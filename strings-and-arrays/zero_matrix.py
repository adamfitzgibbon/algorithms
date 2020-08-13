"""Write an algorithm such that if an element in an MxN matrix is 0, the entire row and column are set to 0"""

def zero_matrix(m):
    zcols = set()
    zrows = set()
    for i, row in enumerate(m):
        for j, cell in enumerate(row):
            if cell == 0:
                zrows.add(i)
                zcols.add(j)
    
    for i, row in enumerate(m):
        for j, cell in enumerate(row):
            if i in zrows or j in zcols:
                m[i][j] = 0
    
m = [[1,0,1], [0,1,1], [1,1,1]]    
expected = [[0,0,0], [0,0,0], [0,0,1]]

zero_matrix(m)
print(m)
