def isMonotonic(array):
    # Write your code here.

    p_count = 0
    n_count = 0
    n = len(array)

    for i in range(0,n-1):

        if array[i] > array[i+1]:
            





    for i in range(0, n):
        if array[i] != posA[i]:
            p_count = p_count + 1
        
        if array[i] != negA[i]:
            n_count = n_count + 1



    out = True  
    if n_count or p_count >= 0:
        out = False

    print(out)
    return out



array= [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

isMonotonic(array)

'''
def isMonotonic(array):
    # Write your code here.

    p_count = 0
    n_count = 0
    n = len(array)

    posA = []
    negA = []
    for i in array:
        posA.append(i)

    posA.sort()
    negA = posA[::-1]



    for i in range(0, n):
        if array[i] != posA[i]:
            p_count = p_count + 1
        
        if array[i] != negA[i]:
            n_count = n_count + 1



    out = True  
    if n_count or p_count >= 0:
        out = False

    print(out)
    return out


'''