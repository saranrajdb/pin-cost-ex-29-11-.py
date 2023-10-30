def pin(n):
    t=0
    while(n!=0):
        t+=n%10
        n//=10
    return t
a=11
t=11
s=1
while(s>0):
    k=pin(a)
    if(k==t):
        print(a)
        s=0
    else:
        a+=1
        

    
