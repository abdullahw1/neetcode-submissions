class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countVals = {}
        for num in nums:
            if num not in countVals:
                countVals[num] = 1
            else:
                countVals[num]+=1
                return True
        return False
