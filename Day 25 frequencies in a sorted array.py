def frequency(a,n):
    prev=a[0]
    count=1
    for i in range(1,n):
        if(a[i]==prev):
            count=count+1
            prev=a[i]
        else:
            print(prev,count)
            prev=a[i]
            count=1
    print(prev,count)
t=int(input())
while t:
    t=t-1
    n=int(input())
    l=list(map(int,input().split()))
    frequency(l,n)
