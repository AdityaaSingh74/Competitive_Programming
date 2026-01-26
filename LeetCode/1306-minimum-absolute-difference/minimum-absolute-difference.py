class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans=[]
        minabs = 100000000
        for i in range(1,len(arr)):
            curr = abs(arr[i]-arr[i-1])
            if curr < minabs:
                minabs = curr
                ans=[]
            if curr == minabs:
                ans.append([arr[i-1],arr[i]])
        return ans