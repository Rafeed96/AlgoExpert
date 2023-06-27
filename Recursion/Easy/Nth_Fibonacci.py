def getNthFib(n):
    # Write your code here.
    fib = [0, 1]
    first = fib[0]
    second = fib[1]
    sum = 0
    
    
    for i in range(n-2):

        sum = first + second
        first = second
        second = sum

    if n <= 2:
        n = n - 1
        sum = fib[n]

    return sum

    
    

n = 2
getNthFib(n)