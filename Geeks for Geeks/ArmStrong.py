#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        N=str(n)
        armstrong = ((int(N[0])**3)+(int(N[1])**3)+(int(N[2])**3))
        if armstrong == n:
            return True
        return False