def sortedSquaredArray(array):
    # Write your code here.
    sqrd = []
    temp = 0
    for i in array:
        temp = i*i
        sqrd.append(temp)

    sqrd.sort()
    print(sqrd)
    return sqrd



array = [-3, -2, -1]

sortedSquaredArray(array)