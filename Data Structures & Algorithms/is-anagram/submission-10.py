class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):       # quick exit — different lengths can't be anagrams
            return False

        count_s = {}
        count_t = {}

        for i in range(len(s)):    # single loop since lengths are equal
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1

        return count_s == count_t

        # count_s = {}
        # count_t = {}

        # for char in s:
        #     if char not in count_s:
        #         count_s[char] = 1
        #     else:
        #         count_s[char] +=1
        # for char in t:
        #     if char not in count_t:
        #         count_t[char] = 1
        #     else:
        #         count_t[char] +=1
        # return count_s == count_t           

        # Brute Force
        # if sorted(s) == sorted(t):
        #     return True
        # else:
        #     return False