import numpy as np
import math
alpha="abcdefghijklmnopqrstuvwxyz"
alpha_map={x:ord(x)-97 for x in alpha}
accept=[1,3,5,7,9,11,15,17,19,21,23,25]
inverse={1:1,3:9,5:21,7:15,9:3,11:19,15:7,17:23,19:11,21:5,
23:17,25:25}

def encrypt(plain_text):
    plain_text=plain_text.lower()
    key=[[9,7,11,13],[4,7,5,6],[2,21,14,9],[3,23,21,8]]
    print(key)
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
    name=Matrix(key)
    inv=name.inverse()
    return inv%26

def bob_decrypt(cipher):
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
# def known_cipher(cipher): 
#     maxi=0
#     curr=""
#     for i in accept:
#         de=""
#         for j in range(26):
#             de=decrypt(cipher,i,j)
#             p=check(de)
#             if(p>maxi):
#                 maxi=p
#                 curr=de

#     return curr
 
def known_plaintext(cipher):
    li=[4,9,16,25,36,49,64,81,100]
    kplain="jhlnehfgcvojdxvi".lower()
    kcipher="ospyoipfbmsmdbmo"
    kplain=kplain.replace(" ","")
    ci_len=len(kcipher)
    kplain=kplain+'z'*(ci_len-len(kplain))
    req=4
    if ci_len in li:
        req=int(ci_len**0.5)
    plain=[]
    ci=[]
    li_c=[]
    li=[]
    i=0
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
    print(plain)
    plain_inv=modular_mat_inverse(plain)
    print(plain_inv)
    key=np.matmul(plain_inv,ci)%26

    return decrypt(cipher,key)




    

if __name__ == "__main__":
    plain_text=input("Enter text to encrypt :\n")
    cipher=encrypt(plain_text)
    print("Encrypted text is:" +cipher)
    r1=known_plaintext(cipher)
    print("Decrypted text using known-plaintext attack is: " +r1)
    # r2=choosen_plaintext(cipher)
    # print("Decrypted text using choosen-plaintext attack is: " +r2)
    # r3=choosen_cipher(cipher)
    # print("Decrypted text using choosen-cipher attack is: " +r3)
    # r4=known_cipher(cipher)
    # print("Decrypted text using known-cipher attack is: " +r4)
    
   
        




    
 