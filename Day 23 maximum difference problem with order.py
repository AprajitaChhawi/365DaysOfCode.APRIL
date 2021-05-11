def dif(l,n):
    top=l[n-1]
    diff=0
    prev=0
    for i in range(n-1,-1,-1):
        prev=diff
        diff=top-l[i]
        if(diff<0):
            top=l[i]
            diff=0
        if(prev>diff):
            diff=prev
    return diff
t=int(input())
while t:
    t=t-1
    n=int(input())
    l=list(map(int,input().split()))
    diff=dif(l,n)
    print(diff)
