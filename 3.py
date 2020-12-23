alpha="abcdefghijklmnopqrstuvwxyz"
alpha_map={x:ord(x)-97 for x in alpha}

def encrypt(plain_text,key):
    plain_text=plain_text.replace(" ","")
    plain=[]
    for i in plain_text:
        #skip the spaces
        if(i==" "):
            continue
        plain.append(alpha_map[i])
    cipher=""
    for i in plain:
        #shift cipher encrypt: cipher=(plain +key) mod 26
        cipher=cipher+chr((97+((i+key)%26)))
    return cipher

def decrypt(cipher,key):
    cip=[]
    for i in cipher:
        cip.append(alpha_map[i])
    revert=""
    for i in cip:
        #shift cipher decrypt: cipher=(plain +key) mod 26
        revert=revert+chr(97+(i-key)%26)
    return revert

if __name__ == "__main__":
    f1=open("files/B180409CS_SAMUDRALA_3_I.txt","r")
    plain_text=input("enter plain:").lower()
    plain_text= plain_text.rstrip('\n')
    k=int(input("enter a key"))
    cipher=encrypt(plain_text,k)
    f2=open("files/B180409CS_SAMUDRALA_3_O.txt","w")
    print("Encrypted text is:" +cipher+'\n')
    revert=decrypt(cipher,k)
    f2=open("files/B180409CS_SAMUDRALA_3_O.txt","a")
    print("Decrypted text is:" +revert)
   
    
    

