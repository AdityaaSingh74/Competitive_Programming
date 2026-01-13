class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        i=0
        j = n-1
        
        while(i<j):
            test = numbers[i]+numbers[j]

            if (test == target):
                return [i+1,j+1]
            if (test < target):
                i+=1
            else:
                j-=1
            
