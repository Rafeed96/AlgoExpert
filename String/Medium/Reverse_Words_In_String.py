def reverseWordsInString(string): 
    
    st = ""   
    rev = "" 
    final = []
    n = len(string)
    for i in range(0,n):
        if string[i] == " " :
            final.append(st)
            st = ""
        elif i == n-1:
            st = st + string[i]
            final.append(st)
            st = ""
        else:
            st = st + string[i]

    final = final[::-1]

    l = len(final)

    for i in range(0,l):
        if i == l-1:
            rev = rev + final[i]
        else:
            rev = rev + final[i] + " "


    return rev

string = "AlgoExpert is the best!"
reverseWordsInString(string)