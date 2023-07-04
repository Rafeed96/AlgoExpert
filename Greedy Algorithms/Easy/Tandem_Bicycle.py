def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    blueShirtSpeeds = blueShirtSpeeds[::-1]

    tots = 0

    n = len(redShirtSpeeds)

    if fastest == True:
        for i in range(0,n):
            if redShirtSpeeds[i] > blueShirtSpeeds[i]:
                tots = tots + redShirtSpeeds[i]
            elif blueShirtSpeeds[i] > redShirtSpeeds[i]:
                tots = tots + blueShirtSpeeds[i]
            else:
                tots = tots + blueShirtSpeeds[i]
    elif fastest == False:
        for i in range(0,n):
            if redShirtSpeeds[i] < blueShirtSpeeds[i]:
                tots = tots + redShirtSpeeds[i]
            elif blueShirtSpeeds[i] < redShirtSpeeds[i]:
                tots = tots + blueShirtSpeeds[i]
            else:
                tots = tots + blueShirtSpeeds[i]


    print(tots)
    return tots



redShirtSpeeds =  [5, 5, 3, 9, 2]
blueShirtSpeeds = [3, 6, 7, 2, 1]
fastest = False

tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest)