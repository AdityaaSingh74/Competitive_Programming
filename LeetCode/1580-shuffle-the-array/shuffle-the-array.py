class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans=[]
        mid = len(nums)//2
        for i in range(0,mid):
            ans.append(nums[i])
            ans.append(nums[mid + i])
        return ans