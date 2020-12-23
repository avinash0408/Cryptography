def modInverse(a, m): 
    a = a % m 
    for x in range(1, m): 
        if ((a * x) % m == 1): 
            return x 
    return 1

def binaryToDecimal(n): 
    return int(n,2) 
if __name__ == "__main__":
    # print("enter values of b:",end="\n")
    # b=list(int(i) for i in input().split())
    # print("You can choose n>{}".format(sum(b)))
    # n=int(input("Enter n:"))
    # r=int(input("Enter r:"))
   
    # t=[]
    # for i in range(len(b)):
    #     t.append(b[i]*r%n)
    # print("t before per:",end="\n")
    # print(t)
    # print("enter perm list",end="\n")
    # p=list(int(i) for i in input().split())

    # a=[]
    # for i in range(len(b)):
    #     a.append(t[p[i]-1])
    # print("t after per:",end="\n")
    # print(a)
    a=[543, 407, 223,703,259, 781, 409]

    print("Choose your msg: ",end="\n")
    m=ord(input())
    print(m)
    m=bin(m).replace("0b","")
    print(m)
    print("Enter the mesg now",end="\n")
    msg=[int(i) for i in input().split()]
    sum=0
    for i in range(len(a)):
        sum=sum+a[i]*msg[i]
    print("cipher is:{}".format(sum))
    print("inv of r is :{}".format(modInverse(r,n)),end="\n")
    s_dash=sum*modInverse(r,n)%n
    print("Decryption sum is:{}".format(s_dash),end="\n")

    key=[]
    for i in range(len(b)):
        if(b[len(b)-i-1]<=s_dash):
            key.append(1)
            s_dash=s_dash-b[len(b)-i-1]
        
        else:
            key.append(0)
    key.reverse()
    f_k=[]
    res=""
    for i in range(len(key)):
        f_k.append(key[p[i]-1])
    print("final result is:{}".format(f_k),end="\n")
    res=input("Enter result")

    print("Decrypted is :{}".format(binaryToDecimal(res)),end="\n")

