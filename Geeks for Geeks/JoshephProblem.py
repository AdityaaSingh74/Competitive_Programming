class Solution:
    def josephus(self,n,k):
        #code here
        i=1
        res=0
        while(i<= n):
            res= (res+k)% i
            i+= 1
        return res + 1
    
    