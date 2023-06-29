def semordnilap(words):

    semor = []
    final = []
    n = len(words)
    count = 0
    for i in words:
        count = count + 1
        l = i
        l = l[::-1]


        temp = []
        for j in words:
            if i == j:
                continue
            else:
                if j == l:
                    temp.append(i)
                    temp.append(l)
                    semor.append(temp)
                    
                    continue              

    for k in semor:
        k.sort()
        final.append(k)

    

    #print(semor)
    print(final)

    return semor



words = ["diaper", "abc", "test", "cba", "repaid",] 
semordnilap(words)