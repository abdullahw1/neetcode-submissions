class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()                                    # sort first — enables two pointers + duplicate skipping

        for i, a in enumerate(nums):
            if a > 0:                                  # all remaining are positive → can't sum to 0
                break

            if i > 0 and a == nums[i - 1]:             # skip duplicate first numbers
                continue

            l, r = i + 1, len(nums) - 1               # two pointers for the remaining elements

            while l < r:
                three_sum = a + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1                             # too big → smaller right number
                elif three_sum < 0:
                    l += 1                             # too small → bigger left number
                else:
                    res.append([a, nums[l], nums[r]])  # found a triplet!
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:  # skip duplicate left values
                        l += 1

        return res






# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         res = set()
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 for k in range(j+1, len(nums)):
#                     if nums[i] + nums[j] +nums[k] == 0:
#                         tmp = [nums[i], nums[j], nums[k]]
#                         res.add(tuple(tmp))
#         return [list(i) for i in res]
#         # nums.sort()
#         # res = []
#         # for i in range(len(nums)):
#         #     a = nums[i]
#         #     if i > 0 and nums[i] == nums[i-1]:
#         #         continue
#         #     target = -a
#         #     L = i+1
#         #     R = len(nums) -1
#         #     while L < R:
#         #         curr_sum = nums[R] + nums[L]
#         #         if curr_sum == target:
#         #             res.append([a, nums[R], nums[L]])
#         #             L+=1
#         #             R-=1
#         #             while L < R and nums[L] == nums[L-1]:
#         #                 L += 1
#         #             while L < R and nums[R] == nums[R+1]:
#         #                 R -= 1
#         #         elif curr_sum < target:
#         #         # Case 2: Sum is TOO SMALL. 
#         #         # Move L right to increase the sum (since the array is sorted ascending).
#         #             L += 1
#         #         else: # current_sum > target
#         #         # Case 3: Sum is TOO LARGE. 
#         #         # Move R left to decrease the sum.
#         #             R -= 1
#         # return res      





