class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans=[0]*(2*length)
        for i, num in enumerate(nums):
            ans[i]=ans[i+length] =num

        return ans