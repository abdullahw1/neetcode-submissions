class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1       # start at both ends

        while left < right:
            # skip non-alphanumeric characters from the left
            while left < right and not s[left].isalnum():
                left += 1
            # skip non-alphanumeric characters from the right
            while left < right and not s[right].isalnum():
                right -= 1

            # compare the characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False               # mismatch — not a palindrome

            left += 1                      # move both pointers inward
            right -= 1

        return True                        # made it through — it's a palindrome

        # --- Alternative: Reverse string — O(n) space ---
        # cleaned = ""
        # for c in s:
        #     if c.isalnum():
        #         cleaned += c.lower()
        # return cleaned == cleaned[::-1]


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("Was it a car or a cat I saw?", True),
        ("tab a cat",                    False),
        ("A man, a plan, a canal: Panama", True),
        ("race a car",                   False),
        ("",                             True),
        ("a",                            True),
        ("!!!",                          True),
        ("Aba",                          True),
        ("12321",                        True),
        ("0P",                           False),
    ]

    print("Valid Palindrome")
    print("Time: O(n) | Space: O(1)\n")

    for i, (s, expected) in enumerate(tests, 1):
        result = sol.isPalindrome(s)
        status = "✅" if result == expected else "❌"
        print(f"  {status} Test {i}: \"{s}\" → {result}")
