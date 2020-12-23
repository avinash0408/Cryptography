def keyless_encrypt(plain_text):
     cipher=""
     even=[]
     odd=[]
     plain=""
     #read even places first and then odd places
     for i in range(len(plain_text)):
         #skip spaces
        if(plain_text[i]==" "):
             pass
        else:
            plain=plain+plain_text[i]

     for i in range(len(plain)):
            if(i%2):
                #getting odd index values
                odd.append(plain[i])
            else:
                #getting even index values
                even.append(plain[i])
    #joining together
     cipher=cipher.join(even)
     p=""
     p=p.join(odd)
     cipher=cipher+p
     return cipher
         
def keyed_encrypt(plain_text,k):
    cipher=""
    block=[]
    entire=[]
    #adding bogus characters to divide plain text into blocks of length of key
    if(len(plain_text)%len(k)!=0):
        x=len(k)-(len(plain_text)%len(k))
        plain_text=plain_text+x*'z'
    #dividing into blocks of length of key
    for i in range(len(plain_text)):
        if(i!=0 and i%len(key)==0):
            entire.append(block)
            block=[]
        block.append(plain_text[i])
    entire.append(block)
    #building cipher as per values in key
    for i in entire:
        for j in range(len(i)):
            cipher=cipher+i[k[j]]

    return cipher

def keyless_decrypt(cipher):
    revert=""
    first=[]
    second=[]
    #keyless decrypt: first half have even places and next have odd places
    for i in range(len(cipher)):
        if(i<len(cipher)/2):
            first.append(cipher[i])
        else:
            second.append(cipher[i])
    #join even and odd places alternatively to build back plain text
    for i in range(max(len(first),len(second))):
        if(i<len(first) and i<len(second)):
            revert=revert+first[i]+second[i]
        elif(i<len(first)):
            revert=revert+first[i]
        else:
            revert=revert+second[i]
    return revert

def get_key(keys,val): 
    for key, value in keys.items(): 
         if val == value: 
             return key 
def key_decrypt(cipher,key):
    revert=''
    block=[]
    entire=[]
    #divide cipher into blocks of length of key
    for i in range(len(cipher)):
        if(i!=0 and i%len(key)==0):
            entire.append(block)
            block=[]
        block.append(cipher[i])
    entire.append(block)
    #building back plain text from cipher using the mapping from keys
    for i in entire:
        for j in range(len(i)):
            revert=revert+i[get_key(key,j)]
    
    return revert

if __name__ == "__main__":
    f1=open("files/B180409CS_SAMUDRALA_5_I.txt","r")
    plain_text=input("enter plain:").lower()
    plain_text= plain_text.rstrip('\n')
    plain_text=plain_text.replace(" ","")
    keyless_cipher=keyless_encrypt(plain_text)

    f2=open("files/B180409CS_SAMUDRALA_5_O.txt","w")
    print("Encrypted text using keyless method is: "+keyless_cipher+'\n')
    #key for keyed transposition cipher
    key={0:3,1:1,2:4,3:5,4:2}
    for i in range(len(key)):
        key[i]=key[i]-1
    key_cipher=keyed_encrypt(plain_text,key)
    f2=open("files/B180409CS_SAMUDRALA_5_O.txt","a")
    print("Encrypted text using keyed method is: "+key_cipher+'\n')

    print("Decrypted text using keyless method is: "+keyless_decrypt(keyless_cipher)+'\n')
    
    print("Decrypted text using keyed method is: "+key_decrypt(key_cipher,key)+'\n')



