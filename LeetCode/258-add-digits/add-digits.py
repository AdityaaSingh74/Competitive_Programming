class Solution:
    def addDigits(self, num: int) -> int:
        summ = 0
        while num >= 10:
            while num != 0:
                summ+=(num%10)
                num = num//10
            num = summ
            summ = 0
        return num