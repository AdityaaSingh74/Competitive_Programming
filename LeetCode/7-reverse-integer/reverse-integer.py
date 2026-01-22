class Solution:
    def reverse(self, x: int) -> int:
        strx = str(abs(x))
        print(strx)
        strx = strx[::-1]
        if int(strx)>2147483648:
            return 0
        else:
            if x<0:
                return (int(strx)*-1)
            else:
                return int(strx)