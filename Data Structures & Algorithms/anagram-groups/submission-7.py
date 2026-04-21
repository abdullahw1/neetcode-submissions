class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for word in strs:
            key = "".join(sorted(word))

            if key not in words:
                words[key] = []
            words[key].append(word)
        return list(words.values())