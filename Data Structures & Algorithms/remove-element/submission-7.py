class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #two pointer method O(n)
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow]=nums[fast]
                slow +=1
        return slow
                
        #brute force method
        # i = 0
        # while i< len(nums):
        #     if nums[i]==val:
        #         nums.pop(i)
        #     else:
        #         i+=1
        # return len(nums)
        