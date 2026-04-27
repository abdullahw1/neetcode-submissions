class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        res = 0

        while left < right:
            if left_max < right_max:
                left += 1                              # move the shorter side
                left_max = max(left_max, height[left]) # update running max
                res += left_max - height[left]         # water = max - ground
            else:
                right -= 1
                right_max = max(right_max, height[right])
                res += right_max - height[right]

        return res

        # --- Alternative: Prefix/Suffix arrays — O(n) space ---
        # n = len(height)
        # left_max = [0] * n
        # right_max = [0] * n
        # left_max[0] = height[0]
        # for i in range(1, n):
        #     left_max[i] = max(left_max[i - 1], height[i])
        # right_max[n - 1] = height[n - 1]
        # for i in range(n - 2, -1, -1):
        #     right_max[i] = max(right_max[i + 1], height[i])
        # res = 0
        # for i in range(n):
        #     res += min(left_max[i], right_max[i]) - height[i]
        # return res


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([0, 2, 0, 3, 1, 0, 1, 3, 2, 1],  9),
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5],               9),
        ([1, 1, 1],                         0),
        ([0, 5, 0],                         0),
        ([3, 0, 2, 0, 4],                   7),
        ([],                                0),
        ([5],                               0),
    ]

    print("Trapping Rain Water")
    print("Time: O(n) | Space: O(1)\n")

    for i, (height, expected) in enumerate(tests, 1):
        result = sol.trap(height)
        status = "✅" if result == expected else "❌"
        print(f"  {status} Test {i}: {height} → {result}")
