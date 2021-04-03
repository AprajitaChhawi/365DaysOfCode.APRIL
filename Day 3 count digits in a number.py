#User function Template for python3

class Solution:
    def countDigits(self, n):
        if n<=9:
            return 1
        ob=Solution()
        return 1+ob.countDigits(n//10)
        '''
        :param n: given number
        :return: count of digits of n.
        '''
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        print(Solution().countDigits(n))
# } Driver Code Ends
