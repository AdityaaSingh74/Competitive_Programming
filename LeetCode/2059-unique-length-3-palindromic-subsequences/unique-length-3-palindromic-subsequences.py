class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        def lastiteration(L,x):
            for i in range(len(L)-1,-1,-1):
                if L[i] == x:
                    return i
        
        ans = 0
        no_retry = set()
        for i in range(len(s)):
            if s[i] in no_retry:
                continue
            no_retry.add(s[i])
            j = lastiteration(s,s[i])
            uniq = set()
            for k in s[i+1:j]:
                uniq.add(k)
            ans += len(uniq)
        return ans
            