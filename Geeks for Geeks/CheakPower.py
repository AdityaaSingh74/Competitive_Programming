#User function Template for python3
class Solution:
    def isPowerOfAnother (ob,X,Y):
        # code here 
        if X == 1:
            return Y == 1
        
        while Y > 1:
            if Y % X != 0:
                return False
            Y //= X
        
        return True
        