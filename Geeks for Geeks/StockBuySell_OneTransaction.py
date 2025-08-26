class Solution:
    def maximumProfit(self, prices):
        # code here
        prft = 0
        mini=prices[0]
        for i in range(0,len(prices)):
            if prices[i] < mini :
                mini = prices[i]
            if prft < (prices[i]-mini):
                prft = prices[i]-mini
        
        return prft