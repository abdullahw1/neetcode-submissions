class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i< len(nums):
            if nums[i]==val:
                nums.pop(i)
            else:
                i+=1
        return len(nums)
        # k = 0
        # while k< len(nums):
        #     if nums[k] == val:
        #         nums.pop(k)
        #     else:
        #         k+=1
        # return len(nums)
        