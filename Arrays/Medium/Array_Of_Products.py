def arrayOfProducts(array):
    # Write your code here.

    arr = []
    temp = 1
    n = len(array)

    for i in range(0, n):
        temp = 1
        for j in range(0, n):
            if j == i:
                continue
            else:
                temp = temp * array[j]

        arr.append(temp)

    return arr



array = [5, 1, 4, 2]

arrayOfProducts(array)