class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        left = 0
        maxx = 1

        for righ in range(n):
            while nums[righ] > k * nums[left]:
                left += 1

            maxx = max(maxx, righ - left + 1)

        return n - maxx
            
