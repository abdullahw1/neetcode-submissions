# Two Sum II — Input Array Is Sorted

**Difficulty:** Medium
**Pattern:** Two Pointers

---

## Prerequisites

Before this problem, you should understand:
- **Two Sum I** — the original problem where you use a hash map to find two numbers that add up to a target. This problem is the sorted version, and the key question is: how does sorting change your approach?
- **Two pointers** — one pointer at the left end, one at the right end, moving inward based on a condition. You just used this in Valid Palindrome.
- **Sorted arrays** — when an array is sorted, you have extra information. If the sum is too big, you know moving right makes it bigger. Moving left makes it smaller. This is the key insight.

---

## Neetcode Problem

Given a **sorted** array of integers `numbers`, return the **1-indexed** positions `[index1, index2]` of two numbers that add up to `target`. There is always exactly one solution. Must use O(1) extra space.

---

## Problem (In My Own Words)

Same as Two Sum, but the array is already sorted and you can't use extra space. Find the two numbers that add up to the target and return their positions (starting from 1, not 0).

---

## ELI5 (Feynman Explanation)

Imagine a number line with people standing on it in order from smallest to largest. You need to find two people whose ages add up to exactly 30.

You put one finger on the youngest person (left) and one finger on the oldest person (right).

- Add their ages. Too big? The oldest person is too old — move your right finger one step left to someone younger.
- Too small? The youngest person is too young — move your left finger one step right to someone older.
- Exactly 30? You found them!

Because the people are in order, every move you make is guaranteed to get you closer to the answer. You never need to backtrack. That's why this works in O(n) — each finger moves at most n times total.

---

## Why Sorting Changes Everything

In Two Sum I (unsorted), you needed a hash map to find the complement in O(1). That costs O(n) space.

In Two Sum II (sorted), you don't need the hash map at all. The sorted order gives you a "direction" to move:

```
Sum too big  → right pointer moves LEFT  (smaller number)
Sum too small → left pointer moves RIGHT (bigger number)
Sum == target → done!
```

This is the core insight. Sorting trades space for a smarter search strategy.

---

## Visual Walkthrough

```
Input: numbers = [1, 2, 3, 4], target = 3

         L              R
         ↓              ↓
       [ 1,  2,  3,  4 ]

Step 1: sum = 1 + 4 = 5 > 3 → too big, move R left
         L         R
         ↓         ↓
       [ 1,  2,  3,  4 ]

Step 2: sum = 1 + 3 = 4 > 3 → still too big, move R left
         L    R
         ↓    ↓
       [ 1,  2,  3,  4 ]

Step 3: sum = 1 + 2 = 3 == target ✅
        return [1, 2]  (1-indexed)
```

```
Input: numbers = [2, 7, 11, 15], target = 9

         L                  R
         ↓                  ↓
       [ 2,  7,  11,  15 ]

Step 1: sum = 2 + 15 = 17 > 9 → move R left
         L         R
         ↓         ↓
       [ 2,  7,  11,  15 ]

Step 2: sum = 2 + 11 = 13 > 9 → move R left
         L    R
         ↓    ↓
       [ 2,  7,  11,  15 ]

Step 3: sum = 2 + 7 = 9 == target ✅
        return [1, 2]  (1-indexed)
```

---

## Interview Approach — How to Talk Through This

**Step 1 — Brute force:**
> "The naive approach is to check every pair — O(n²) time, O(1) space. But we're not using the sorted property at all."

**Step 2 — Hash map (Two Sum I approach):**
> "I could use a hash map like in Two Sum I — O(n) time, but O(n) space. The problem says O(1) space, so this doesn't meet the requirement. Also, we're ignoring the sorted property again."

**Step 3 — Two pointers (optimal):**
> "Since the array is sorted, I can use two pointers. Start one at each end. If the sum is too big, move the right pointer left. If too small, move the left pointer right. This is O(n) time and O(1) space — optimal."

This progression shows you understand *why* each approach works and what the trade-offs are.

---

## Solution (Two Pointers — Optimal) ⭐

```python
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

        return []                            # guaranteed to find one, but just in case
```

---

## All Approaches Compared

| Approach | Time | Space | Notes |
|---|---|---|---|
| Brute force (nested loops) | O(n²) | O(1) | Ignores sorted property entirely |
| Binary search | O(n log n) | O(1) | Uses sorted property, but not fully |
| Hash map | O(n) | O(n) | Optimal time but wastes space, ignores sorted |
| **Two pointers** | **O(n)** | **O(1)** | **Optimal — uses sorted property fully** |

The two-pointer approach is the only one that achieves both O(n) time AND O(1) space. It's the "correct" answer for this problem specifically because of the sorted constraint.

---

## Two Sum I vs Two Sum II — Key Difference

| | Two Sum I | Two Sum II |
|---|---|---|
| Array sorted? | No | Yes |
| Best approach | Hash map | Two pointers |
| Time | O(n) | O(n) |
| Space | O(n) | O(1) |
| Return | 0-indexed | **1-indexed** |

The sorted property is what lets you drop from O(n) space to O(1) space. Interviewers love asking this follow-up: "What if the array were sorted?" — now you know the answer.

---

## Complexity Analysis

| | Complexity | Why |
|---|---|---|
| **Time** | O(n) | Each pointer moves at most n times total |
| **Space** | O(1) | Just two integer pointers, no extra data structures |

---

## Gotchas & Edge Cases

- **1-indexed output** — the problem wants `[1, 2]` not `[0, 1]`. Don't forget `+1` on both indices.
- **Exactly one solution guaranteed** — no need to handle "not found"
- **Negative numbers** — works fine, the pointer logic doesn't care about sign
- **Duplicates** — `[2, 2]` with target `4` → `[1, 2]` — works correctly since `left < right`
- **Two elements** — `[1, 3]` with target `4` → `[1, 2]` — the while loop runs once

---

## Pattern Recognition

This problem is the canonical example of **two pointers on a sorted array**.

You'll use this exact same pattern in:
- 3Sum (sort first, then two pointers for the inner loop)
- 4Sum (same idea, two more nested loops)
- Container With Most Water
- Trapping Rain Water

Whenever you see "sorted array + find a pair/triplet that sums to target" → think **two pointers**.
