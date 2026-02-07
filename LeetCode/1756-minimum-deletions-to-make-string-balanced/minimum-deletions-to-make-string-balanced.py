class Solution:
    def minimumDeletions(self, s: str) -> int:
        b=0
        dele = 0

        for i in s:
            if i=='b':
                b+=1
            else:
                dele = min(dele+1,b)
        return dele
