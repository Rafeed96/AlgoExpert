def missingNumbers(nums):
    # Write your code here.
    arr = []

    n = len(nums)
    n = n+2
    nums.sort()

    for i in range(1,n+1):
        if i in nums:
            continue
        else:
            nums.append(i)
            arr.append(i)

    return arr




nums = [1,4,3]
missingNumbers(nums)