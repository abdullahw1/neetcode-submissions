class Solution:
    def maxArea(self, heights: list[int]) -> int:
        left, right = 0, len(heights) - 1    # start as wide as possible
        max_area = 0

        while left < right:
            # calculate area with current pair
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height
            max_area = max(max_area, area)

            # move the shorter side inward (greedy choice)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return max_area

        # --- Alternative: Brute force — O(n²) ---
        # max_area = 0
        # for i in range(len(heights)):
        #     for j in range(i + 1, len(heights)):
        #         area = min(heights[i], heights[j]) * (j - i)
        #         max_area = max(max_area, area)
        # return max_area


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([1, 7, 2, 5, 4, 7, 3, 6],  36),
        ([2, 2, 2],                   4),
        ([1, 1],                      1),
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([5, 4, 3, 2, 1],            6),
        ([1, 2, 1],                   2),
    ]

    print("Container With Most Water")
    print("Time: O(n) | Space: O(1)\n")

    for i, (heights, expected) in enumerate(tests, 1):
        result = sol.maxArea(heights)
        status = "✅" if result == expected else "❌"
        print(f"  {status} Test {i}: {heights} → {result}")
