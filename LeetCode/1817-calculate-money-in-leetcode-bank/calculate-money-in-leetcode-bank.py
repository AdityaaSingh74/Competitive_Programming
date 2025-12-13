class Solution:
    def totalMoney(self, n: int) -> int:
        amt=0
        weeks = n//7
        days = n%7
        for i in range(0,weeks):
            amt+=28+(7*i)
        for i in range(weeks+1,weeks+days+1):
            amt+=i
            
        return amt