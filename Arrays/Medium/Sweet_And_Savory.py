def sweetAndSavory(dishes, target):
    # Write your code here.
    
    dishes.sort()
    print(dishes)
    print(target)

    sweet = []
    savory = []

    for i in dishes:
        if i < 0:
            sweet.append(i)
        else:
            savory.append(i)

    print("Sweet:",sweet)
    print("Savory:",savory)

    

    return []




dishes = [2, 5, -4, -7, 12, 100, -25]
target = -5

sweetAndSavory(dishes, target)