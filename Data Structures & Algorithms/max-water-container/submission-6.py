class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        rt=0
        while left<right:

            rt=max(rt,min(heights[left],heights[right])*(right-left))
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return rt





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



