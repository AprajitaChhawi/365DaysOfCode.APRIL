#User function Template for python3

class Solution:
    def isDigitSumPalindrome(self,N):
        s=0
        while(N>0):
            s=s+(N%10)
            N=N//10
        l=s
        rev=0
        while(s>0):
            temp=s%10
            rev=rev*10+temp
            s=s//10
        if l==rev:
            return 1
        return 0
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.isDigitSumPalindrome(N))
# } Driver Code Ends
