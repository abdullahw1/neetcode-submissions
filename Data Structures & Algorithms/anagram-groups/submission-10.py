class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            groups.setdefault(sorted_word, []).append(word)
        return list(groups.values())
