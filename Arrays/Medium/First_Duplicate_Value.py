def firstDuplicateValue(array):
    # Write your code here.

    # need to count distance in between

    n = len(array)
    dist = n
    temp = n
    final = 0
    out = False
    for i in range(0, n):
        val = array[i]
        for j in range(i+1, n):
            if val == array[j]:
                temp = j-i
                if temp < dist:
                    dist = temp
                    final = val
                continue

 

    print(final," ", dist, " ", temp)
    return final





array = [13, 4, 10, 10, 8, 13, 13, 7, 11, 6, 3, 2, 11]

firstDuplicateValue(array)