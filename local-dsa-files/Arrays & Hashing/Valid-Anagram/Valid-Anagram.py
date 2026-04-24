class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):       # different lengths → can't be anagrams
            return False

        count_s, count_t = {}, {}

        for i in range(len(s)):    # single loop since lengths are equal
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1

        return count_s == count_t

        # --- Alternative: Frequency Array — O(n), no hashing ---
        # count = [0] * 26
        # for i in range(len(s)):
        #     count[ord(s[i]) - ord('a')] += 1
        #     count[ord(t[i]) - ord('a')] -= 1
        # return all(v == 0 for v in count)

        # --- Alternative: Sorting — O(n log n) ---
        # return sorted(s) == sorted(t)


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("racecar", "carrace", True),
        ("jar",     "jam",     False),
        ("anagram", "nagaram", True),
        ("rat",     "car",     False),
        ("",        "",        True),
        ("a",       "a",       True),
        ("a",       "b",       False),
        ("ab",      "a",       False),
    ]

    print("Valid Anagram")
    print("Time: O(n) | Space: O(1)\n")

    for i, (s, t, expected) in enumerate(tests, 1):
        result = sol.isAnagram(s, t)
        status = "✅" if result == expected else "❌"
        print(f"  {status} Test {i}: s=\"{s}\", t=\"{t}\" → {result}")
