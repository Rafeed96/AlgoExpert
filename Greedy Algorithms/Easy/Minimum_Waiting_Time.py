def minimumWaitingTime(queries):
    # Write your code here.
    time = 0

    for i in queries:
        time = time + i

    time = time + 1

    return time 




queries = [3, 2, 1, 2, 6]
minimumWaitingTime(queries)