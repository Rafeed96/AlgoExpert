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
            print("Sweet + Savory : ", (j) ," ", temp)
            if(temp == target):
                final.append(i)
                final.append(j)
                break

            if target > 0:
                far = target - temp
                if far <= dist :
                    dist = far

            else:
                far = target + temp
                if far >= dist :
                    dist = far

            

    print(final)
    return []

dishes = [2, 5, -4, -7, 12, 100, -25]
target = -5

sweetAndSavory(dishes, target)