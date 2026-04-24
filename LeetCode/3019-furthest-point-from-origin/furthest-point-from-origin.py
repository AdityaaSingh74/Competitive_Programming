class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        ans=0
        left=0
        right=0
        cnt=0
        for i in moves:
            if i=='L':
                left+=1
            if i=='R':
                right+=1
            if i=='_':
                cnt+=1
        if left>right:
            ans+=left-right+cnt
        elif left<right:
            ans+=right-left+cnt
        else:
            ans=cnt
        return ans