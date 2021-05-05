#User function Template for python3


class Solution:
    # Function to find largest and second largest element in the array
    def largestAndSecondLargest(self,sizeOfArray, arr):
        ma=0
        res=-1
        for i in range(1,sizeOfArray):
            if(arr[i]>arr[ma]):
                res=ma
                ma=i
            elif(arr[i]<arr[ma]):
                if(res==-1 or arr[i]>arr[res]):
                    res=i
        if res==-1:
            return arr[ma],'-1'
        return arr[ma],arr[res]

#{ 
#  Driver Code Starts
#Initial Template for Python 3


#Initial Template for Python 3

# Driver Code
def main():
    
    # testcase input
    testcases = int(input())
    
    # looping through all testcases
    while testcases > 0:
        
        sizeOfArray = int(input())
        
        arr = [int(x) for x in input().split()]
        
        li = Solution().largestAndSecondLargest(sizeOfArray, arr)
        for val in li:
            print(val, end = ' ')
        print('')
            
        testcases -= 1


if __name__ == '__main__':
    main()
# } Driver Code Ends
