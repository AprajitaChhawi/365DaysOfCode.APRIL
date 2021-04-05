# User function Template for python3

class Solution:
    def toh(self, N, fromm, to, aux):
        if N==1:
            print("move disk 1 from rod "+str(fromm)+" to rod "+str(to))
            return 1
        ob=Solution()
        ob.toh(N-1,fromm,aux,to)
        print("move disk "+str(N)+" from rod "+str(fromm)+" to rod "+str(to))
        ob.toh(N-1,aux,to,fromm)
        return (2**N)-1
    
        
        # Your code here

#{ 
#  Driver Code Starts
# Initial Template for Python 3


import math


def main():

    T = int(input())

    while(T > 0):
        N = int(input())
        ob = Solution()
        print(ob.toh(N, 1, 3, 2))
        T -= 1
if __name__ == "__main__":
    main()


# } Driver Code Ends
