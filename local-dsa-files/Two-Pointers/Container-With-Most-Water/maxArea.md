# Container With Most Water

**Difficulty:** Medium
**Pattern:** Two Pointers (Greedy)

---

## Prerequisites

Before this problem, you should understand:
- **Two pointers** — one at each end, moving inward. Same pattern as Valid Palindrome and Two Sum II.
- **Area of a rectangle** — `width × height`. The width is the distance between the two pointers. The height is the shorter of the two lines (water overflows over the shorter side).
- **Greedy reasoning** — why moving the shorter pointer is always the right move. This is the key insight.

---

## Neetcode Problem

Given an array `heights` where `heights[i]` is the height of a bar at position `i`, choose any two bars to form a container. Return the maximum amount of water the container can hold.

---

## Problem (In My Own Words)

Pick two bars. They form the walls of a container. The water level is limited by the shorter bar. The width is the distance between them. Find the pair that holds the most water.

```
Water = min(left_height, right_height) × distance_between_them
```

---

## ELI5 (Feynman Explanation)

Imagine you're holding a plank of wood in each hand, standing in a pool. The water level can only go as high as your shorter plank — any higher and it spills over.

You start with your arms stretched as wide as possible (maximum width). You look at your two planks:
- The left one is short, the right one is tall.
- The water level is limited by the short one.

Now you have a choice: move the short plank inward, or the tall plank inward?

- **Moving the tall plank** → the width shrinks, and the height can only stay the same or get worse (still limited by the short plank). You LOSE width and gain nothing. Bad move.
- **Moving the short plank** → the width shrinks, BUT you might find a taller plank that raises the water level. You MIGHT gain height. Worth trying.

So you always move the shorter plank inward. That's the greedy choice.

---

## The Key Insight — Why Move the Shorter Side?

This is the part interviewers want you to explain. Here's the logic:

```
area = min(heights[l], heights[r]) × (r - l)
```

The area is bottlenecked by the **shorter** side. If you move the taller side:
- Width decreases by 1 (guaranteed loss)
- Height stays the same or decreases (the min is still the short side)
- Area can only get worse or stay the same

If you move the shorter side:
- Width decreases by 1 (guaranteed loss)
- Height might increase (you might find a taller bar)
- Area might increase if the height gain outweighs the width loss

So moving the shorter side is the only move that has a *chance* of improving the area. Moving the taller side is provably useless.

---

## Hint Breakdown

**Hint 1:** Brute force checks every pair — O(n²). Can you do better?

**Hint 2:** Two pointers. The formula is `(r - l) × min(heights[l], heights[r])`.

**Hint 3:** Start wide (pointers at both ends). Move the pointer at the shorter height inward.

**Hint 4:** The area depends on the minimum height. Replacing the shorter height is the only way to potentially increase the area.

---

## Visual Walkthrough

```
Input: heights = [1, 7, 2, 5, 4, 7, 3, 6]
                  ^                       ^
                  L                       R

Step 1: L=1, R=6, width=7
        area = min(1,6) × 7 = 1 × 7 = 7
        heights[L]=1 < heights[R]=6 → move L right
        max_area = 7

Step 2: L=7, R=6, width=6
        area = min(7,6) × 6 = 6 × 6 = 36
        heights[L]=7 > heights[R]=6 → move R left
        max_area = 36

Step 3: L=7, R=3, width=5
        area = min(7,3) × 5 = 3 × 5 = 15
        heights[R]=3 < heights[L]=7 → move R left
        max_area = 36

Step 4: L=7, R=7, width=4
        area = min(7,7) × 4 = 7 × 4 = 28
        heights[L]=heights[R] → move L right (either works)
        max_area = 36

Step 5: L=2, R=7, width=3
        area = min(2,7) × 3 = 2 × 3 = 6
        move L right
        max_area = 36

Step 6: L=5, R=7, width=2
        area = min(5,7) × 2 = 5 × 2 = 10
        move L right
        max_area = 36

Step 7: L=4, R=7, width=1
        area = min(4,7) × 1 = 4 × 1 = 4
        move L right
        max_area = 36

L meets R → done.
Output: 36 ✅
```

---

## Solution (Two Pointers — Optimal) ⭐

```python
class Solution:
    def maxArea(self, heights: list[int]) -> int:
        left, right = 0, len(heights) - 1    # start as wide as possible
        max_area = 0

        while left < right:
            # calculate area with current pair
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height
            max_area = max(max_area, area)

            # move the shorter side inward (greedy choice)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return max_area
```

---

## Brute Force (For Reference)

```python
class Solution:
    def maxArea(self, heights: list[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                area = min(heights[i], heights[j]) * (j - i)
                max_area = max(max_area, area)
        return max_area
```

| Pros | Cons |
|---|---|
| Dead simple, checks every pair | O(n²) — too slow for large inputs |
| Good to mention as starting point | Doesn't use any clever insight |

---

## Both Compared

| Approach | Time | Space | Notes |
|---|---|---|---|
| Brute force | O(n²) | O(1) | Check every pair |
| **Two pointers** | **O(n)** | **O(1)** | **Greedy — always move the shorter side** |

---

## Interview Approach — How to Talk Through This

**Step 1:** "Brute force is O(n²) — check every pair. But I can do better."

**Step 2:** "I'll use two pointers starting at both ends — that gives me the maximum width. The area formula is `min(left, right) × width`."

**Step 3:** "The key insight is which pointer to move. Moving the taller side can never help because the height is bottlenecked by the shorter side. Moving the shorter side might find a taller bar that increases the area. So I always move the shorter one."

**Step 4:** "This is greedy — at each step I make the locally optimal choice (move the shorter side) and it leads to the globally optimal answer."

---

## This Is NOT Trapping Rain Water

Common confusion. The difference:
- **Container With Most Water** → pick TWO bars, find the max area between them
- **Trapping Rain Water** → sum up ALL the water trapped between ALL bars

Different problems, different solutions. Don't mix them up.

---

## Complexity Analysis

| | Complexity | Why |
|---|---|---|
| **Time** | O(n) | Each pointer moves at most n times total |
| **Space** | O(1) | Just two pointers and a max variable |

---

## Gotchas & Edge Cases

- **Equal heights** → `heights[l] == heights[r]` — move either pointer, both are valid
- **All same height** → `[2, 2, 2]` → widest pair wins: `2 × 2 = 4`
- **Decreasing array** → `[5, 4, 3, 2, 1]` → first pair is best (widest × min)
- **Width is `r - l`** not `r - l + 1` — the bars are at positions l and r, the water is between them
- **Height 0** → a bar with height 0 holds no water, pointer moves past it immediately

---

## Pattern Recognition

This problem teaches the **greedy two-pointer** pattern — start wide, shrink inward, always make the move that has a chance of improving the answer.

You'll see similar reasoning in:
- Trapping Rain Water (two pointers, but summing water)
- Two Sum II (move based on sum comparison)
- Shortest Unsorted Continuous Subarray

Whenever you see "maximize/minimize something with two endpoints" → think **two pointers from both ends + greedy move**.
