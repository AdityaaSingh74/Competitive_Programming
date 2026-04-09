class Solution:
    def countAsterisks(self, s: str) -> int:
        stk = []
        cnt=0
        for i in s:
            if stk != []:
                if i == '|':
                    stk = []
                continue
            if i == '|':
                stk = ['|']
                continue
            if i=='*':
                cnt+=1
        return cnt