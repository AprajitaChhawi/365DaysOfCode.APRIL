#User function Template for python3

class Solution:
    #Function to find element with more appearances between two elements in an array.    
    def majorityWins(self, arr, n, x, y):
        count1=0
        count2=0
        for i in arr:
            if i==x:
                count1=count1+1
            if i==y:
                count2=count2+1
        if(count1==count2):
            return min(x,y)
        elif count1>count2:
            return x
        else:
            return y
            
            
        # code here
    

#{ 
#  Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    while(T>0):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        
        x,y=map(int,input().strip().split())
        
        print(Solution().majorityWins(arr,n,x,y))
        T-=1

# } Driver Code Ends
