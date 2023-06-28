def runLengthEncoding(string):

    st = ""
    n = len(string)
    count = 0
    for i in range(0, n-1):
        count = count + 1

        if count > 8:
            l = str(count)
            st = st + l + string[i]
            count = 0

        if string[i] != string[i+1]:
            l = str(count)
            st = st + l + string[i]
            count = 0

    print(st)

    return st


string = "AAAAAAAAAAAAABBCCCCDD"
runLengthEncoding(string)