#User function Template for python3

class Solution:
    def maxPoint(self, N, K, A, B):
        s=[]
        for i in range(N):
            s.append((K//A[i])*B[i])
        return max(s)
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, K = [int(x) for x in input().split()]
        A = input().split()
        B = input().split()
        for i in range(N):
            A[i] = int(A[i])
            B[i] = int(B[i])
        
        ob = Solution()
        print(ob.maxPoint(N, K, A, B))
# } Driver Code Ends
