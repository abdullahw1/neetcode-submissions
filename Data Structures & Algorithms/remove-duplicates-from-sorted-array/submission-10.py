class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #two pointer solution
        slow = 0
        fast =1 
        for fast in range(1, len(nums)):
            if nums[fast]!=nums[slow]:
                slow+=1
                nums[slow]=nums[fast]
        return slow + 1
        #brute force:
        # i =1
        # while i < len(nums):
        #     if nums[i]==nums[i-1]:
        #         nums.pop(i)
        #     else:
        #         i+=1
        # return len(nums)