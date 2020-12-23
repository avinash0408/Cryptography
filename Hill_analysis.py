import numpy as np
import math
alpha="abcdefghijklmnopqrstuvwxyz"
alpha_map={x:ord(x)-97 for x in alpha}
accept=[1,3,5,7,9,11,15,17,19,21,23,25]
inverse={1:1,3:9,5:21,7:15,9:3,11:19,15:7,17:23,19:11,21:5,
23:17,25:25}

def encrypt(plain_text):
    #hill cipher encrypt: cipher matrix=plain matrix X key matrix
    plain_text=plain_text.lower()
    key=[[9,7,11,13],[4,7,5,6],[2,21,14,9],[3,23,21,8]]
    plain_text=plain_text.replace(" ","")
    if(len(plain_text)%len(key)!=0):
        x=len(key)-(len(plain_text)%len(key))
        plain_text=plain_text+x*'z'

    plain=[]
    li=[]
    i=0
    while(i<len(plain_text)):
        if(plain_text[i]!=" "):
            if(i!=0 and i%len(key)==0):
                plain.append(li)
                li=[]
            li.append(alpha_map[plain_text[i]])
        i+=1
    plain.append(li)
    ans=np.matmul(plain,key)%26
    cipher=""
    for j in ans:
        for k in j:
            cipher=cipher+chr(k+97)
    return cipher

def decrypt(cipher,key):
    #hill cipher decrypt: plain matrix =cipher matrix X (inverse(key))
    revert=""
    mod_inv=modular_mat_inverse(key)
    cipher_mat=[]
    li=[]
    i=0
    while(i<len(cipher)):
        if(i!=0 and i%len(key)==0):
                cipher_mat.append(li)
                li=[]
        li.append(alpha_map[cipher[i]])
        i+=1
    cipher_mat.append(li)
    ans=np.matmul(cipher_mat,mod_inv)%26
    for j in ans:
        for k in j:
            revert=revert+chr(k+97)

    
    return revert
def modular_mat_inverse(key):
    det= math.ceil(np.linalg.det(key))
    inv=np.linalg.inv(key)
    adj=inv*det
    mod_inv=adj*inverse[det%26]%26
    mod_inv=np.round(mod_inv)
    mod_inv=mod_inv.astype(int)
    return mod_inv
def bob_decrypt(cipher):
    #predefined key matrix
    key=[[9,7,11,13],[4,7,5,6],[2,21,14,9],[3,23,21,8]]
    revert=""
    mod_inv=modular_mat_inverse(key)
    cipher_mat=[]
    li=[]
    i=0
    while(i<len(cipher)):
        if(i!=0 and i%len(key)==0):
                cipher_mat.append(li)
                li=[]
        li.append(alpha_map[cipher[i]])
        i+=1
    cipher_mat.append(li)
    ans=np.matmul(cipher_mat,mod_inv)%26
    for j in ans:
        for k in j:
            revert=revert+chr(k+97)

    
    return revert

def known_plaintext(cipher):
    #hill cipher key=inverse(plain matrix) X (cipher matrix)
    li=[4,9,16,25,36,49,64,81,100]
    kplain="jhlnehfgcvojdxvi".lower()
    kcipher="ospyoipfbmsmdbmo"
    kplain=kplain.replace(" ","")
    ci_len=len(kcipher)
    kplain=kplain+'z'*(ci_len-len(kplain))

    if ci_len in li:
        req=int(ci_len**0.5)
    plain=[]
    ci=[]
    li_c=[]
    li=[]
    i=0
    #building plain and cipher matrix 
    while(i<len(kplain)):
            if(i!=0 and i%req==0):
                plain.append(li)
                ci.append(li_c)
                li=[]
                li_c=[]
            li.append(alpha_map[kplain[i]])
            li_c.append(alpha_map[kcipher[i]])
            i+=1
    plain.append(li)
    ci.append(li_c)
    #compute inverse of plain matrix
    plain_inv=modular_mat_inverse(plain)
    key=np.matmul(plain_inv,ci)%26

    return decrypt(cipher,key)

def choosen_plaintext(cipher):
    li=[4,9,16,25,36,49,64,81,100]
    cplain="jhlnehfgcvojdxvi".lower()
    result_cipher=encrypt(cplain)
    cplain=cplain.replace(" ","")
    ci_len=len(result_cipher)
    cplain=cplain+'z'*(ci_len-len(cplain))
    if ci_len in li:
        req=int(ci_len**0.5)
    plain=[]
    ci=[]
    li_c=[]
    li=[]
    i=0
    while(i<len(cplain)):
            if(i!=0 and i%req==0):
                plain.append(li)
                ci.append(li_c)
                li=[]
                li_c=[]
            li.append(alpha_map[cplain[i]])
            li_c.append(alpha_map[result_cipher[i]])
            i+=1
    plain.append(li)
    ci.append(li_c)
    plain_inv=modular_mat_inverse(plain)
    key=np.matmul(plain_inv,ci)%26

    return decrypt(cipher,key)

def choosen_cipher(cipher):
    li=[4,9,16,25,36,49,64,81,100]
    ccipher="ospyoipfbmsmdbmo"
    result_plain=bob_decrypt(ccipher)
    ci_len=len(ccipher)
    result_plain=result_plain+'z'*(ci_len-len(result_plain))
    if ci_len in li:
        req=int(ci_len**0.5)
    plain=[]
    ci=[]
    li_c=[]
    li=[]
    i=0
    while(i<len(result_plain)):
            if(i!=0 and i%req==0):
                plain.append(li)
                ci.append(li_c)
                li=[]
                li_c=[]
            li.append(alpha_map[result_plain[i]])
            li_c.append(alpha_map[ccipher[i]])
            i+=1
    plain.append(li)
    ci.append(li_c)
    plain_inv=modular_mat_inverse(plain)
    key=np.matmul(plain_inv,ci)%26

    return decrypt(cipher,key)

#known ciphertext attack too complex to perform  

if __name__ == "__main__":
    print("            Welcome to Hill cipher         ")
    f1=open("files/B180409CS_SAMUDRALA_2a_I.txt","r")
    plain_text=f1.readline().lower()
    plain_text=plain_text.rstrip('\n')

    #user input keys to encrypt
    #since users might end up in error by giving a key that doesn't have an inverse under module 26
    #i initialized one of the key with valid input
    
    cipher=encrypt(plain_text)
    f2=open("files/B180409CS_SAMUDRALA_2a_O.txt","w")
    f2.write("Encrypted text is:" +cipher+'\n')
    f2=open("files/B180409CS_SAMUDRALA_2a_O.txt","a")
    r1=known_plaintext(cipher)
    f2.write("Decrypted text using known-plaintext attack is: " +r1+'\n')
    r2=choosen_plaintext(cipher)
    f2.write("Decrypted text using choosen-plaintext attack is: " +r2+'\n')
    r3=choosen_cipher(cipher)
    f2.write("Decrypted text using choosen-cipher attack is: " +r3+'\n')
    
    # r4=known_cipher(cipher)
    # p=(max(r4))
    # mac2=0
    # for i in r4:
    #     if(mac2<i[0] and mac2<p[0]):
    #         mac2=i[0]
    # f2.write("The predicted decrypted text using known-cipher attack are :\n")
    # for i in r4:
    #     if(i[0]==p[0] or i[0]==mac2):
    #         f2.write("{ "+i[1] +" } " +"has "+str(i[0])+" meaningful words\n")
    
   
        




    
 