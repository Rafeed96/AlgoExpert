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

    temp = []
    for i in range(0, row):
        temp.append(0)

    for i in range(0, col):
        mat.append(temp)

    print(mat)
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):

            mat[j][i] = matrix[i][j]
            print(mat)


    print(mat)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transposeMatrix(matrix)