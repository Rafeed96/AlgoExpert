def generateDocument(characters, document):
    
    out = True
    cDict = {}
    n = len(characters)
    for i in range(0,n):
        count = 1
        if characters[i] not in cDict:
            cDict[characters[i]] = count
        else:
            x = cDict.get(characters[i])
            x = x + count
            cDict.update({characters[i]: x})

    dDict = {}
    n = len(document)
    for i in range(0,n):
        count = 1
        if document[i] not in dDict:
            dDict[document[i]] = count
        else:
            x = dDict.get(document[i])
            x = x + count
            dDict.update({document[i]: x})

    print(dDict)
    return out




characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"

generateDocument(characters, document)