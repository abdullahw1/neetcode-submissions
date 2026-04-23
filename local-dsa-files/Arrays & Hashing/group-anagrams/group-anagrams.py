class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}
        for word in strs:
            key = "".join(sorted(word))            # sort the letters → anagram "name tag"
            groups.setdefault(key, []).append(word) # group under that key
        return list(groups.values())

        # Optimal — O(m * n) using character count as key
        # from collections import defaultdict
        # groups = defaultdict(list)
        # for word in strs:
        #     count = [0] * 26
        #     for char in word:
        #         count[ord(char) - ord('a')] += 1
        #     groups[tuple(count)].append(word)
        # return list(groups.values())


if __name__ == "__main__":
    sol = Solution()

    tests = [
        (["act", "pots", "tops", "cat", "stop", "hat"],
         [["act", "cat"], ["pots", "tops", "stop"], ["hat"]]),
        (["x"],
         [["x"]]),
        ([""],
         [[""]]),
        (["aaa", "aaa"],
         [["aaa", "aaa"]]),
    ]

    print("Group Anagrams")
    print("Time: O(m * n log n) | Space: O(m * n)\n")

    for i, (strs, expected) in enumerate(tests, 1):
        result = sol.groupAnagrams(strs)
        # sort inner lists and outer list for comparison since order doesn't matter
        result_sorted = sorted([sorted(g) for g in result])
        expected_sorted = sorted([sorted(g) for g in expected])
        status = "✅" if result_sorted == expected_sorted else "❌"
        print(f"  {status} Test {i}: {strs} → {result}")
