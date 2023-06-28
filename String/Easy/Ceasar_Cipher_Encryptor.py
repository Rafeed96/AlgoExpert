def caesarCipherEncryptor(string, key):
    
    for i in range(0, len(string)):
        n = ord(string[i])
        l = ord(string[i])
        n = n + key

        if n > 122:
            n = n - 25
        
        
        print(string[i], " " ,chr(n) , " ", l , " ",n)

string = "abcxyz"
key = 2


caesarCipherEncryptor(string, key)