#User function Template for python3
class Solution:
    def repeatedSumOfDigits (self,N):
        # code here
        if N == 0:
            return 0
        return 1 + (N - 1) % 9