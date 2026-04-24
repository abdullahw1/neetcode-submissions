# Longest Consecutive Sequence

**Difficulty:** Medium
**Pattern:** Hash Set / Sequence Start Detection

---

## Prerequisites

Before this problem, you should understand:
- **Hash sets** — O(1) lookup to check "does this number exist?" Same tool as Contains Duplicate.
- **What "consecutive" means** — numbers that follow each other with no gaps: 1, 2, 3, 4. Not necessarily in order in the array.

---

## Neetcode Problem

Given an array of integers `nums`, return the length of the longest consecutive sequence of elements. The elements don't have to be next to each other in the array. Must run in O(n) time.

---

## Problem (In My Own Words)

Find the longest chain of numbers where each one is exactly 1 more than the last. The numbers can be scattered anywhere in the array — you just need to find them.

`[2, 20, 4, 10, 3, 4, 5]` → the chain `2, 3, 4, 5` has length 4.

---

## ELI5 (Feynman Explanation)

Imagine you dump a box of numbered LEGO bricks on the floor: 2, 20, 4, 10, 3, 4, 5.

You want to find the longest chain you can snap together where each brick is exactly 1 more than the last.

**Dumb approach:** Pick up every brick and try to build a chain starting from it. Brick 4? Check for 5, 6, 7... Brick 20? Check for 21, 22... You're doing a ton of repeated work.

**Smart approach:** Before you start building, ask yourself: "Is this brick the START of a chain?" A brick is a start only if there's NO brick with the number one less than it.

- Brick 2: is 1 on the floor? NO → this is a start! Count: 2, 3, 4, 5 → length 4
- Brick 3: is 2 on the floor? YES → skip, 3 is in the middle of a chain, not the start
- Brick 20: is 19 on the floor? NO → this is a start! Count: 20 → length 1

By only starting from chain beginnings, you never count the same brick twice.

---

## The Key Insight

The trick that makes this O(n) instead of O(n²):

**Only start counting from the BEGINNING of a sequence.**

A number `num` is the start of a sequence if `num - 1` is NOT in the set.

```
nums = [100, 4, 200, 1, 3, 2]

Set = {1, 2, 3, 4, 100, 200}

100: is 99 in set? NO → start! 100, 101? no → length 1
  4: is 3 in set? YES → skip (4 is not a start)
200: is 199 in set? NO → start! 200, 201? no → length 1
  1: is 0 in set? NO → start! 1→2→3→4→5? no → length 4 ✅
  3: is 2 in set? YES → skip
  2: is 1 in set? YES → skip
```

Even though there's a while loop inside the for loop, each number is visited at most twice (once in the for loop, once in a while loop). Total work = O(n).

---

## Visual Walkthrough

```
Input: nums = [2, 20, 4, 10, 3, 4, 5]

Step 1 — Build set (removes duplicates):
  num_set = {2, 3, 4, 5, 10, 20}

Step 2 — Find sequence starts and count:

  num=2:  is 1 in set? NO → start!
          2→3? yes, 3→4? yes, 4→5? yes, 5→6? no
          length = 4, longest = 4

  num=3:  is 2 in set? YES → skip

  num=4:  is 3 in set? YES → skip

  num=5:  is 4 in set? YES → skip

  num=10: is 9 in set? NO → start!
          10→11? no
          length = 1, longest = 4

  num=20: is 19 in set? NO → start!
          20→21? no
          length = 1, longest = 4

Output: 4 ✅
```

---

## Solution (Hash Set — Optimal) ⭐

```python
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)                    # O(1) lookups + removes duplicates
        longest = 0

        for num in num_set:
            if (num - 1) not in num_set:       # is this the START of a sequence?
                length = 1
                while (num + length) in num_set:  # keep extending
                    length += 1
                longest = max(length, longest)

        return longest
```

**Why this is the best interview answer:**
- O(n) time — each number is processed at most twice
- O(n) space — just the set
- The `(num - 1) not in num_set` check is the entire trick. One line makes it optimal.

---

## Why Is This O(n) and Not O(n²)?

This confuses a lot of people because there's a while loop inside a for loop. Here's why it's still O(n):

- The for loop visits every number in the set → n iterations
- The while loop ONLY runs when `num` is a sequence start
- Each number can only be part of ONE sequence
- So across ALL iterations of the for loop, the while loop runs a TOTAL of n times, not n times per iteration

Think of it this way: every number gets "counted" at most once by the while loop. Total work = O(n) + O(n) = O(n).

---

## Alternative: Sorting

```python
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        longest, streak = 1, 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:         # skip duplicates
                continue
            if nums[i] == nums[i - 1] + 1:     # consecutive
                streak += 1
            else:                                # gap — reset
                streak = 1
            longest = max(longest, streak)

        return longest
```

| Pros | Cons |
|---|---|
| Simple to understand | O(n log n) — doesn't meet the O(n) requirement |
| No extra space (if in-place sort) | Modifies the input array |
| Good to mention as starting point | Interviewer will ask for O(n) |

---

## Both Compared

| Approach | Time | Space | Notes |
|---|---|---|---|
| Sorting | O(n log n) | O(1) | Mention first, then optimize |
| **Hash set** | **O(n)** | **O(n)** | **Use this — meets the O(n) requirement** |

---

## Complexity Analysis

| | Complexity | Why |
|---|---|---|
| **Time** | O(n) | Each number visited at most twice (once in for, once in while) |
| **Space** | O(n) | The set stores all unique numbers |

---

## Gotchas & Edge Cases

- **Empty array** → return 0
- **All same numbers** → `[5, 5, 5]` → set becomes `{5}`, longest = 1
- **Duplicates** → the set handles them automatically, no special logic needed
- **Negative numbers** → works fine, `num - 1` and `num + 1` still make sense
- **Single element** → `[7]` → longest = 1
- **Already sorted** → doesn't matter, the set approach doesn't care about order

---

## Pattern Recognition

This problem teaches the **sequence start detection** pattern — only process items that are the beginning of something, skip everything in the middle.

You'll see similar ideas in:
- Longest Substring Without Repeating Characters (sliding window start detection)
- Union Find problems (connecting components)
- Interval merging (finding where intervals start)

Whenever you see "find the longest chain/sequence" with an O(n) requirement → think **set + only start from the beginning**.
