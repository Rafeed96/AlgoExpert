def minimumWaitingTime(queries):
    # Write your code here.
    time = 0
    out = []
    n = len(queries)
    queries.sort()
    print(queries)

    for i in range(0,n):
        if i == 0:
            out.append(0)
            continue

        else:
            sum = 0
            for j in range(0,i):
                sum = sum + queries[j]

            out.append(sum)
        
    

        


    return time 




queries = [3, 2, 1, 2, 6]
minimumWaitingTime(queries)