class Solution:
    def twoEggDrop(self, n: int) -> int:
        k = 0
        total = 0
        
        while total < n:
            k += 1
            total += k
            
        return k