def isValidSubsequence(array, sequence):

    # done  16/24
    output = False    
    n = len(array)
    current = 0
    for i in sequence:
        output = False
        for j in range(current, n):
           if array[j] == i:
               output = True   
               current = j 
               
        if output == False:
            break

    
    print(output)



array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 5]



isValidSubsequence(array, sequence)

