class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}                          # {number: index}
        for i, num in enumerate(nums):
            complement = target - num      # what do I need?
            if complement in seen:         # have I seen it before?
                return [seen[complement], i]
            seen[num] = i                  # remember this number and where it was
        return []

        # Brute Force — O(n²)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([3, 4, 5, 6],  7,  [0, 1]),
        ([4, 5, 6],     10, [0, 2]),
        ([5, 5],        10, [0, 1]),
        ([1, 2, 3, 4],  7,  [2, 3]),
        ([-1, -2, -3, -4, -8], -6, [1, 3]),
    ]

    print("Two Sum")
    print("Time: O(n) | Space: O(n)\n")

    for i, (nums, target, expected) in enumerate(tests, 1):
        result = sol.twoSum(nums, target)
        status = "✅" if result == expected else "❌"
        print(f"  {status} Test {i}: nums={nums}, target={target} → {result}")
