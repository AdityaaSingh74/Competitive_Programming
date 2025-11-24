class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        n = ""
        for i in nums:
            n += str(i)
            if (int(n,2)%5 == 0):
                ans.append(True)
            else:
                ans.append(False)
        return ans
        