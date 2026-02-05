class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        for i in range(len(nums)):
            temp = nums[i]
            j = (i+temp)%n
            res[i] = nums[j] 
        return res