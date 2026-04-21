class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #using a hash set O(n)
        countVals = {}
        for num in nums:
            if num not in countVals:
                countVals[num]=1
            else:
                countVals[num]+=1
                return True
        return False
        #brute force O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]==nums[j]:
        #             return True
        # return False
