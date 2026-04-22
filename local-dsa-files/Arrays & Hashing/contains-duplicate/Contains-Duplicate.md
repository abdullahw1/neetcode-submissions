# Contains Duplicate

**Difficulty:** Easy
**Pattern:** Hash Set / Frequency Check

---

## Problem (In My Own Words)

Given an array of integers, figure out if any number shows up more than once.
That's it. Duplicates? → `True`. All unique? → `False`.

---

## ELI5 (Feynman Explanation)

Imagine you have a bag of marbles. You pick them out one at a time.
Before dropping each marble into a bowl, you glance at the bowl —
"Have I seen this color before?"

- **Yes** → you found a duplicate, stop.
- **No** → toss it in the bowl, grab the next marble.

The "bowl" is a **hash set** — it lets you check "is this already here?" instantly.

---

## Intuition — Why Does This Work?

- **Brute force** would compare every pair → O(n²). Slow.
- A **set** gives O(1) lookup. So instead of comparing against every element,
  you just ask the set: "seen this before?"
- One pass through the array, one check per element → O(n) total.

The key insight: **trading space for time**. We use extra memory (the set)
to avoid redundant comparisons.

---

## Visual Walkthrough

```
Input: nums = [1, 2, 3, 3]

Step 1: num = 1
        seen = {}
        1 in seen? NO → add it
        seen = {1}

Step 2: num = 2
        seen = {1}
        2 in seen? NO → add it
        seen = {1, 2}

Step 3: num = 3
        seen = {1, 2}
        3 in seen? NO → add it
        seen = {1, 2, 3}

Step 4: num = 3
        seen = {1, 2, 3}
        3 in seen? YES → return True ✅
```

```
Input: nums = [1, 2, 3, 4]

Steps 1-4: each number is new, added to seen
           seen = {1, 2, 3, 4}
           Loop ends → return False ✅
```

---

## Solution

```python
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()          # our "bowl" of marbles
        for num in nums:      # pick each marble
            if num in seen:   # already in the bowl?
                return True   # duplicate found!
            seen.add(num)     # nope — toss it in
        return False          # went through all, no dupes
```

---

## Complexity Analysis

| | Complexity | Why |
|---|---|---|
| **Time** | O(n) | Single pass through the array. `in` check on a set is O(1) average. |
| **Space** | O(n) | Worst case, all elements are unique → set holds n items. |

---

## Alternative Approaches

| Approach | Time | Space | Trade-off |
|---|---|---|---|
| Brute force (nested loops) | O(n²) | O(1) | No extra memory, but way too slow |
| Sort first, check neighbors | O(n log n) | O(1)* | Decent, but sorting modifies input |
| **Hash set (this solution)** | **O(n)** | **O(n)** | **Optimal time, uses extra space** |

*O(1) extra space if you sort in-place, but you mutate the input array.

---

## Gotchas & Edge Cases

- **Empty array** → no duplicates, return `False`
- **Single element** → can't have a duplicate, return `False`
- **All same elements** → caught on the second element immediately
- Don't overthink it — this is a "do you know what a set is?" problem

---

## Pattern Recognition

This problem teaches the **hash set for uniqueness** pattern.
You'll see this same idea in:

- Two Sum (hash map variant)
- Valid Anagram
- Longest Substring Without Repeating Characters
- Group Anagrams

Whenever you see "find duplicates" or "check uniqueness" → think **set**.
