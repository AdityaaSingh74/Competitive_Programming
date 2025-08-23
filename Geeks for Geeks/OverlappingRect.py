#User function Template for python3

class Solution:
    
    def doOverlap(self, L1, R1, L2, R2):
        if ((R1[0] < L2[0]) or (R2[0] < L1[0])):
            return 0

        if ((L1[1] < R2[1]) or (L2[1] < R1[1])):
            return 0
    
        return 1