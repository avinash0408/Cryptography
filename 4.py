def get_key(keys,val): 
    for key, value in keys.items(): 
         if val == value: 
             return key 

def encrypt(plain_text,key):
    plain_text=plain_text.lower()
    cipher=""
    for i in plain_text:
        #skip the spaces
        if(i==" "):
            pass
        else:
            #substistution cipher encrypt: cipher=key[plain]
            cipher=cipher+key[i]
    return cipher

def decrypt(cipher,key):
    revert=""
    for i in cipher:
        revert=revert+get_key(key,i)
    return revert




if __name__ == "__main__":
    f1=open("files/B180409CS_SAMUDRALA_4_I.txt","r")
    plain_text=f1.readline().lower()
    plain_text= plain_text.rstrip('\n')
    #key for mono alphabetic
    key={'a':'N','b':'O','c':'A','d':'T','e':'R','f':'B','g':'E','h':'C','i':'F','j':'U','k':'X','l':'D','m':'Q',
'n':'G','o':'Y','p':'L','q':'K','r':'H','s':'V','t':'I','u':'J','v':'M','w':'P','x':'Z','y':'S','z':'W'}
    cipher=encrypt(plain_text,key)
    f2=open("files/B180409CS_SAMUDRALA_4_O.txt","w")
    f2.write("Encrypted text is:" +cipher+'\n')
    revert=decrypt(cipher,key)
    f2=open("files/B180409CS_SAMUDRALA_4_O.txt","a")
    f2.write("Decrypted text is:" +revert)

    