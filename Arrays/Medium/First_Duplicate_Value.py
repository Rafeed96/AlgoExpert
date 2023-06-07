def firstDuplicateValue(array):
    # Write your code here.

    # need to count distance in between

    n = len(array)
    out = False
    for i in range(0, n):
        val = array[i]
        for j in range(i, n):
            if val == array[j]:
                out = True
                break

        if out == True:
            break

    return val





array = [2, 1, 5, 3, 3, 2, 4]

firstDuplicateValue(array)