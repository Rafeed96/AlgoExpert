# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array):
    # Write your code here.

    sum = 0
    for i in array:
        if type(i) == int:
            sum = sum + i
        else:
            out = productSum(i)
            sum = sum + out

    print(sum)
    return sum


array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]


productSum(array)