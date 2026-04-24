class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)                    # O(1) lookups + removes duplicates
        longest = 0

        for num in num_set:
            if (num - 1) not in num_set:       # is this the START of a sequence?
                length = 1
                while (num + length) in num_set:  # keep extending
                    length += 1
                longest = max(length, longest)

        return longest

        # --- Alternative: Sorting — O(n log n) ---
        # if not nums:
        #     return 0
        # nums.sort()
        # longest, streak = 1, 1
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         continue
        #     if nums[i] == nums[i - 1] + 1:
        #         streak += 1
        #     else:
        #         streak = 1
        #     longest = max(longest, streak)
        # return longest


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([2, 20, 4, 10, 3, 4, 5],    4),
        ([0, 3, 2, 5, 4, 6, 1, 1],   7),
        ([100, 4, 200, 1, 3, 2],      4),
        ([],                           0),
        ([7],                          1),
        ([5, 5, 5],                    1),
        ([-1, 0, 1, 2],               4),
        ([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6], 7),
    ]

    print("Longest Consecutive Sequence")
    print("Time: O(n) | Space: O(n)\n")

    for i, (nums, expected) in enumerate(tests, 1):
        result = sol.longestConsecutive(nums)
        status = "✅" if result == expected else "❌"
        print(f"  {status} Test {i}: {nums} → {result}")
