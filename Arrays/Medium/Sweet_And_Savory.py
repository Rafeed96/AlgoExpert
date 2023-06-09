def sweetAndSavory(dishes, target):
    # Write your code here.
    
    dishes.sort()

    sweet = []
    savory = []

    for i in dishes:
        if i < 0:
            sweet.append(i)
        else:
            savory.append(i)

    dist = min(sweet) + max(savory) 

    far = 0

    final = []
    temp = 0
    for i in sweet:
        print("For : ", i , " With Target : " , target)
        for j in savory:
            temp = i + j
            print("Sweet + Savory : ", temp)
            if target > 0:
                far = target - temp
            else:
                far = target + temp
            


    return []

dishes = [2, 5, -4, -7, 12, 100, -25]
target = -5

sweetAndSavory(dishes, target)