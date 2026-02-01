class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ans = nums[0]
        nums = nums[1:]
        nums.sort()
        print(nums)
        ans+=nums[0]
        ans+=nums[1]
        return ans
