def move_all(a,n):
    lp=[]
    ln=[]
    for i in a:
        if(i<0):
            ln.append(i)
        else:
            lp.append(i)
    lp.extend(ln)
    print(lp)
t=int(input())
while t:
    t=t-1
    n=int(input())
    l=list(map(int,input().split()))
    move_all(l,n)
    
