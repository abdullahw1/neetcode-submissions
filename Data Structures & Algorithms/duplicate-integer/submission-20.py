class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] +=1
                return True
        return False
        
        # brute force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[j] == nums[i]:
        #             return True
        # return False            
                