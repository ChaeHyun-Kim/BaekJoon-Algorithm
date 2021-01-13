def apart(k,n):
    if k==0:  #0층이면 n
        return n
    if n==1:  #1호면 1
        return 1
    else:
        return(apart(k-1,n) + apart(k,n-1))
        
T = int(input())
i=1
while(True):
    k= int(input())
    n= int(input())
    print(apart(k,n))
    if T==i: break
    i+=1
