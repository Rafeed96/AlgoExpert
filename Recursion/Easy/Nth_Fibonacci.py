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

    print(sum)
    
    

n = 2
getNthFib(n)