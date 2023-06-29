def commonCharacters(strings):
    
    k = strings[0]
    final = []
    n = len(strings)
    for i in k:
        flag = True
       
        for j in range(1,n):
            l = strings[j]
            if i not in l:
                flag = False

        if flag == True:
            final.append(i)


    return final

strings = ["abc", "bcd", "cbad"]
commonCharacters(strings)