class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #optimal solution using a hashmap
        count = {}
        for num in nums:
            if num in count:
                count[num] +=1
                return True
            else:
                count[num] = 1
        return False
        #brute force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        