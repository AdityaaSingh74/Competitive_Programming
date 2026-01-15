class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if x==0:
                return 0
            if n==0:
                return 1
            ans = power(x,n//2)
            ans = ans*ans
            if n%2 == 1:
                return ans*x
            return ans
        
        ans = power(x,abs(n))
        if n>=0:
            return ans
        else:
            return (1/ans)
            