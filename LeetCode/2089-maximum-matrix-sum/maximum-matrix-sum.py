class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        cnt=0
        total=0
        mini=1000000

        for i in range(row):
            for j in range(col):
                if matrix[i][j]<0:
                    cnt+=1
                    matrix[i][j]*=-1
                total+=matrix[i][j]
                if mini >= matrix[i][j]:
                    mini = matrix[i][j]

        if cnt%2 == 0:
            return total
        else:
            return (total-(mini*2))