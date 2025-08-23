
def isvalid(n,arr):
    for i in range(n):
        for j in range(n):
            n = i+j
            if n%2 == 0 and arr[i][j] != 1:
                return False
            if n%2 != 0 and arr[i][j] != 0:
                return False
    return True

arr = [ [ 1, 0 ], [ 0, 1 ] ]
size = len(arr)
print(isvalid(size,arr))