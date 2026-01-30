class Solution:
    def minPartitions(self, n: str) -> int:
        maxdig=-1
        for i in n:
            i = eval(i)
            if i > maxdig:
                maxdig = i
        return maxdig