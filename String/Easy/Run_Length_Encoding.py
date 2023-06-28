def runLengthEncoding(string):

    st = ""
    n = len(string)
    count = 0
    for i in range(0, n-1):
        print(string[i])
        count = count + 1

        if count > 8:
            l = str(count)
            st = st + l + string[i]
            count = 0

        if string[i] != string[i+1]:
            l = str(count)
            st = st + l + string[i]
            count = 0

        if i == n-2:
            if string[i] == string[i+1]:
                count = count + 1
                l = str(count)
                st = st + l + string[i]
                count = 0
            else:
                l = str(count)
                st = st + l + string[i]
                count = 1
                l = str(count)
                st = st + l + string[i+1]

    return st


string = "AAAAAAAAAAAAABBCCCCDD"
runLengthEncoding(string)