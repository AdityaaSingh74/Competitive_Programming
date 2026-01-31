class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i=ord(target)
        while (i<=122):
            i+=1
            if chr(i) in letters:
                return chr(i)
        return letters[0]