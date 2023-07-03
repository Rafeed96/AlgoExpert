def firstDuplicateValue(array):
    # Write your code here.

    n = len(array)
    dist = n
    temp = n
    final = -1
    ind = 0
    out = False
    for i in range(0, n):
        val = array[i]
        for j in range(i+1, n):
            if val == array[j]:
                temp = j
                if temp < dist:
                    dist = temp
                    final = val
                continue

    return final





array = [3, 1, 3, 1, 1, 4, 4]

firstDuplicateValue(array)