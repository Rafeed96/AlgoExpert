def transposeMatrix(matrix):
    # Write your code here.
    mat = []
    n = len(matrix)
    row = 0
    col = 0
    for i in range(0,n):
        row = i
        col = len(matrix[i])
    row = row + 1
    print(row,col)
    temp = []
    for i in range(0, row):
        temp.append(0)

    for i in range(0, col):
        mat.append(temp)

    

    print(mat)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transposeMatrix(matrix)