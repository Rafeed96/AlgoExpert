def smallestDifference(arrayOne, arrayTwo):

    
    ret = []
    mininum = arrayOne[0] - arrayTwo[0]

    mininum = abs(mininum)
    print(mininum)

    for i in range(1,len(arrayOne)):        

        for j in range(1, len(arrayTwo)):
    #         # print(arrayTwo[j])

    
    # return ret




arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

smallestDifference(arrayOne, arrayTwo)
