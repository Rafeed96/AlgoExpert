def isMonotonic(array):
    # Write your code here.
    
    neg = True
    pos = True
    p_count = 0
    n_count = 0
    n = len(array)

    posA = array
    negA = array[::-1]
    
    for i in range(0, n):
        if array[i] != posA[i]:
            p_count = p_count + 1
        
        if array[i] != negA[i]:
            n_count = n_count + 1
        
    
    if n_count or p_count == 0:
        out = True
    else:
        out = False


    return out



array= [-1, -5, -10, -1100, -1101, -1102, -9001]

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