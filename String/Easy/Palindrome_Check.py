def isPalindrome(string):
    
    out = True
    n = len(string)
    st = string[::-1]

    for i in range(0, n):
        if st[i] != string[i]:
            out = False
            break

    # print(st, " ", string)    
    print(out)
    return out



string = "abcdcba"
isPalindrome(string)