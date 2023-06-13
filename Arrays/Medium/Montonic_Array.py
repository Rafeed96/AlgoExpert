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

    return out



array= [1, 1, 1, 2, 3, 4, 1]

isMonotonic(array)

'''
def isMonotonic(array):
    # Write your code here.
    
    neg = True
    pos = True
    p_count = 0
    n_count = 0
    n = len(array)

    for i in range(1, n):

        if array[i] >= array[i-1]:
            pos = True
        else:
            pos = False
            p_count = p_count + 1

        
        if array[i] <= array[i-1]:
            neg = True
        else:
            neg = False
            n_count = n_count + 1
    
    if n_count or p_count == 0:
        out = True
    else:
        out = False

    return out
'''


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


    print(posA)
    print(negA)
    print(array)

    for i in range(0, n):
        if array[i] != posA[i]:
            p_count = p_count + 1
        
        if array[i] != negA[i]:
            n_count = n_count + 1

        print("-----------", array[i], "Pos: ",posA[i], " Neg: ",negA[i])


    out = True  
    print(p_count," " ,n_count)
    if n_count or p_count >= 0:
        out = False


    print(out)
    return out

'''