class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            a = s[:i]
            b = s[i:]
            if b+a == goal:
                return True
        return False