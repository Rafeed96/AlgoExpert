def minimumCharactersForWords(words):

    ret = []
    charDict = {}
    for i in words:
        n = len(i)
        temp = []
        charDict = {}
        for j in range(0,n):
            count = 1
            for k in range(j+1,n):
                if i[j] == i[k]:
                    count = count +1
            
            charDict[i[j]] = count
        
        print(charDict)

        print(" ")
    return ret


words = ["this", "that", "did", "deed", "them!", "a"]
minimumCharactersForWords(words)