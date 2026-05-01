class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)
        total_sum = sum(nums)
        
        f0 = 0
        for i in range(n):
            f0 += i * nums[i]
        
        max_val = f0
        current = f0
        
        for k in range(1, n):
            current = current + total_sum - n * nums[n - k]
            max_val = max(max_val, current)
        
        return max_val