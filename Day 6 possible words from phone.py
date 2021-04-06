#User function Template for python3


class Solution:
    def pos(self,a,lst,dit,string,index,N):
        if(len(string)==N):
            lst.append(string)
            return
        cur = dit[a[index]]
        for i in range(len(cur)):
            self.pos(a,lst,dit,string+cur[i],index+1,N)
    def possibleWords(self,a,N):
        lst = []
        dit = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        self.pos(a,lst,dit,"",0,N)
        return lst
        ##Your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        a=[int(x) for x in input().strip().split()]
        ob = Solution()
        res = ob.possibleWords(a,N)
        for i in range (len (res)):
            print (res[i], end = " ") 
        
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
