class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans = [0]*(2*n)
        b=0
        for i, num in enumerate(nums):
            ans[i]=nums
            ans[b] = nums
            ans=ans[i]+ans[b]
        return ans
