#User function Template for python3
class Solution:

    def calculateFraction(self, a, b):
        # Code Here
        if a == 0:
            return "0"
    
        result = []
        
        if (a < 0) ^ (b < 0):
            result.append("-")
        
        a, b = abs(a), abs(b)
        
        result.append(str(a // b))
        a %= b
        
        if a == 0:
            return "".join(result)
        
        result.append(".")
        
        remainders = {}
        
        while a != 0:
            if a in remainders:
                idx = remainders[a]
                return "".join(result[:idx]) + "(" + "".join(result[idx:]) + ")"
            
            remainders[a] = len(result)
            a *= 10
            result.append(str(a // b))
            a %= b
        
        return "".join(result)