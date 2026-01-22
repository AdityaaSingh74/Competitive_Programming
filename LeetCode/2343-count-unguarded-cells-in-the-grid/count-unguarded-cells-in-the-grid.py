class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        
        wall_set = set(tuple(w) for w in walls)
        gaurd_set = set(tuple(g) for g in guards)
        
        for each in guards:
            i=each[0]
            j=each[1]
            #RIGHT
            for k in range(j+1,n):
                if (i,k) in wall_set or (i,k) in gaurd_set:
                    break
                grid[i][k] = 1
            #LEFT
            for k in range(j-1,-1,-1):
                if (i,k) in wall_set or (i,k) in gaurd_set:
                    break
                grid[i][k] = 1
            #UP
            for k in range(i-1,-1,-1):
                if (k,j) in wall_set or (k,j) in gaurd_set:
                    break
                grid[k][j]=1
            #DOWN
            for k in range(i+1,m):
                if (k,j) in wall_set or (k,j) in gaurd_set:
                    break
                grid[k][j]=1
        cnt=0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    cnt+=1
        return cnt- (len(guards) + len(walls))