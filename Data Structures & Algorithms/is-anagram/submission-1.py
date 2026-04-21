class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #hashmap O(n+m)
        if len(s)!=len(t):
            return False
        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]]=1+countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
        #brute force O(nlogn)
        # if len(s)==len(t):
        #     alpha_s=sorted(s)
        #     alpha_t = sorted(t)
        #     if alpha_s==alpha_t:
        #         return True
        # return False