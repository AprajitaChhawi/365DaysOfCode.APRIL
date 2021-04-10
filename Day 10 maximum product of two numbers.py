#User function Template for python3
class Solution:

	def maxProduct(self,arr, n):
	    if n==1:
	        return arr[0]
	    a=max(arr)
	    arr.remove(a)
	    b=max(arr)
	    return a*b
		# code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
