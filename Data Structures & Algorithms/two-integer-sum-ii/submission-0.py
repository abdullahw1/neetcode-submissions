class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
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
