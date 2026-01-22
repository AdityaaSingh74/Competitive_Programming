class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        S = set()
        ans = []
        for i in nums:
            if i not in S:
                S.add(i)
            else:
                ans.append(i)
        return ans