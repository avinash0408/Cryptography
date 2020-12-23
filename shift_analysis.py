from math import log
import enchant


alpha="abcdefghijklmnopqrstuvwxyz"
alpha_map={x:ord(x)-97 for x in alpha}

d=enchant.Dict("en_US")
def encrypt(plain_text):
    key=8
    plain_text=plain_text.lower()
    plain=[]
    for i in plain_text:
        if(i==" "):
            continue
        plain.append(alpha_map[i])
    cipher=""
    for i in plain:
        cipher=cipher+chr((97+((i+key)%26)))
    return cipher

def decrypt(cipher,key):
    cip=[]
    for i in cipher:
        cip.append(alpha_map[i])
    revert=""
    for i in cip:
        revert=revert+chr(97+(i-key)%26)
    return revert

def bob_decrypt(cipher):
    key=8
    cip=[]
    for i in cipher:
        cip.append(alpha_map[i])
    revert=""
    for i in cip:
        revert=revert+chr(97+(i-key)%26)
    return revert
def known_plaintext(cipher):
    kplain="mynameisavinash"
    kcipher="ugviumqaidqviap"
    kplain=kplain.lower() 
    key=alpha_map[kcipher[0]]-alpha_map[kplain[0]]
    return decrypt(cipher,key)

def choosen_plaintext(cipher):
    cplain="MySELF avinash how are you"
    cplain=cplain.lower()
    result_cipher=encrypt(cplain)
    key=alpha_map[result_cipher[0]]-alpha_map[cplain[0]]
    return decrypt(cipher,key)

def choosen_cipher(cipher):
    ccipher="hsgjfgkhlsdjkg"
    result_plain=bob_decrypt(ccipher)
    key=alpha_map[ccipher[0]]-alpha_map[result_plain[0]]
    return decrypt(cipher,key)
    


# Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).

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
def check(text):
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
    return valid,ret

def known_cipher(cipher):
    dic=[]
    #bruteforce all 26keys
    for i in range(26):
        de=""
        for j in cipher:
            de=de+chr(97+(alpha_map[j]-i)%26)
        tup=check(de)
        dic.append(tup)
    #dic contains each decrypted text with respective #.of meaningful words
    return dic

if __name__ == "__main__":

    print("      Welcome to Shift Cipher    ")
    f1=open("files/B180409CS_SAMUDRALA_3a_I.txt","r")
    plain_text=f1.readline().lower()
    plain_text=plain_text.rstrip('\n')
    cipher=encrypt(plain_text)
    f2=open("files/B180409CS_SAMUDRALA_3a_O.txt","w")
    f2.write("Encrypted text is:" +cipher+'\n')
    r1=known_plaintext(cipher)
    f2=open("files/B180409CS_SAMUDRALA_3a_O.txt","a")
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