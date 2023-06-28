def firstNonRepeatingCharacter(string):

    ind = 0
    fl = False
    n = len(string)
    count = 0
    l = []
    for i in range(0, n):
        count = 1
        if string[i] not in l:
            l.append(string[i])
            for j in range(i, n):
                if string[i] == string[j]:
                    count = count + 1
                    
        else:
            continue


    return ind




string = "abcdcaf"
firstNonRepeatingCharacter(string)