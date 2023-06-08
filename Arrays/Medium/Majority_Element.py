def majorityElement(array):
    # Write your code here.

    arr = []
    n = len(array)
    array.sort()
    freq = []
    count = 0
    max_freq = 0
    print(array)
    for i in range(0,n):
        if array[i] in arr:
            count = count +1
        else:
            freq.append(count)
            count = 0
            count = count +1
            arr.append(array[i])       


    print(arr)
    print(freq)

    return arr


array = [1,2,3,2,2,1,2]

majorityElement(array)