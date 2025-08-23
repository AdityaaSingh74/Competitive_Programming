class Solution:
    def closestNumber(self, n, m):
        # code here 
        if n % m == 0:
            return n
        
        m = abs(m)
        q = n // m
        
        if n >= 0:
            a = q * m
            b = (q + 1) * m
        else:
            a = (q + 1) * m
            b = q * m
        
        da = abs(n - a)
        db = abs(n - b)
        
        if da < db:
            return a
        elif db < da:
            return b
        else:
            if abs(a) > abs(b):
                return a
            else:
                return b