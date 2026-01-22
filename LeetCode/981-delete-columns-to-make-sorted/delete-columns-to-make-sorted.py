class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt=0
        row = len(strs)
        col = len(strs[0])
        for i in range(col):
            k = ord(strs[0][i])
            tag=False
            for j in range(1,row):
                if k<=ord(strs[j][i]):
                    k=ord(strs[j][i])
                else:
                    tag=True
                    break
            if tag==True:
                cnt+=1
                continue
            
        return cnt