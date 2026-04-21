class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #brute force
        while len(s) == len(t):
            if sorted(s) == sorted(t):
                return True
            else:
                return False
        return False
        