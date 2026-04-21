class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Sort the numbers so we can:
        # 1) stop early when a number is too large
        # 2) ensure combinations are built in non-decreasing order
        nums.sort()

        # This will store all valid combinations
        res = []

        # Backtracking helper function
        # start     -> index in nums we are allowed to use from
        # remaining -> how much sum we still need to reach target
        # path      -> current combination being built
        def dfs(start, remaining, path):
            # If remaining is exactly 0, we found a valid combination
            if remaining == 0:
                # Make a copy of path and add it to results
                res.append(path[:])
                return

            # Try all numbers starting from index 'start'
            # This prevents duplicates like [2,5,2] vs [2,2,5]
            for i in range(start, len(nums)):
                # Current number we are considering
                x = nums[i]

                # If the number is larger than what we still need,
                # we can stop because nums is sorted
                if x > remaining:
                    break

                # Choose the current number
                path.append(x)

                # Recurse:
                # - i (not i+1) because we can reuse the same number
                # - remaining - x because we used x
                dfs(i, remaining - x, path)

                # Backtrack:
                # remove the last number so we can try the next option
                path.pop()

        # Start DFS from index 0, with full target, and empty path
        dfs(0, target, [])

        # Return all valid combinations found
        return res


# class Solution:
#     def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
#         res = []

#         def dfs(i, cur, total):
#             if total == target:
#                 res.append(cur.copy())
#                 return
#             if i >= len(nums) or total > target:
#                 return

#             cur.append(nums[i])
#             dfs(i, cur, total + nums[i])
#             cur.pop()
#             dfs(i + 1, cur, total)

#         dfs(0, [], 0)
#         return res