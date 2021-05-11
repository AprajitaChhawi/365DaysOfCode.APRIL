class Solution:
    def reverse(self,arr,low,high):
        while(low<high):
            arr[low],arr[high]=arr[high],arr[low]
            low=low+1
            high=high-1
    def leftRotate(self, arr, k, n):
        if k>=n:
            k=k%n
        ob=Solution()
        ob.reverse(arr,0,k-1)
        ob.reverse(arr,k,n-1)
        ob.reverse(arr,0,n-1)
        
        # Your code goes here

#{ 
#  Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        k=l[1]
        a = list(map(int,input().split()))
        ob = Solution()
        ob.leftRotate(a,k,n)
        print(*a)
# } Driver Code Ends
