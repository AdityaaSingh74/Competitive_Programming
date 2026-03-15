class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for i in queries:
            cnt=0
            for j in points:
                val = (((i[0] - j[0])**2) + ((i[1] - j[1])**2))**0.5
                if val<=i[2]:
                    cnt+=1
            ans.append(cnt)
        return ans