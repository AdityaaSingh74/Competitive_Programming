class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        L=0
        n=len(nums)
        R=len(nums)-1
        res = [0]*n
        for i in range(n-1,-1,-1):
            if abs(nums[L]) > abs(nums[R]):
                val=nums[L]
                L+=1
            else:
                val=nums[R]
                R-=1
            res[i] = val**2
        return res