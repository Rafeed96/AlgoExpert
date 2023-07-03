def isMonotonic(array):
    # Write your code here.

    p_count = True
    n_count = True
    n = len(array)

    for i in range(0,n-1):

        if array[i] > array[i+1]:
            n_count = False
        
        if array[i] < array[i+1]:
            p_count = False

    out = True  
    if n_count == True or p_count == True:
        out = True
    else :
        out = False

    return out

array= [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

isMonotonic(array)
