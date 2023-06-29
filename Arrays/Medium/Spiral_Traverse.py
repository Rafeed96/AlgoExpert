def spiralTraverse(array):
    
    final = []

    row = 0 
    col = 0

    n = len(array)
    m = n
    
    for i in range(0, n):
        for j in range(0, m):
            print(array[i][j])
        

    return final


array = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
  ]

spiralTraverse(array)