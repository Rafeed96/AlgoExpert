def isValidSubsequence(array, sequence):

    # done  16/24
    output = False    

    for i in sequence:
        output = False
        for j in array:
           if j == i :
               output = True    
               
        if output == False:
            break

    
    print(output) 



array = [5, 1, 22, 25, 6, -1, 8, 10],
sequence = [5, 1, 22, 25, 6, -1, 8, 10, 10]


isValidSubsequence(array, sequence)

