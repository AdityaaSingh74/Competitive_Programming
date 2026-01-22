class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d={}
        n=(len(nums)//2)
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d.keys():
            if (d[i]==n):
                return i
            