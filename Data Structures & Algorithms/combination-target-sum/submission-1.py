class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(start, remaining, path):
            if remaining == 0:
                res.append(path[:])
                return
            for i in range(start, len(nums)):
                x = nums[i]
                if x > remaining:
                    break
                path.append(x)
                dfs(i, remaining - x, path)  # reuse allowed
                path.pop()
        dfs(0, target, [])
        return res


# def combinationSum(nums, target):
#     nums.sort()
#     res = []

#     def dfs(start, remaining, path):
#         if remaining == 0:
#             res.append(path[:])
#             return

#         for i in range(start, len(nums)):
#             x = nums[i]
#             if x > remaining:
#                 break
#             path.append(x)
#             dfs(i, remaining - x, path)  # reuse allowed
#             path.pop()

#     dfs(0, target, [])
#     return res
