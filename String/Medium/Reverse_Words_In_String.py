def reverseWordsInString(string): 
    
    st = ""   
    rev = "" 
    final = []
    n = len(string)
    for i in range(0,n):
        if string[i] == " " or i == n-1:
            st = st + string[i]
            final.append(st)
            st = ""
        else:
            st = st + string[i]

    final = final[::-1]

    for i in final:
        rev = rev + str(i) + " "

    print(rev)
    return rev




string = "AlgoExpert is the best!"
reverseWordsInString(string)