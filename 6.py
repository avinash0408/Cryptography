alpha="abcdefghijklmnopqrstuvwxyz"
alpha_map={x:ord(x)-97 for x in alpha}
def encrypt(plain_text,key):
    cipher=""
    p=-1
    plain_text=plain_text.lower()
    key=key.lower()
    for i in plain_text:
        #skip the spaces
        if(i==" "):
            pass
        else:
            p=(p+1)%(len(key))
            #vignere cipher encrypt: cipher=(key+plain)mod26
            #example: plain= enemya ttacks  tonigh t
                    #  key=  pascal pascal  pascal p
            cipher=cipher+chr(97+(alpha_map[key[p]]+alpha_map[i])%26)
    return cipher

def decrypt(cipher,key):
    revert=""
    key=key.lower()
    p=-1
    for i in cipher:
        p=(p+1)%(len(key))
        #vignere cipher decrypt: plain=(cipher-key)mod26
        revert=revert+chr(97+(alpha_map[i]-alpha_map[key[p]])%26)
    return revert
        


if __name__ == "__main__":

    f1=open("files/B180409CS_SAMUDRALA_6_I.txt","r")
    plain_text=input("enter plain:").lower()
    plain_text=plain_text.rstrip('\n')
    #reading the key from file
    key=input("enter key string:").lower()
    key=key.rstrip('\n')
    cipher=encrypt(plain_text,key)
    f2=open("files/B180409CS_SAMUDRALA_6_O.txt","w")
    print("Encrypted text is:" +cipher+'\n')
    revert=decrypt(cipher,key)
    f2=open("files/B180409CS_SAMUDRALA_6_O.txt","a")
    print("Decrypted text is:" +revert)