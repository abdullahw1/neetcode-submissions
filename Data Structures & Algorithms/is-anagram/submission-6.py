class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #optimal solution using hashmap
        if len(s) != len(t):
            return False
        count_s = {}
        count_t = {}
        for char in s:
            if char in count_s:
                count_s[char] +=1
            else:
                count_s[char] =1
        for char in t:
            if char in count_t:
                count_t[char] +=1
            else:
                 count_t[char] =1
        return count_s == count_t
        # #brute force
        # while len(s) == len(t):
        #     if sorted(s) == sorted(t):
        #         return True
        #     else:
        #         return False
        # return False
        