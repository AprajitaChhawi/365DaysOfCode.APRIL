def remove(l):
    temp=l[0]
    for i in range(1,n):
        l[i-1]=l[i]
    l[n-1]=temp
t=int(input())
while t:
    t=t-1
    n=int(input())
    l=list(map(int,input().split()))
    remove(l)
    print(l)
    
