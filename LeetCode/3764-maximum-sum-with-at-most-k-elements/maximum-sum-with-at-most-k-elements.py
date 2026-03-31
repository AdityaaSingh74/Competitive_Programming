class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        maxx = []
        for i in range(len(grid)):
            grid[i].sort(reverse=True)
            for j in range(0,limits[i]):
                maxx.append(grid[i][j])
        maxx.sort(reverse=True)
        return sum(maxx[:k])
