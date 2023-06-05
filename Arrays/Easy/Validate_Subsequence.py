def isValidSubsequence(array, sequence):

    # done  16/24
    output = True    

    for i in sequence:
        if i not in array:
            output = False

    
    print(output) 



array = [5, 1, 22, 25, 6, -1, 8, 10],
sequence = [5, 1, 22, 25, 6, -1, 8, 10, 10]


isValidSubsequence(array, sequence)

