import numpy as np
#mapping alphabets to their respective numbers
alpha="abcdefghijklmnopqrstuvwxyz"
alpha_map={x:ord(x)-97 for x in alpha}
#dictionary with keys and multiplicative inverses
inverse={1:1,3:9,5:21,7:15,9:3,11:19,15:7,17:23,19:11,21:5,
23:17,25:25}

def encrypt(plain_text,key):
    #remove all the spaces
    plain_text=plain_text.replace(" ","")
    #add bogus characters at the end to divide it accurately into blocks with the length of key
    if(len(plain_text)%len(key)!=0):
        x=len(key)-(len(plain_text)%len(key))
        plain_text=plain_text+x*'z'

    plain=[]
    li=[]
    i=0
    #creating matrix for plain text
    while(i<len(plain_text)):
        if(plain_text[i]!=" "):
            if(i!=0 and i%len(key)==0):
                plain.append(li)
                li=[]
            li.append(alpha_map[plain_text[i]])
        i+=1
    plain.append(li)
    #hill cipher encrypt: cipher matrix=plain matrix X key matrix
    ans=np.matmul(plain,key)%26
    #retrieving cipher text from cipher matrix
    cipher=""
    for j in ans:
        for k in j:
            cipher=cipher+chr(k+97)
    return cipher

def decrypt(cipher,key):
    revert=""
    #finding modular inverse of key matrix to decrypt cipher
    det= np.linalg.det(key)
    inv=np.linalg.inv(key)
    adj=inv*det%26
    mod_inv=adj*inverse[det%26]%26
    mod_inv=np.round(mod_inv)
    mod_inv=mod_inv.astype(int)
    print("key inv is:")
    print(mod_inv)
    cipher_mat=[]
    # name=Matrix(key)
    # inv=name.inverse()
    li=[]
    i=0
    #building cipher matrix from cipher text
    while(i<len(cipher)):
        if(i!=0 and i%len(key)==0):
                cipher_mat.append(li)
                li=[]
        li.append(alpha_map[cipher[i]])
        i+=1
    cipher_mat.append(li)
    #hill cipher decrypt: plain matrix=cipher matrix X inverse(key matrix)
    ans=np.matmul(cipher_mat,mod_inv)%26
    #retriving plain text from plain matrix
    for j in ans:
        for k in j:
            revert=revert+chr(k+97)    
    return revert
    

if __name__ == "__main__":
    #predefined key
    key=[[9,7,11,13],[4,7,5,6],[2,21,14,9],[3,23,21,8]]
    #open file to read plain text
    f1=open("files/B180409CS_SAMUDRALA_2_I.txt","r")
    plain_text=input("enter plain:").lower()
    plain_text=plain_text.rstrip('\n')
    #encrypt
    cipher=encrypt(plain_text,key)
    f2=open("files/B180409CS_SAMUDRALA_2_O.txt","w")
    print("Encrypted text is:" +cipher+'\n')
    #decrypt
    revert=decrypt(cipher,key)
    f2=open("files/B180409CS_SAMUDRALA_2_O.txt","a")
    print("Decrypted text is:" +revert)
   
        




    
