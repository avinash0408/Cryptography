def encrypt(plain_text):
    key={'a':'N','b':'O','c':'A','d':'T','e':'R','f':'B','g':'E','h':'C','i':'F','j':'U','k':'X','l':'D','m':'Q',
'n':'G','o':'Y','p':'L','q':'K','r':'H','s':'V','t':'I','u':'J','v':'M','w':'P','x':'Z','y':'S','z':'W'}
    plain_text=plain_text.lower()
    cipher=""
    for i in plain_text:
        if(i==" "):
            pass
        else:
            cipher=cipher+key[i]
    return cipher
def get_key(dic,val):
    for key,value in dic.items():
        if val==value:
            return key
def decrypt(cipher):
    key={'a':'N','b':'O','c':'A','d':'T','e':'R','f':'B','g':'E','h':'C','i':'F','j':'U','k':'X','l':'D','m':'Q',
'n':'G','o':'Y','p':'L','q':'K','r':'H','s':'V','t':'I','u':'J','v':'M','w':'P','x':'Z','y':'S','z':'W'}
    revert=""
    for i in cipher:
        revert=revert+get_key(key,i)
    return revert

def known_plaintext(cipher):
    kplain="abcdefghijklmnopqrstuvwxyz"
    kcipher="NOATRBECFUXDQGYLKHVIJMPZSW"
    dic={}
    for i in range(len(kplain)):
        dic[kplain[i]]=kcipher[i]
    revert=""
    for i in range(len(cipher)):
        revert=revert+get_key(dic,cipher[i])
    return revert

def choosen_plaintext(cipher):
    cplain="qwertyuiopasdfghjklzxcvbnm"
    result_cipher=encrypt(cplain)
    dic={}
    for i in range(len(cplain)):
        dic[cplain[i]]=result_cipher[i]
    revert=""
    for i in range(len(cipher)):
        revert=revert+get_key(dic,cipher[i])
    return revert
def choosen_cipher(cipher):
    ccipher="qwertyuiopasdfghjklzxcvbnm".upper()
    result_plain=decrypt(ccipher)
    dic={}
    for i in range(len(ccipher)):
        dic[ccipher[i]]=result_plain[i]
    revert=""
    for i in range(len(cipher)):
        revert=revert+dic[cipher[i]]
    return revert
#known plain text too complex to compute

if __name__ == "__main__":
    print('   Welcome to substitution cipher  ')
    f1=open("files/B180409CS_SAMUDRALA_4a_I.txt","r")
    plain_text=f1.readline().lower()
    plain_text= plain_text.rstrip('\n')
    f2=open("files/B180409CS_SAMUDRALA_4a_O.txt","w")
    cipher=encrypt(plain_text)
    f2.write("Encrypted text is:" +cipher+'\n')
    r1=known_plaintext(cipher)
    f2=open("files/B180409CS_SAMUDRALA_4a_O.txt","a")
    f2.write("Decrypted text using known-plaintext attack is: " +r1 +'\n')
    r2=choosen_plaintext(cipher)
    f2.write("Decrypted text using choosen-plaintext attack is: " +r2+'\n')
    r3=choosen_cipher(cipher)
    f2.write("Decrypted text using choosen-cipher attack is: " +r3+'\n')

    

    