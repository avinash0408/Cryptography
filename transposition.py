from itertools import permutations
from math import log
import enchant

d=enchant.Dict("en_US")
def keyless_encrypt(plain_text):
     cipher=""
     even=[]
     odd=[]
     plain=""
     for i in range(len(plain_text)):
        if(plain_text[i]==" "):
             pass
        else:
            plain=plain+plain_text[i]

     for i in range(len(plain)):
            if(i%2):
                odd.append(plain[i])
            else:
                even.append(plain[i])
     cipher=cipher.join(even)
     p=""
     p=p.join(odd)
     cipher=cipher+p
     return cipher
         
def keyed_encrypt(plain_text):
    k={0:3,1:1,2:4,3:5,4:2}
    plain_text=plain_text.replace(" ","")
    for i in range(len(k)):
        k[i]=k[i]-1
    cipher=""
    block=[]
    entire=[]
    if(len(plain_text)%len(k)!=0):
        x=len(k)-(len(plain_text)%len(k))
        plain_text=plain_text+x*'z'
    for i in range(len(plain_text)):
        if(i!=0 and i%len(k)==0):
            entire.append(block)
            block=[]
        block.append(plain_text[i])
    entire.append(block)
    for i in entire:
        for j in range(len(i)):
            cipher=cipher+i[k[j]]

    return cipher

def keyless_decrypt(cipher):
    revert=""
    first=[]
    second=[]
    for i in range(len(cipher)):
        if(i<len(cipher)/2):
            first.append(cipher[i])
        else:
            second.append(cipher[i])
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
def bob_key_decrypt(cipher):
    key={0:3,1:1,2:4,3:5,4:2}
    for i in range(len(key)):
        key[i]=key[i]-1
    revert=''
    block=[]
    entire=[]
    for i in range(len(cipher)):
        if(i!=0 and i%len(key)==0):
            entire.append(block)
            block=[]
        block.append(cipher[i])
    entire.append(block)
    for i in entire:
        for j in range(len(i)):
            revert=revert+i[get_key(key,j)]
    
    return revert
def key_decrypt(cipher,key):
    revert=''
    block=[]
    entire=[]
    for i in range(len(cipher)):
        if(i!=0 and i%len(key)==0):
            entire.append(block)
            block=[]
        block.append(cipher[i])
    entire.append(block)
    for i in entire:
        for j in range(len(i)):
            revert=revert+i[get_key(key,j)]
    
    return revert

def known_plaintext(cipher):
    kplain="kston"
    kcipher='tkons'
    key={}
    for i in range(len(kplain)):
        key[i]=kplain.index(kcipher[i])
    return key_decrypt(cipher,key)

def choosen_plaintext(cipher):
    cplain="kston"
    result_cipher=keyed_encrypt(cplain)
    key={}
    for i in range(len(cplain)):
        key[i]=cplain.index(result_cipher[i])
    return key_decrypt(cipher,key)
def choosen_cipher(cipher):
    ccipher='tkons'
    result_plain=bob_key_decrypt(ccipher)
    key={}
    for i in range(len(result_plain)):
        key[i]=result_plain.index(ccipher[i])
    return key_decrypt(cipher,key)

def infer_spaces(s):
    words = open("words.txt").read().split()
    wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
    maxword = max(len(x) for x in words)
    # Find the best match for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k

    st= " ".join(reversed(out))
    li=st.split(" ")
    return li
    
checker=['he','in','or','is','it','by','do','my','to','of','be','at','as',
'we','so','on','no','an','if','up','hi','ok','go','up','us','am']
def checky(text):
    tried=infer_spaces(text)
    ret=" ".join(tried)
    valid=0
    for i in tried:
        if(d.check(i)):
            if((len(i)==1) and (i!='a' or i!='i')):
                continue
            if(len(i)==2 and not(i in checker)):
                continue
            valid=valid+1       
    print(ret,end="-")
    print(str(valid))
    #if all words in sentence are meaningful then return -1
    if(valid==len(tried)):
        return -1
    return valid

def make_key(li):
    key={}
    for i in range(len(li)):
        if(i==li[i]):
            return {}
        key[i]=li[i]
    return key

def known_cipher(cipher):
    flag=1
    fin=[]
    #since we dont the lenght of key try all lenghts from 2 to 7
    for p in range(2,7):
        ar=[i for i in range(0,p+1)]
        #returns all possible permutations in which our key exists
        per=permutations(ar)
        per_li=list(list(k) for k in per)
        for i in per_li:
            l=make_key(i)
            if(l):
                fin.append(l)
    maxi=0
    curr=0
    key={}
    for i in fin:
        try:
            tried=key_decrypt(cipher,i)
            curr=checky(tried)
            print(tried,end="-")
            print(curr)
            if(curr==-1):
                flag=0
                print("{ "+ tried+ " }"+" - "+str(curr))
                return (i,tried)
               
        except:
            pass
        if(maxi<curr):
                maxi=curr
                key=i
        
    if(flag):
        print(key)
        print(key_decrypt(cipher,key))
        return (key,key_decrypt(cipher,key))
        

if __name__ == "__main__":
    f1=open("files/B180409CS_SAMUDRALA_5a_I.txt","r")
    plain_text=input("Enter text:").lower()
    keyless_cipher=keyless_encrypt(plain_text.replace(" ",""))
    f2=open("files/B180409CS_SAMUDRALA_5a_O.txt","w")
    f2.write("Encrypted text using keyless method is: "+keyless_cipher+'\n')
    key_cipher=keyed_encrypt(plain_text)
    f2=open("files/B180409CS_SAMUDRALA_5a_O.txt","a")
    f2.write("Encrypted text using keyed method is: "+key_cipher+'\n')
    f2.write("for keyless all attacks are same..\n" )
    f2.write("Decrypted text using keyless method is: "+keyless_decrypt(keyless_cipher)+'\n')
    

    r1=known_plaintext(key_cipher)
    f2.write("Decrypted text using known-plaintext attack is: " +r1+'\n')
    r2=choosen_plaintext(key_cipher)
    f2.write("Decrypted text using choosen-plaintext attack is: " +r2+'\n')
    r3=choosen_cipher(key_cipher)
    f2.write("Decrypted text using choosen-cipher attack is: " +r3+'\n')
    known_cipher(key_cipher)
    # f2.write("Decrypted text using known-cipher attack is: " +r3+'\n')
    # f2.write("Final answer maybe...\n")
    # f2.write(r4[1]+ " with the key "+str(r4[0])+ '\n')

