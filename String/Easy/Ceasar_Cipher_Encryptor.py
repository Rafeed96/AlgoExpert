def caesarCipherEncryptor(string, key):

    st = ""
    for i in range(0, len(string)):
        n = ord(string[i])
        l = ord(string[i])
        n = n + key

        if n > 122:
            n = n - 26
        
        
        st = st + chr(n)
  

    return st

string = "abcxyz"
key = 2


caesarCipherEncryptor(string, key)