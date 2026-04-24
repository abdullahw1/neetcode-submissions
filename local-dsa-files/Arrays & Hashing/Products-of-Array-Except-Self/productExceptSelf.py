class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)

        prefix = 1                              # running product from the left
        for i in range(len(nums)):
            res[i] = prefix                     # store left product
            prefix *= nums[i]                   # include current for next position

        postfix = 1                             # running product from the right
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix                   # multiply by right product
            postfix *= nums[i]                  # include current for next position

        return res

        # --- Alternative: Separate prefix/suffix arrays — O(n) space ---
        # n = len(nums)
        # left = [1] * n
        # right = [1] * n
        # for i in range(1, n):
        #     left[i] = left[i - 1] * nums[i - 1]
        # for i in range(n - 2, -1, -1):
        #     right[i] = right[i + 1] * nums[i + 1]
        # return [left[i] * right[i] for i in range(n)]

        # --- Alternative: Brute force — O(n²) ---
        # res = []
        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             prod *= nums[j]
        #     res.append(prod)
        # return res


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([1, 2, 3, 4],       [24, 12, 8, 6]),
        ([1, 2, 4, 6],       [48, 24, 12, 8]),
        ([-1, 0, 1, 2, 3],   [0, -6, 0, 0, 0]),
        ([2, 3],              [3, 2]),
        ([0, 0, 2],           [0, 0, 0]),
        ([1, 1, 1, 1],        [1, 1, 1, 1]),
        ([-1, -1],            [-1, -1]),
    ]

    print("Products of Array Except Self")
    print("Time: O(n) | Space: O(1) extra\n")

    for i, (nums, expected) in enumerate(tests, 1):
        result = sol.productExceptSelf(nums)
        status = "✅" if result == expected else "❌"
        print(f"  {status} Test {i}: {nums} → {result}")
