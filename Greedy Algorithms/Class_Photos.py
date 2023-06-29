def classPhotos(redShirtHeights, blueShirtHeights):
    
    out = True
    n = len(redShirtHeights)

    redTaller = True
    blueTaller = True
    for i in range(0,n):
        if redShirtHeights[i] < blueShirtHeights[i]:
            redTaller = False

        if redShirtHeights[i] > blueShirtHeights[i]:
            blueTaller = False

    return out




redShirtHeights = [5, 8, 1, 3, 4]
blueShirtHeights = [6, 9, 2, 4, 5]

classPhotos(redShirtHeights, blueShirtHeights)