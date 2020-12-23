from Affine_analysis import known_cipher as ak
from shift_analysis import known_cipher as sk
from transposition import known_cipher as tk
from math import log
import enchant

d=enchant.Dict("en_US")
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

if __name__ == "__main__":
    cipher=input().lower()
    ac=ak(cipher)
    sc=sk(cipher)
    #tc=tk(cipher)

    t1=check(ac)
    t2=check(sc)
    #t3=check(tc[1])

    # print("The predicted output maybe..\n")
    # print("{ "+ t1[1]+" }"+" has "+str(t1[0])+" meaningful words")
    # print("{ "+ t2[1]+" }"+" has "+str(t2[0])+" meaningful words")
    #print("{ "+ t3[1]+" }"+" has "+str(t3[0])+" meaningful words")
    p=(max(t1))
    mac2=0
    for i in t1:
        if(mac2<i[0] and mac2<p[0]):
            mac2=i[0]
    print("The predicted decrypted text  are :\n")
    #predict few outputs with same number of valid words as our final plain text
    for i in t1:
        if(i[0]==p[0] or i[0]==mac2):
            print("{ "+i[1] +" } " +"has "+str(i[0])+" meaningful words\n")
    p=(max(t2))
    mac2=0
    for i in t2:
        if(mac2<i[0] and mac2<p[0]):
            mac2=i[0]
   
    #predict few outputs with same number of valid words as our final plain text
    for i in t2:
        if(i[0]==p[0] or i[0]==mac2):
            print("{ "+i[1] +" } " +"has "+str(i[0])+" meaningful words\n")
