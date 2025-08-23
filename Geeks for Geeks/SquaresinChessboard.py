
class Solution:
    def squaresInChessBoard(self, N):
        # code here
        if N == 1:
            return 1
        
        return (N*N + self.squaresInChessBoard(N-1))