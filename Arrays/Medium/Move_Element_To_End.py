def moveElementToEnd(array, toMove):
    # Write your code here.

    n = len(array)
    end = []
    for i in range(0,n):        
        if array[i] == toMove:            
            array.remove(array[i])
            array.append(toMove)
                        
    return array
    
arr = [2,1,2,2,2,3,4,2]
num = 2
moveElementToEnd(arr, num)
