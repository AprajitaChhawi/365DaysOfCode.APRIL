#User function Template for python3

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        d={}
        for i in A:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        for i in B:
            if i not in d or d[i]<=0:
                return False
            else:
                d[i]=d[i]-1
        return True
        
        #return: True or False
        
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        
        A = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        B = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        ob=Solution()
        if ob.check(A,B,N):
            print(1)
        else:
            print(0)
        
                
                
# } Driver Code Ends
