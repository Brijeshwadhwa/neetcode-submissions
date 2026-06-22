class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t) # matching the characters that both string should be exact same. and then it will satisfied the solutio