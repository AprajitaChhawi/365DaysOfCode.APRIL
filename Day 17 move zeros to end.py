#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr, n):
	    count=0
	    for i in range(n):
	        if arr[i]==0:
	            count=count+1
	    res=0
	    for i in range(n):
	        if arr[i]!=0:
	            arr[res]=arr[i]
	            res=res+1
	    while(count):
	        arr[res]=0
	        res=res+1
	        count=count-1
	    return arr
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
        ans = ob.pushZerosToEnd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
