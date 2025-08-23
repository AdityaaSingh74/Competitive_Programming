class Solution:
    def isPalindrome(self, n):
        S = str(n)
        if S == S[::-1]:
            return True
        return False

