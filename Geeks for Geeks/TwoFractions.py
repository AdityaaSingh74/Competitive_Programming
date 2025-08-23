def addFraction(num1, den1, num2, den2):
    #Code here
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    numerator = num1 * den2 + num2 * den1
    denominator = den1 * den2
    
    common = gcd(numerator, denominator)
    numerator //= common
    denominator //= common
    
    print(f"{numerator}/{denominator}")
    
    