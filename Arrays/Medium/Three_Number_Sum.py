def threeNumberSum(array, targetSum):
    
    #Partially Done 5/11

    x = len(array)

    ret = []
    fin = []

    for i in range(0,x-2):
        if i == (x-2):
            break
        for j in range((i+1),x-1):

            for k in range((j+1),x):
                ret = []
                sum = (array[i] + array[j] + array[k])
                if sum == targetSum:
                    print(sum)
                    ret.append(array[i])
                    ret.append(array[j])
                    ret.append(array[k])
                    fin.append(ret)
    print(fin)
    return fin

arr = [12, 3, 1, 2, -6, 5, -8, 6]
target = 0


threeNumberSum(arr, target)