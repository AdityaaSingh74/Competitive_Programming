class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        L = []
        for i in range(len(nums)):
            if nums[i] == 1:
                L.append(i)
        for j in range(0,len(L)-1):
            if (L[j+1] - L[j]) <= k:
                return False
        return True

            