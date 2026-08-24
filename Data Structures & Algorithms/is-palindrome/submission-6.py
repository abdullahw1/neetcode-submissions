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

        # left = 0
        # right = len(s) - 1
        # while left < right:

        #     while left < right and not s[left].isalnum():
        #         left += 1
        #     while left < right and not s[right].isalnum():
        #         right -= 1
        #     if s[left].lower() != s[right].lower():
        #         return False
        #     left += 1
        #     right -= 1
        # return True



            
            