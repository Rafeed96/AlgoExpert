def majorityElement(array):
    # Write your code here.

    arr = []
    n = len(array)
    array.sort()
    freq = []
    count = 0
    max_freq = 0

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
    flag = 0
    if len(arr) <= 0:
        flag = -1

    max_freq = freq[0]
    flag = arr[0]
    for i in range(1, len(arr)):
        if freq[i] > max_freq:
            max_freq = freq[i]
            flag = arr[i]

    return flag


array =[1, 2, 3, 2, 3, 2, 2, 4, 2]

majorityElement(array)