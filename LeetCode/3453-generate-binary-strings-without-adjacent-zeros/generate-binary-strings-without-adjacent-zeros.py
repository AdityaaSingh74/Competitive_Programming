class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n==1:
            return ['0','1']
        
        ans=[]
        for i in range(0,2**n):
            Binum = bin(i)[2:].zfill(n)
            if '00' not in Binum:
                ans.append(Binum)
        return ans