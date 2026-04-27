class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # left, right = 0, len(heights) - 1    # start as wide as possible
        # max_area = 0

        # while left < right:
        #     # calculate area with current pair
        #     width = right - left
        #     height = min(heights[left], heights[right])
        #     area = width * height
        #     max_area = max(max_area, area)

        #     # move the shorter side inward (greedy choice)
        #     if heights[left] <= heights[right]:
        #         left += 1
        #     else:
        #         right -= 1

        # return max_area


        res = 0
        n = len(heights)

        for i in range(len(heights)):
            for j in range(i+1, n):
                res = max(res, min(heights[i], heights[j]) * (j-i))
        return res