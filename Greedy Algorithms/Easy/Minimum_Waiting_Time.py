def minimumWaitingTime(queries):
    # Write your code here.
    time = 0

    n = len(queries)
    queries.sort()

    total = 0
    for i in range(0,n):
        if i == 0:
            continue

        else:
            sum = 0
            for j in range(0,i):
                sum = sum + queries[j]

            total = total + sum


    return total 


queries = [3, 2, 1, 2, 6]
minimumWaitingTime(queries)