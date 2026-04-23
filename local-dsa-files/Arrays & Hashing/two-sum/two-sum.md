# Two Sum

**Difficulty:** Easy
**Pattern:** Hash Map / Complement Lookup

---

## Neetcode Problem

Given an array of integers `nums` and an integer `target`, return the indices `i` and `j` such that `nums[i] + nums[j] == target` and `i != j`.

You may assume that every input has exactly one pair of indices that satisfy the condition. Return the answer with the smaller index first.

---

## Problem (In My Own Words)

You have a list of numbers and a target. Find the two numbers that add up to the target and return their positions (indices). There's always exactly one answer.

---

## ELI5 (Feynman Explanation)

You're at a party and the host says: "I need two people whose ages add up to 30."

You could go around asking every single pair — "Hey, do you two add up to 30?" That's slow (brute force).

Or you could be smart about it. You walk up to the first person:
- "How old are you?" → "12"
- You think: "I need someone who's **18** (30 - 12). Haven't met an 18-year-old yet."
- You write down: "12-year-old is at position 0" in your notebook.

Next person:
- "How old are you?" → "18"
- You think: "I need someone who's **12** (30 - 18). Wait — I wrote down a 12-year-old at position 0!"
- Done. Return [0, 1].

The **notebook** is your hash map. Instead of checking every pair, you check your notebook for the **complement** (target - current number) each time.

---

## The Key Insight

The math trick is simple algebra:

```
nums[i] + nums[j] = target
```

Rearrange it:

```
nums[j] = target - nums[i]
```

So for every number you see, you already know *exactly* what number you're looking for.
You don't need to search — you just need to **remember** what you've seen. That's what the hash map does.

---

## Visual Walkthrough

```
Input: nums = [3, 4, 5, 6], target = 7

Step 1: i=0, num=3
        complement = 7 - 3 = 4
        seen = {}
        4 in seen? NO
        Store: seen = {3: 0}

Step 2: i=1, num=4
        complement = 7 - 4 = 3
        seen = {3: 0}
        3 in seen? YES → seen[3] = 0
        Return [0, 1] ✅
```

```
Input: nums = [4, 5, 6], target = 10

Step 1: i=0, num=4
        complement = 10 - 4 = 6
        seen = {}
        6 in seen? NO
        Store: seen = {4: 0}

Step 2: i=1, num=5
        complement = 10 - 5 = 5
        seen = {4: 0}
        5 in seen? NO
        Store: seen = {4: 0, 5: 1}

Step 3: i=2, num=6
        complement = 10 - 6 = 4
        seen = {4: 0, 5: 1}
        4 in seen? YES → seen[4] = 0
        Return [0, 2] ✅
```

---

## Why Hash Map and Not Hash Set?

- A **set** only stores values — "I've seen the number 3"
- A **map** stores values AND their indices — "I've seen 3, and it was at index 0"
- We need to return **indices**, not the numbers themselves. So we need the map.

---

## Solution (Hash Map — One Pass)

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}                          # {number: index}
        for i, num in enumerate(nums):
            complement = target - num      # what do I need?
            if complement in seen:         # have I seen it before?
                return [seen[complement], i]
            seen[num] = i                  # remember this number and where it was
        return []
```

---

## Brute Force (For Reference)

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
```

Check every pair. Works, but O(n²) — interviewers want you to do better.

---

## Complexity Analysis

| Approach | Time | Space | Notes |
|---|---|---|---|
| **Hash map (one pass)** | **O(n)** | **O(n)** | **Optimal — use this in interviews** |
| Brute force (nested loops) | O(n²) | O(1) | Too slow, but good to mention as starting point |

---

## Gotchas & Edge Cases

- **Duplicate values** → `[5, 5]` with target `10` works fine because you check the complement *before* storing the current number
- **Negative numbers** → complement math still works: `target=2`, `num=5`, complement = `2 - 5 = -3`
- **Don't use the same element twice** → the loop naturally prevents this since you only look at previously seen numbers
- **Exactly one solution guaranteed** → no need to handle "no answer" case, but returning `[]` is clean

---

## Pattern Recognition

This problem teaches the **complement lookup with hash map** pattern.
You'll see this same idea in:

- Two Sum II (sorted array — use two pointers instead)
- 3Sum (sort + two pointers, but same complement idea)
- 4Sum
- Subarray Sum Equals K

Whenever you see "find two things that combine to a target" → think **hash map + complement**.
