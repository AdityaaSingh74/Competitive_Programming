class Solution:
    def maxProduct(self, n: int) -> int:
        L = [int(i) for i in str(n)]
        L.sort()
        return L[-1]*L[-2]