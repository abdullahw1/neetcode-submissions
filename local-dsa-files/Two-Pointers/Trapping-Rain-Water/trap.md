# Trapping Rain Water

**Difficulty:** Hard
**Pattern:** Two Pointers / Prefix-Suffix Max

---

## Prerequisites

Before this problem, you should understand:
- **Container With Most Water** — you just did this. That problem picks TWO bars and finds the area between them. This problem sums up ALL the water trapped across the ENTIRE elevation map. Different problem, but same two-pointer intuition.
- **Prefix/Suffix arrays** — same idea as Products of Array Except Self. For each position, you need to know the tallest bar to the left and the tallest bar to the right.
- **Two pointers** — one at each end, moving inward. The pointer on the shorter side moves because that side determines the water level.

---

## Neetcode Problem

Given an array of non-negative integers `height` representing an elevation map (each bar has width 1), return the total amount of water that can be trapped between the bars.

---

## Problem (In My Own Words)

Imagine the bars as a cross-section of terrain. It rains. Water fills in the gaps between tall bars. How much total water is trapped?

---

## ELI5 (Feynman Explanation)

Imagine you're looking at a city skyline from the side. It rains. Water pools in the valleys between buildings.

For any single spot, ask: "How high can the water go here?"

The water level at any spot is determined by the **shorter** of the two tallest buildings on either side. Water can't go higher than the shorter wall — it would spill over.

```
Water at position i = min(tallest_left, tallest_right) - height[i]
```

If the building at position `i` is already taller than the water level, no water sits there (it's a peak, not a valley).

**The whole problem is just:** for every position, figure out the water level, subtract the ground height, and add it all up.

---

## The Core Formula

For each position `i`:

```
water[i] = min(max_left[i], max_right[i]) - height[i]
```

Where:
- `max_left[i]` = tallest bar from the left up to position `i`
- `max_right[i]` = tallest bar from the right up to position `i`
- The water level is the shorter of the two walls
- Subtract the ground height to get the water depth at that spot

Sum all the `water[i]` values = total trapped water.

---

## Hint Breakdown

**Hint 1:** How much water sits at ONE position? Look at the picture — it depends on the walls on either side.

**Hint 2:** `water[i] = min(left_max, right_max) - height[i]`. The water level is the shorter wall.

**Hint 3:** Brute force: for each position, scan left and right to find the max. That's O(n²). Can you precompute?

**Hint 4:** Build a prefix max array (left to right) and a suffix max array (right to left). Then one pass to calculate water. O(n) time, O(n) space. Can you do O(1) space? → Two pointers.

---

## Visual Walkthrough

```
Input: height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]

Elevation map (sideways):

3 |      #           #
2 |   #  #           #  #
1 |   #  #  #     #  #  #  #
0 | # #  #  #  #  #  #  #  #
  +--------------------------
    0  1  2  3  4  5  6  7  8  9

After rain fills in:

3 |      #  ~  ~  ~  #
2 |   #  #  ~  ~  ~  #  #
1 |   #  #  #  ~  #  #  #  #
0 | # #  #  #  #  #  #  #  #
  +--------------------------

Water at each position:
  i=0: min(0,3)-0 = 0  (left edge, no left wall)
  i=1: min(2,3)-2 = 0  (bar is at water level)
  i=2: min(2,3)-0 = 2  ← 2 units of water
  i=3: min(3,3)-3 = 0  (bar is at water level)
  i=4: min(3,3)-1 = 2  ← 2 units
  i=5: min(3,3)-0 = 3  ← 3 units
  i=6: min(3,3)-1 = 2  ← 2 units
  i=7: min(3,3)-3 = 0  (bar is at water level)
  i=8: min(3,3)-2 = 0  (wait — right max from here is only 1)
       Actually: min(3,2)-2 = 0
  i=9: min(3,1)-1 = 0  (right edge)

Total: 0+0+2+0+2+3+2+0+0+0 = 9 ✅
```

---

## Solution 1: Two Pointers (Optimal) ⭐

```python
class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        res = 0

        while left < right:
            if left_max < right_max:
                left += 1                              # move the shorter side
                left_max = max(left_max, height[left]) # update running max
                res += left_max - height[left]         # water = max - ground
            else:
                right -= 1
                right_max = max(right_max, height[right])
                res += right_max - height[right]

        return res
```

**Why this works:**
- If `left_max < right_max`, the water at the left pointer is determined by `left_max` (the shorter wall). We don't need to know the exact right max — we just know it's at least as tall as `right_max`, which is already bigger. So `left_max` is the bottleneck.
- Same logic in reverse for the right side.
- `left_max - height[left]` is always ≥ 0 because `left_max` is updated to be at least `height[left]`.

---

## Solution 2: Prefix & Suffix Arrays (Easier to Understand)

```python
class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        left_max = [0] * n                    # left_max[i] = tallest bar from 0..i
        right_max = [0] * n                   # right_max[i] = tallest bar from i..n-1

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        res = 0
        for i in range(n):
            res += min(left_max[i], right_max[i]) - height[i]

        return res
```

| Pros | Cons |
|---|---|
| Very clear — you can see left_max and right_max explicitly | O(n) extra space for two arrays |
| Great for explaining the concept | Interviewer may ask for O(1) space |
| Good stepping stone to the two-pointer solution | |

**Interview tip:** Explain this version first to show you understand the formula, then optimize to two pointers for O(1) space.

---

## All Approaches Compared

| Approach | Time | Space | Notes |
|---|---|---|---|
| Brute force (scan left/right each time) | O(n²) | O(1) | Too slow |
| Prefix/Suffix arrays | O(n) | O(n) | Clear, explain first |
| Stack (monotonic) | O(n) | O(n) | Works but harder to explain |
| **Two pointers** | **O(n)** | **O(1)** | **Optimal — final interview answer** |

---

## Interview Approach — How to Talk Through This

**Step 1 — The formula:**
> "Water at any position = min(tallest bar to the left, tallest bar to the right) minus the height at that position."

**Step 2 — Prefix/suffix:**
> "I can precompute the left max and right max arrays in O(n), then one pass to sum up the water. That's O(n) time, O(n) space."

**Step 3 — Optimize to two pointers:**
> "I can eliminate the arrays by using two pointers. The key insight: if left_max < right_max, the water at the left pointer is determined by left_max regardless of what's further to the right. So I move the shorter side inward and calculate water as I go. O(n) time, O(1) space."

---

## Container With Most Water vs Trapping Rain Water

| | Container With Most Water | Trapping Rain Water |
|---|---|---|
| What you're finding | Max area between TWO bars | Total water across ALL bars |
| Formula | `min(h[l], h[r]) × (r-l)` | `sum of min(left_max, right_max) - h[i]` |
| Answer | One number (max area) | Sum of water at every position |
| Which pointer moves | The shorter bar | The side with the smaller max |
| Difficulty | Medium | Hard |

---

## Complexity Analysis

| | Complexity | Why |
|---|---|---|
| **Time** | O(n) | Each pointer moves at most n times |
| **Space** | O(1) | Just pointers and two max variables |

---

## Gotchas & Edge Cases

- **Edge bars can't hold water** — the leftmost and rightmost bars have no wall on one side
- **`left_max - height[left]` is never negative** — because `left_max` is updated BEFORE calculating water, and it's always ≥ `height[left]`
- **Flat terrain** → `[1, 1, 1]` → no water (no valleys)
- **Single peak** → `[0, 5, 0]` → no water (water spills off both sides)
- **Empty array** → return 0
- **All zeros** → `[0, 0, 0]` → no water

---

## Pattern Recognition

This problem combines **prefix/suffix** (from Products of Array Except Self) with **two pointers** (from Container With Most Water).

The "for each position, what's the max on each side?" pattern shows up in:
- Products of Array Except Self (prefix/suffix products)
- Largest Rectangle in Histogram
- Daily Temperatures (monotonic stack variant)

Whenever you see "for each position, compute something based on the rest of the array" → think **prefix/suffix or two pointers**.
