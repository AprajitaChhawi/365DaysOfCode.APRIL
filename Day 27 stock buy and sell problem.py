def maxprofit(arr,start,end):
    if(end<=start):
        return 0
    profit=0
    for i in range(start,end):
        for j in range(i+1,end):
            if (arr[j]>arr[i]):
                curr_profit=arr[j]-arr[i]+maxprofit(arr,j+1,end)+maxprofit(arr,start,i-1)
                profit=max(profit,curr_profit)
    return profit
t=int(input())
while t:
    t=t-1
    n=int(input())
    l=list(map(int,input().split()))
    p=maxprofit(l,0,n)
    print(p)
