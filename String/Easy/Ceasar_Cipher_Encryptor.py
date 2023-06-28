def caesarCipherEncryptor(string, key):

    st = ""
    for i in range(0, len(string)):
        n = ord(string[i])
        l = ord(string[i])
        n = n + key

        if n > 122:
            while(n>122):
                n = n - 26
        
        # print(string[i], " ", chr(n), " ", n)
        
        st = st + chr(n)
  

    return st

string = "abc"
key = 52


caesarCipherEncryptor(string, key)