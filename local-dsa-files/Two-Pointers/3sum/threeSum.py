class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()                                    # sort first — enables two pointers + duplicate skipping

        for i, a in enumerate(nums):
            if a > 0:                                  # all remaining are positive → can't sum to 0
                break

            if i > 0 and a == nums[i - 1]:             # skip duplicate first numbers
                continue

            l, r = i + 1, len(nums) - 1               # two pointers for the remaining elements

            while l < r:
                three_sum = a + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1                             # too big → smaller right number
                elif three_sum < 0:
                    l += 1                             # too small → bigger left number
                else:
                    res.append([a, nums[l], nums[r]])  # found a triplet!
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:  # skip duplicate left values
                        l += 1

        return res

        # --- Alternative: Brute force — O(n³) ---
        # res = set()
        # nums.sort()
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 res.add((nums[i], nums[j], nums[k]))
        # return [list(t) for t in res]


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([-1, 0, 1, 2, -1, -4],  [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1],               []),
        ([0, 0, 0],               [[0, 0, 0]]),
        ([1, 2, 3],               []),
        ([-2, 0, 0, 2, 2],        [[-2, 0, 2]]),
        ([-4, -1, -1, 0, 1, 2],   [[-1, -1, 2], [-1, 0, 1]]),
    ]

    print("3Sum")
    print("Time: O(n²) | Space: O(1)\n")

    for i, (nums, expected) in enumerate(tests, 1):
        result = sol.threeSum(nums)
        # sort for comparison since order doesn't matter
        result_sorted = sorted([sorted(t) for t in result])
        expected_sorted = sorted([sorted(t) for t in expected])
        status = "✅" if result_sorted == expected_sorted else "❌"
        print(f"  {status} Test {i}: {nums} → {result}")
