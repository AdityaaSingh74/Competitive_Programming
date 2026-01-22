class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        if row == 0 or col == 0:
            return []
        
        ans = []
        
        # TOP row
        for i in range(col):
            ans.append(matrix[0][i])
        
        # RIGHT column
        for i in range(1, row):
            ans.append(matrix[i][col-1])
        
        # BOTTOM row 
        if row > 1:
            for i in range(col-2, -1, -1):
                ans.append(matrix[row-1][i])
        
        # LEFT column 
        if col > 1:
            for i in range(row-2, 0, -1):
                ans.append(matrix[i][0])
        
        new = [row[1:col-1] for row in matrix[1:row-1]]
        if new and new[0]:  
            ans += self.spiralOrder(new)
        
        return ans