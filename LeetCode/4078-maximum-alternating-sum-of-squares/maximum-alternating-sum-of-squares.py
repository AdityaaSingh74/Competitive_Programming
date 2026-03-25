class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i]<0:
                nums[i] *= -1
        nums.sort()
        
        mid = n//2

        ans = 0
        for i in nums[:mid]:
            ans -= i*i
        for i in nums[mid:n]:
            ans += i*i
        
        return ans
