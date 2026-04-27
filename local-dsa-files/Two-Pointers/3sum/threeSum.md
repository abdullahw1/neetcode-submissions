# 3Sum

**Difficulty:** Medium
**Pattern:** Sort + Two Pointers

---

## Prerequisites

Before this problem, you should understand:
- **Two Sum II** — you just did this. 3Sum is literally Two Sum II applied inside a loop. If you can do Two Sum II, you can do 3Sum.
- **Sorting** — sorting the array is what makes the two-pointer trick work AND makes duplicate-skipping easy.
- **Two pointers on a sorted array** — if sum is too big, move right pointer left. If too small, move left pointer right.
- **Skipping duplicates** — after sorting, duplicates are next to each other. You skip them by checking `if nums[i] == nums[i-1]: continue`.

---

## Neetcode Problem

Given an integer array `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]` where `i`, `j`, `k` are distinct and `nums[i] + nums[j] + nums[k] == 0`. No duplicate triplets in the output.

---

## Problem (In My Own Words)

Find every group of 3 numbers in the array that add up to zero. Don't return the same group twice.

---

## ELI5 (Feynman Explanation)

Imagine you have a bunch of numbered cards spread on a table. You want to find every group of 3 cards that add up to zero.

**Dumb approach:** Pick every possible combination of 3 cards and check. That's O(n³) — way too slow.

**Smart approach:**
1. First, sort the cards in order from smallest to largest.
2. Pick one card at a time as your "anchor" (the fixed first number).
3. For the remaining cards, use the Two Sum II trick — put one finger at the left end and one at the right end. Move them inward based on whether the sum is too big or too small.

The anchor card reduces the problem from "find 3 numbers" to "find 2 numbers that sum to -anchor." You already know how to do that from Two Sum II.

---

## The Hint-by-Hint Breakdown

**Hint 1 — Brute force is O(n³):**
Three nested loops checking every triplet. Works but way too slow. You need better.

**Hint 2 — Sort first:**
Sorting lets you use two pointers AND skip duplicates easily. Both are critical.

**Hint 3 — Rearrange the equation:**
`a + b + c = 0` → `b + c = -a`

Fix `a` (the outer loop), then find `b` and `c` that sum to `-a`. That's exactly Two Sum II on the remaining elements.

**Hint 4 — Two pointers for b and c:**
After fixing `a` at index `i`, set `l = i+1` and `r = end`. Move them based on the sum:
- `sum > 0` → move `r` left (need smaller number)
- `sum < 0` → move `l` right (need bigger number)
- `sum == 0` → found a triplet, record it and move both inward

**Hint 5 — Skip duplicates:**
After finding a triplet, advance `l` past any repeated values. Same for the outer loop — if `nums[i] == nums[i-1]`, skip it. This prevents duplicate triplets in the output.

---

## Visual Walkthrough

```
Input: nums = [-1, 0, 1, 2, -1, -4]

Step 1 — Sort:
  nums = [-4, -1, -1, 0, 1, 2]

Step 2 — Outer loop, fix a:

  i=0, a=-4:
    target for l+r = 4
    l=1(-1), r=5(2): sum=-1+2=1 < 4 → l++
    l=2(-1), r=5(2): sum=-1+2=1 < 4 → l++
    l=3(0),  r=5(2): sum=0+2=2  < 4 → l++
    l=4(1),  r=5(2): sum=1+2=3  < 4 → l++
    l=5, l not < r → done. No triplets.

  i=1, a=-1:
    target for l+r = 1
    l=2(-1), r=5(2): sum=-1+2=1 == 1 ✅ → add [-1,-1,2]
    l++ → l=3(0), r-- → r=4(1)
    l=3(0), r=4(1): sum=0+1=1 == 1 ✅ → add [-1,0,1]
    l++ → l=4, r-- → r=3, l not < r → done.

  i=2, a=-1:
    nums[2] == nums[1] → SKIP (duplicate)

  i=3, a=0:
    target for l+r = 0
    l=4(1), r=5(2): sum=1+2=3 > 0 → r--
    r=4, l not < r → done. No triplets.

  i=4, a=1:
    a > 0 → BREAK (all remaining are positive, can't sum to 0)

Output: [[-1,-1,2], [-1,0,1]] ✅
```

---

## Why Break When `a > 0`?

If `a` (the smallest of the three numbers, since the array is sorted) is already positive, then `b` and `c` are also positive (they're to the right of `a`). Three positive numbers can never sum to zero. So you can stop the outer loop early.

**Important gotcha:** break when `a > 0`, NOT `a >= 0`. The triplet `[0, 0, 0]` is valid!

---

## Solution (Sort + Two Pointers — Optimal) ⭐

```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
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
```

---

## Interview Approach — How to Talk Through This

**Step 1 — Brute force:**
> "The obvious approach is three nested loops — O(n³). Check every triplet, use a set to avoid duplicates. Way too slow."

**Step 2 — Reduce to Two Sum II:**
> "If I sort the array, I can fix one number `a` in an outer loop and then find two numbers that sum to `-a` in the remaining elements. That's exactly Two Sum II, which I can solve in O(n) with two pointers."

**Step 3 — Handle duplicates:**
> "After sorting, duplicates are adjacent. I skip duplicate values for the outer loop with `if nums[i] == nums[i-1]: continue`. After finding a triplet, I advance the left pointer past any repeated values."

**Step 4 — Early termination:**
> "If the current number is positive, all remaining numbers are also positive — they can't sum to zero. I break early."

This shows you can build on previous knowledge (Two Sum II) and handle edge cases cleanly.

---

## All Approaches Compared

| Approach | Time | Space | Notes |
|---|---|---|---|
| Brute force (3 loops) | O(n³) | O(m) | Too slow, mention as starting point |
| Hash map | O(n²) | O(n) | Works but uses extra space, ignores sorted property |
| **Sort + Two Pointers** | **O(n²)** | **O(1)** | **Optimal — use this in interviews** |

O(n²) is the best you can do here — you need at least O(n²) to find all triplets since there can be O(n²) of them.

---

## Complexity Analysis

| | Complexity | Why |
|---|---|---|
| **Time** | O(n²) | Outer loop O(n) × inner two-pointer O(n) |
| **Space** | O(1) extra | Just pointers (output list doesn't count) |

Sorting is O(n log n) but O(n²) dominates.

---

## Gotchas & Edge Cases

- **`a > 0` not `a >= 0`** — `[0, 0, 0]` is a valid triplet, don't skip zeros
- **Duplicate outer values** — `[-1, -1, 0, 1]` — skip the second `-1` in the outer loop
- **Duplicate inner values** — after finding a triplet, skip repeated `l` values
- **All same number** — `[0, 0, 0]` → one triplet `[0, 0, 0]`
- **No valid triplets** — `[1, 2, 3]` → return `[]`
- **The inner `l < r` guard in the duplicate skip** — without it you can go out of bounds

---

## Pattern Recognition

3Sum = **sort + fix one + Two Sum II on the rest**.

This "reduce by one dimension" pattern shows up in:
- 4Sum (fix two numbers, Two Sum II on the rest)
- 3Sum Closest (same structure, track minimum difference)
- Triangle Number Count

Whenever you see "find k numbers that sum to target" → **sort + fix (k-2) numbers + two pointers**.
