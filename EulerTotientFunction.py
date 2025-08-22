class Solution:
    def etf(self, n):
        # code here
        def PrimeFactors(num):
            prime = []
            i=3
            while (num % 2 == 0):
                prime.append(2)
                num = num // 2
            while(i*i <= n):
                while (num%i == 0):
                    prime.append(i)
                    num = num//i
                i+=2 
            
            if (num > 2):
                prime.append(num)
            
            return set(prime)
        
        L = PrimeFactors(n)
        res=n
        for i in L:
            res *= (1 - (1/i))
        
        if res - int(res) > 0.5:
            res = int(res)+1
        
        return int(res)
                
        