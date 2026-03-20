class Solution:
    def countDigits(self, num: int) -> int:
        snum = str(num)
        ans = 0
        for i in snum:
            if num % int(i) == 0:
                ans+=1
        return ans