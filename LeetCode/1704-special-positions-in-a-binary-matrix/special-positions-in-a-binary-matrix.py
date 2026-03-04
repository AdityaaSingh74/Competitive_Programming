class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        r = [sum(i) for i in mat]
        c = [sum(j) for j in zip(*mat)]
        return sum(mat[i][j] and r[i]==1 and c[j]==1
                   for i in range(len(mat))
                   for j in range(len(mat[0])))