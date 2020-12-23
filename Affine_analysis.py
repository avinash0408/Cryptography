
from math import log
#english dictionary to check for meaningful words
import enchant
accept=[1,3,5,7,9,11,15,17,19,21,23,25]
inverse={1:1,3:9,5:21,7:15,9:3,11:19,15:7,17:23,19:11,21:5,
23:17,25:25}

d=enchant.Dict("en_US")
alpha="abcdefghijklmnopqrstuvwxyz"
alpha_map={x:ord(x)-97 for x in alpha}

def encrypt(plain_text):
    k1=9
    k2=11
    cipher=""
    for i in plain_text:
        if(i==" "):
            continue
        else:
            p=((alpha_map[i]*k1)+k2)%26 
            cipher=cipher+chr(p+97)
    return cipher


def decrypt(cipher,k1,k2):
    revert=""
    for i in cipher:
        p=((alpha_map[i]-k2)*inverse[k1])%26
        revert=revert+chr(p+97)
    return revert

def bob_decrypt(cipher):
    k1=9
    k2=11
    revert=""
    for i in cipher:
        p=((alpha_map[i]-k2)*inverse[k1])%26
        revert=revert+chr(p+97)
    return revert

# Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).
#function to split the sentences into meaningful words
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
    #returns list of words in the sentence
    return li
#commonly used 2 letter english words
checker=['he','in','or','is','it','by','do','my','to','of','be','at','as',
'we','so','on','no','an','if','up','hi','ok','go','up','us','am']
def check(text):
    tried=infer_spaces(text)
    ret=" ".join(tried)
    valid=0
    for i in tried:
        #check for word in the dictionary we have imported
        if(d.check(i)):
            #only i and a are meaningful one letter words
            if((len(i)==1) and (i!='a' or i!='i')):
                continue
            #if the two letter word is in our list we accept
            #since our dictionary  accepts abbrevations as meaningful
            if(len(i)==2 and not(i in checker)):
                continue
            valid=valid+1
    #valid stores the count of meaningful words in our text       
    print(ret,end="-")
    print(str(valid))
    return valid,ret

def known_cipher(cipher): 
    dic=[]
    for i in accept:
        de=""
        for j in range(26):
            de=decrypt(cipher,i,j)
            tup=check(de)
            dic.append(tup)
    #our dic contains all tuples with text along with number of meaningful words
    return dic
    
def known_plaintext(cipher):
    kplain="avinash"
    kcipher="lsfylrw"
    for i in accept:
        check=""
        for j in range(26):
            check=decrypt(kcipher,i,j)
            if(check==kplain):
                k1=i
                k2=j
                break

    return decrypt(cipher,k1,k2)



def choosen_cipher(cipher):
    ccipher="lsfylrw"
    result_plain=bob_decrypt(ccipher)
    for i in accept:
        check=""
        for j in range(26):
            check=decrypt(ccipher,i,j)
            if(check==result_plain):
                k1=i
                k2=j
                break

    return decrypt(cipher,k1,k2)

def choosen_plaintext(cipher):
    cplain="mynameisavinash"
    result_cipher=encrypt(cplain)
    #bruteforce all possible 13*26 keys. accept contais 13keys which have multiplicative inverses in z26
    for i in accept:
        check=""
        for j in range(26):
            check=decrypt(result_cipher,i,j)
            if(check==cplain):
                k1=i 
                k2=j
                break
    return decrypt(cipher,k1,k2)



if __name__ == "__main__": 
#User input for plain text
    #converting entire text to small letters
    print("            Welcome to Affine cipher         ")
    f1=open("files/B180409CS_SAMUDRALA_1a_I.txt","r")
    plain_text=f1.readline().lower()
    plain_text=plain_text.rstrip('\n')

    #user input keys to encrypt
    #since users might end up in error by giving a key that doesn't have an inverse under module 26
    #i initialized one of the key with valid input
    
    cipher=encrypt(plain_text)
    f2=open("files/B180409CS_SAMUDRALA_1a_O.txt","w")
    f2.write("Encrypted text is:" +cipher+'\n')
    f2=open("files/B180409CS_SAMUDRALA_1a_O.txt","a")
    r1=known_plaintext(cipher)
    f2.write("Decrypted text using known-plaintext attack is: " +r1+'\n')
    r2=choosen_plaintext(cipher)
    f2.write("Decrypted text using choosen-plaintext attack is: " +r2+'\n')
    r3=choosen_cipher(cipher)
    f2.write("Decrypted text using choosen-cipher attack is: " +r3+'\n')
    
    r4=known_cipher(cipher)
    #check for maximum valid words in our dictionary
    p=(max(r4))
    mac2=0
    for i in r4:
        if(mac2<i[0] and mac2<p[0]):
            mac2=i[0]
    f2.write("The predicted decrypted text using known-cipher attack are :\n")
    #predict few outputs with same number of valid words as our final plain text
    for i in r4:
        if(i[0]==p[0] or i[0]==mac2):
            f2.write("{ "+i[1] +" } " +"has "+str(i[0])+" meaningful words\n")

   








