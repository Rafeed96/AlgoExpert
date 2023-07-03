def reverseWordsInString(string): 
    
    st = ""   
    rev = "" 
    final = []
    n = len(string)
    count = 0
    for i in range(0,n):
        if string[i] == " " and count == 0:
            final.append(st)
            st = ""
        elif string[i] == " " and count > 0:
            st = st + string[i]
        elif i == n-1:
            st = st + string[i]
            final.append(st)
            st = ""
            count = 0
        else:
            st = st + string[i]
            count = 0

    final = final[::-1]

    l = len(final)

    for i in range(0,l):
        if i == l-1:
            rev = rev + final[i]
        else:
            rev = rev + final[i] + " "

    print(string, len(string))
    print(rev, len(rev))
    return rev

string = "test        "

reverseWordsInString(string)