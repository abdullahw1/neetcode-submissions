class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1   # start at both ends

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum > target:
                right -= 1                   # sum too big → smaller right number
            elif current_sum < target:
                left += 1                    # sum too small → bigger left number
            else:
                return [left + 1, right + 1] # found it! return 1-indexed

        return []

        # --- Alternative: Brute force — O(n²) ---
        # for i in range(len(numbers)):
        #     for j in range(i + 1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]
        # return []

        # --- Alternative: Hash map — O(n) time, O(n) space ---
        # seen = {}
        # for i, num in enumerate(numbers):
        #     complement = target - num
        #     if complement in seen:
        #         return [seen[complement] + 1, i + 1]
        #     seen[num] = i
        # return []


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([1, 2, 3, 4],    3,    [1, 2]),
        ([2, 7, 11, 15],  9,    [1, 2]),
        ([2, 3, 4],       6,    [1, 3]),
        ([2, 2],          4,    [1, 2]),
        ([-3, -1, 0, 2],  -1,   [1, 4]),
        ([1, 3, 4, 5, 7, 11], 9, [3, 4]),
    ]

    print("Two Sum II — Input Array Is Sorted")
    print("Time: O(n) | Space: O(1)\n")

    for i, (numbers, target, expected) in enumerate(tests, 1):
        result = sol.twoSum(numbers, target)
        status = "✅" if result == expected else "❌"
        print(f"  {status} Test {i}: numbers={numbers}, target={target} → {result}")
