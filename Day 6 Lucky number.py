#User function Template for python3
import math
class Solution:
    counter=2
    def isLucky(self, n):
        next_pos=n
        if Solution.counter>n:
            Solution.counter=2
            return True
        if n%Solution.counter==0:
            Solution.counter=2
            return False
        next_pos=next_pos-int(next_pos/Solution.counter)
        Solution.counter=Solution.counter+1
        return self.isLucky(next_pos)
        
        #RETURN True OR False

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB

if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        n=int(input())
        obj = Solution()
        if obj.isLucky(n):
            print(1)
        else:
            print(0)
        
# } Driver Code Ends
