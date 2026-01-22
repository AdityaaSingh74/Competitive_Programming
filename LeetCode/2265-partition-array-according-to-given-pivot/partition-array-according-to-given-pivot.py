class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        L = []
        M = []
        G = []
        for i in nums:
            if i<pivot:
                L.append(i)
            elif i>pivot:
                G.append(i)
            else:
                M.append(i)
        ans = L + M + G
        return ans