#User function Template for python3
class Solution:
    def nthFibonacci (ob, n):
        temp=n+1
        l=[0]*temp
        l[0]=0
        l[1]=1
        for i in range(2,n+1):
            l[i]=(l[i-1]+l[i-2])%1000000007
        return l.pop()
        # code here 

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.nthFibonacci(n))
# } Driver Code Ends
