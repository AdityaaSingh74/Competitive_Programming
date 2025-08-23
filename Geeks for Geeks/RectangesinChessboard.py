
class Solution:
    def rectanglesInChessBoard(self, N):
        # code here
        def total(N):
            if N == 1:
                return 1
            
            return (N*N*N + total(N-1))
        
      
        def squaresInChessBoard(N):
            # code here
            if N == 1:
                return 1
            
            return (N*N + squaresInChessBoard(N-1))
            
        tots = total(N)
        sqr = squaresInChessBoard(N)
        return (tots - sqr)
