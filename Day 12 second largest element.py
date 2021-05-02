
class Solution:
    def print2largest(self,A,N): 
        res=-1
        largest=0
        for i in range(1,N):
            if (A[i]>A[largest]):
                res=largest
                largest=i
            elif(A[i]!=A[largest]):
                if(res==-1 or A[i]>A[res]):
                    res=i
        if res==-1:
            return -1
        return A[res]
        #code here


#{ 
#  Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ob = Solution()
    print(ob.print2largest(a,n))
# } Driver Code Ends
