class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        
        # count = {}
        # for num in nums:
        #     if num not in count:
        #         count[num] =1
        #     else:
        #         count[num] +=1
        #         return True
        # return False

            


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([1, 2, 3, 3],    True),
        ([1, 2, 3, 4],    False),
        ([],               False),
        ([1],              False),
        ([1, 1, 1, 1],    True),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 1], True),
    ]

    print("Contains Duplicate")
    print("Time: O(n) | Space: O(n)\n")

    for i, (nums, expected) in enumerate(tests, 1):
        result = sol.hasDuplicate(nums)
        status = "✅" if result == expected else "❌"
        print(f"  {status} Test {i}: {nums} → {result}")
