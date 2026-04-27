class Solution:
    def trap(self, height: List[int]) -> int:
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