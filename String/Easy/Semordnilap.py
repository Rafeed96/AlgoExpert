def semordnilap(words):

    semor = []
    n = len(words)

    for i in words:
        l = i
        l = l[::-1]
        print(l)

        temp = []
        for j in words:
            if i == j:
                continue
            else:
                if j == l:
                    temp.append(i)
                    temp.append(l)
                    semor.append(temp)
                    temp =[]
                    continue              


    print(semor)

    return semor



words = ["diaper", "abc", "test", "cba", "repaid",] 
semordnilap(words)