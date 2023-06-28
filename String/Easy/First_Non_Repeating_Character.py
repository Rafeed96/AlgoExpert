def firstNonRepeatingCharacter(string):

    ind = 0
    n = len(string)
    count = 0
    
    for i in range(0, n):
        count = 1
    
        for j in range(i, n):
            if string[i] == string[j]:
                count = count + 1
                continue


    return ind




string = "abcdcaf"
firstNonRepeatingCharacter(string)