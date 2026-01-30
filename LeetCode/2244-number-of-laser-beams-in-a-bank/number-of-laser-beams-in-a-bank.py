class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        rows = []
        for i in bank:
            lasers=0
            for j in i:
                if j=='1':
                    lasers+=1
            if lasers != 0:
                rows.append(lasers)
        n = len(rows)
        ans = 0
        for i in range(1,n):
            ans+=(rows[i-1]*rows[i])
        return ans