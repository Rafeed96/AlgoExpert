def twoNumberSum(array, targetSum):
    
    x = len(array)

    ret = []

    for i in range(0,x):
        if i == (x-1):
            break
        for j in range((i+1),x):
            if array[i] + array[j] == targetSum:
                ret.append(array[i])
                ret.append(array[j])

    return ret

arr = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10


twoNumberSum(arr, target)