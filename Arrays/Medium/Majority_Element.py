def majorityElement(array):
    # Write your code here.

    arr = []
    n = len(array)
    array.sort()
    freq = []
    count = 0
    max_freq = 0
    print(array)
    temp = 0
    for i in range(0,n):
        if array[i] in arr:
            count = count +1
        elif count > 0:
            freq.append(count)
            count = 0        
        if count == 0:
            arr.append(array[i])  
            count = count +1

    freq.append(count)        



    return arr


array = [5, 4, 3, 2, 1, 1, 1, 1, 1]

majorityElement(array)