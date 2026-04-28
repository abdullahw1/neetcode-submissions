class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}                          # {number: index}
        for i, num in enumerate(nums):
            complement = target - num      # what do I need?
            if complement in seen:         # have I seen it before?
                return [seen[complement], i]
            seen[num] = i                  # remember this number and where it was
        return []
