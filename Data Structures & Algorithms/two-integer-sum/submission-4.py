class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #best solution using a hashmap
        seen = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in seen:
                return [seen[compliment], i]
            seen[num] = i
        return []
        #brute force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        #     i +=1
        # return False
         