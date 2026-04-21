class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            a = nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -a
            L = i+1
            R = len(nums) -1
            while L < R:
                curr_sum = nums[R] + nums[L]
                if curr_sum == target:
                    res.append([a, nums[R], nums[L]])
                    L+=1
                    R-=1
                    while L < R and nums[L] == nums[L-1]:
                        L += 1
                    while L < R and nums[R] == nums[R+1]:
                        R -= 1
                elif curr_sum < target:
                # Case 2: Sum is TOO SMALL. 
                # Move L right to increase the sum (since the array is sorted ascending).
                    L += 1
                else: # current_sum > target
                # Case 3: Sum is TOO LARGE. 
                # Move R left to decrease the sum.
                    R -= 1
        return res      





