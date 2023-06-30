def reverseWordsInString(string): 
    
    st = ""   
    rev = "" 
    final = []
    n = len(string)
    for i in range(0,n):
        if string[i] == " " or i == n-1:
            final.append(st)
            st = ""
        else:
            st = st + string[i]

    print(final)
    return st




string = "AlgoExpert is the best!"
reverseWordsInString(string)