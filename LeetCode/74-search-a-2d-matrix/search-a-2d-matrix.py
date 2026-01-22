class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        """ for i in range(row):
            if i!=row and matrix[i+1][0] > target:
                for j in range(col):
                    if (matrix[i][j]) == target:
                        return True
            continue
        return False """

        
        for i in range(0,row):
            for j in range(0,col):
                if (matrix[i][j]) == target:
                    return True
        return False

