def majorityElement(array):
    # Write your code here.

    arr = []
    n = len(array)
    array.sort()
    freq = []
    count = 0
    max_freq = 0
    for i in range(0,n-1):
        if array[i+1] == array[i]:
            count = count +1
        elif array[i+1] != array[i]:
            arr.append(array[i])
            freq.append(count)
            count = 0

            



    print(arr)
    print(freq)

    return arr


array = [1,2,3,2,2,1,2]

majorityElement(array)