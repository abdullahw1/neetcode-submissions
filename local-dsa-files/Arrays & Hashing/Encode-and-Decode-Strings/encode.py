class Solution:

    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s   # length + separator + string
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":            # find the '#' separator
                j += 1
            length = int(s[i:j])           # everything before '#' is the length
            i = j + 1                      # skip past '#'
            j = i + length                 # jump exactly 'length' characters
            res.append(s[i:j])             # extract the string
            i = j                          # move to next encoded segment

        return res


if __name__ == "__main__":
    sol = Solution()

    tests = [
        (["Hello", "World"],              ["Hello", "World"]),
        (["neet", "code", "love", "you"], ["neet", "code", "love", "you"]),
        ([""],                            [""]),
        ([],                              []),
        (["5#hello", "world"],            ["5#hello", "world"]),
        (["a", "bb", "ccc"],              ["a", "bb", "ccc"]),
        (["abc123", "#", "test#ing"],     ["abc123", "#", "test#ing"]),
    ]

    print("Encode and Decode Strings")
    print("Time: O(m) | Space: O(m + n)\n")

    for i, (strs, expected) in enumerate(tests, 1):
        encoded = sol.encode(strs)
        decoded = sol.decode(encoded)
        status = "✅" if decoded == expected else "❌"
        print(f"  {status} Test {i}: {strs} → encode → \"{encoded}\" → decode → {decoded}")
