


class Solution:
    #Back-end complete function Template for Python 3
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        l=[]
        l.append(A[N-1])
        top=0
        for i in range(N-2,-1,-1):
            if A[i]>=l[top]:
                l.append(A[i])
                top=top+1
        low=0
        while(low<top):
            l[low],l[top]=l[top],l[low]
            low=low+1
            top=top-1
        return l
        #Code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
