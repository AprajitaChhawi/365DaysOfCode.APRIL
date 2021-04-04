#User function Template for python3

class Solution:
	def is_power_of_eight(self, n):
	    a=0
	    z=0
	    while(n):
	        if(n&1):
	            a=a+1
	        else:
	            z=z+1
	        n=n>>1
	    if a==1 and z%3==0:
	        return "Yes"
	    return "No"
		# Code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.is_power_of_eight(n)
		print(ans)


# } Driver Code Ends
