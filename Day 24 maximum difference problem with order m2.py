def dif(l,n):
    minval=l[0]
    res=l[1]-l[0]
    for i in range(1,n):
        res=max(res,l[i]-minval)
        minval=min(minval,l[i])
        
    return res
t=int(input())
while t:
    t=t-1
    n=int(input())
    l=list(map(int,input().split()))
    diff=dif(l,n)
    print(diff)
