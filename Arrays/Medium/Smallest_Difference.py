def smallestDifference(arrayOne, arrayTwo):
    
    ret = []
    mininum = arrayOne[0] - arrayTwo[0]
    tem = 0
    mininum = abs(mininum)
    #print(mininum)
    ret = [arrayOne[0], arrayTwo[0]]


    for i in range(1,len(arrayOne)):        

        for j in range(0, len(arrayTwo)):
            tem = (arrayOne[i] - arrayTwo[j])
            tem = abs(tem)

            if tem < mininum:
                ret = []
                mininum = tem
                ret.append(arrayOne[i])
                ret.append(arrayTwo[j])         
    
    return ret

arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]






smallestDifference(arrayOne, arrayTwo)
