class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = set()
        for i in sentence:
            alphabet.add(i)
        if len(alphabet) == 26:
            return True
        return False