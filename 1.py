
#only these keys are to be taken as key1 since only these have multiplicative inverse in z26
accept=[1,3,5,7,9,11,15,17,19,21,23,25]

#dictionary to fetch inverse of a key
inverse={1:1,3:9,5:21,7:15,9:3,11:19,15:7,17:23,19:11,21:5,
23:17,25:25}

#mapping alphabets to corresponding numbers
alpha="abcdefghijklmnopqrstuvwxyz"
alpha_map={x:ord(x)-97 for x in alpha}

def encrypt(plain_text,k1,k2):
    cipher=""
    for i in plain_text:
        #skip the spaces
        if(i==" "):
            continue
        else:
            #affine encrypt method
            #cipher=(plain *k1)+k2 mod 26
            p=((alpha_map[i]*k1)+k2)%26 
            cipher=cipher+chr(p+97)
    return cipher


def decrypt(cipher,k1,k2):
    revert=""
    for i in cipher:
        #affine decrypt method
        #plain=(cipher-k2)*inverse(k1) mod 26
        p=((alpha_map[i]-k2)*inverse[k1])%26
        revert=revert+chr(p+97)
    return revert
     


if __name__ == "__main__": 
    #reading plain text from file
    #converting entire text to small letters
    f1=open("files/B180409CS_SAMUDRALA_1_I.txt","r")
    plain_text=input("enter plain:").lower()
    plain_text= plain_text.rstrip('\n')

    #user input keys to encrypt
    #since users might end up in error by giving a key that doesn't have an inverse under module 26
    #i initialized one of the key with valid input
    k1=18
    #reading second key from file
    k2=int(input("enter a int key"))
    #encrypt
    cipher=encrypt(plain_text,k1,k2)
    #open file to write data
    f2=open("files/B180409CS_SAMUDRALA_1_O.txt","w")
    print("Encrypted text is:" +cipher+'\n')
    #decrypt
    # revert=decrypt(cipher,k1,k2)
    # f2=open("files/B180409CS_SAMUDRALA_1_O.txt","a")
    # print("Decrypted text is:" +revert)








