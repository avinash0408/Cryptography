
from collections import Counter

alpha="abcdefghijklmnopqrstuvwxyz"
alpha_map={x:ord(x)-97 for x in alpha}
def encrypt(plain_text):
    key="untrUE"
    key=(key.replace(" ","")).lower()
    cipher=""
    p=-1
    plain_text=plain_text.lower()
    for i in plain_text:
        if(i==" "):
            pass
        else:
            p=(p+1)%(len(key))
            cipher=cipher+chr(97+(alpha_map[key[p]]+alpha_map[i])%26)
    return cipher

def decrypt(cipher,key):
    revert=""
    key=key.lower()
    p=-1
    for i in cipher:
        p=(p+1)%(len(key))
        revert=revert+chr(97+(alpha_map[i]-alpha_map[key[p]])%26)
    return revert
        
def bob_decrypt(cipher):
    revert=""
    key="untrUE"
    key=(key.replace(" ","")).lower()
    p=-1
    for i in cipher:
        p=(p+1)%(len(key))
        revert=revert+chr(97+(alpha_map[i]-alpha_map[key[p]])%26)
    return revert

def analyze(plain,cipher):
    key=""
    li_key=[]
    for i in range(len(plain)):
        li_key.append((alpha_map[cipher[i]]-alpha_map[plain[i]])%26)
    print(li_key)
    fin=[]
    for i in range(len(li_key)):
        if(not(li_key[i] in fin)):
            fin.append(li_key[i])
        else:
            j=i
            flag=0
            while(j<i+len(fin)):
                if(li_key[j] in fin):
                   flag=flag+1
                j+=1
            if(flag!=len(fin)):
                fin.append(li_key[i])
            else:
                break


    for i in fin:
        key=key+chr(97+i)
    

    return key
def known_plaintext(cipher):
    kplain="mynameisavinash"
    kcipher="glgrgicftmcrufa"
    kplain=kplain.lower() 
    result_key= analyze(kplain,kcipher)
    return decrypt(cipher,result_key)

def choosen_plaintext(cipher):
    cplain="MySELF avinash how are you"
    cplain=(cplain.lower()).replace(" ","")
    result_cipher=encrypt(cplain)
    result_key= analyze(cplain,result_cipher)
    return decrypt(cipher,result_key)

def choosen_cipher(cipher):
    ccipher="hsgjfgkhlsdjkg"
    result_plain=bob_decrypt(ccipher)
    result_key= analyze(result_plain,ccipher)
    return decrypt(cipher,result_key)

def known_cipher(cipher):
    revert=""

    #not possible or maybe too complex to compute

    return revert

if __name__ == "__main__":
    f1=open("files/B180409CS_SAMUDRALA_6a_I.txt","r")
    plain_text=f1.readline().lower()
    plain_text= plain_text.rstrip('\n')
    cipher=encrypt(plain_text)
    f2=open("files/B180409CS_SAMUDRALA_6a_O.txt","w")
    f2.write("Encrypted text is:" +cipher+'\n')
    r1=known_plaintext(cipher)
    f2=open("files/B180409CS_SAMUDRALA_6a_O.txt","a")
    f2.write("Decrypted text using known-plaintext attack is: " +r1+'\n')
    r2=choosen_plaintext(cipher)
    f2.write("Decrypted text using choosen-plaintext attack is: " +r2+'\n')
    r3=choosen_cipher(cipher)
    f2.write("Decrypted text using choosen-cipher attack is: " +r3+'\n')

    r4=known_cipher(cipher)
    f2.write("Decrypted text using known-cipher attack is: "+r4+'\n')
    f2.write(" vignere known-cipher attack is too complex to compute\n")