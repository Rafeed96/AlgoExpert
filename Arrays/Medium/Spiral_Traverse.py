def spiralTraverse(array):
    
    final = []

    row = 0 
    col = 0

    n = len(array)
    m = n
    
    for i in range(0, n):
        for j in range(0, m):
            final.append(array[i][j])

        i = 1
        j = m-1

        for k in range(1,m):
            final.append(array[k][j])

        i = n-1
        k = m-2
        for j in range(m-1):
            final.append(array[i][k])
            k = k-1

        

        break
        #print("               ", array[i][j])

        

    print(final)
    return final


array = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
  ]

spiralTraverse(array)