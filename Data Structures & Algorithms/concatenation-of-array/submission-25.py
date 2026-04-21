class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0]*(2* len(nums))
        b = 0
        for i, num in enumerate(nums):
            ans[i]= nums
            ans[b]=nums
            ans = ans[i]+ans[b]
        return ans