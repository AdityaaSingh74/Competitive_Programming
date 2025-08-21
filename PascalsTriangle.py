class Solution:
    
        
	def nthRowOfPascalTriangle(self, n):
	    # code here
	    if n==1:
	        return [1]
	    if n==2:
	        return [1,1]
	    
        A=self.nthRowOfPascalTriangle(n-1)
        L=[]
        L.append(1)
        
        for i in range(1,n-1):
            L.append(A[i-1]+A[i])
        
        L.append(1)
        return L