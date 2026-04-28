class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []

        for row in grid:
            for val in row:
                arr.append(val)
        arr.sort()
        median = arr[len(arr) // 2]

        operations = 0

        for val in arr:
            if (val - arr[0]) % x != 0:
                return -1
            operations += abs(val - median) // x

        return operations
        