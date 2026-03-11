class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n==0:
            return 1
        s = len(bin(n)[2:])
        ans = (2**s - n)
        return ans-1
        