class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            alpha_s=sorted(s)
            alpha_t = sorted(t)
            if alpha_s==alpha_t:
                return True
        return False