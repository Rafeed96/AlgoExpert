def findThreeLargestNumbers(array):

    final = []
    n = len(array)
    first = min(array)
    second = min(array)
    third = min(array)
    print(third)

    for i in range(0, n):
        if array[i] > first:
            third = second
            second = first
            first = array[i]

    array[::-1]
   # print(array)
    print(first, second, third)


    return final


array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
findThreeLargestNumbers(array)