class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        cnt = 0
        for i in range(1,len(points)):
            start = points[i-1]
            end = points[i]
            diffX = abs(start[0]-end[0])
            diffY = abs((start[1]) - (end[1]))
            if diffX > diffY:
                cnt+= diffY
                cnt+=(diffX-diffY)
            else:
                cnt+= diffX
                cnt+=(diffY-diffX)
        return cnt
