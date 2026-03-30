class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        odd1 = {}
        even1 = {}
        odd2 = {}
        even2 = {}
        for i in range(0,len(s1),2):
            if s1[i] not in even1:
                even1[s1[i]] = 1
            even1[s1[i]] += 1

        for i in range(1,len(s1),2):
            if s1[i] not in odd1:
                odd1[s1[i]] = 1
            odd1[s1[i]] += 1
        
        for i in range(0,len(s2),2):
            if s2[i] not in even2:
                even2[s2[i]] = 1
            even2[s2[i]] += 1

        for i in range(1,len(s2),2):
            if s2[i] not in odd2:
                odd2[s2[i]] = 1
            odd2[s2[i]] += 1
        
        if len(odd1)!=len(odd2) or len(even1)!=len(even2):
            return False

        for i in odd1:
            if i not in odd2:
                return False
            if odd1[i] != odd2[i]:
                return False
        for i in even1:
            if i not in even2:
                return False
            if even1[i] != even2[i]:
                return False
        
        return True