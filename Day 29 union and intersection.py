def union(a1,a2,n,m):
    i=0
    j=0
    while i<n and j<m:
        if(a1[i]>a2[j]):
            print(a1[i],end=" ")
            i=i+1
        elif(a1[i]<a2[j]):
            print(a2[j],end=" ")
            i=i+1
        else:
            print(a1[i],end=" ")
            i=i+1
            j=j+1
t=int(input())
while t:
    t=t-1
    n=int(input())
    m=int(input())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    union(l1,l2,n,m)
