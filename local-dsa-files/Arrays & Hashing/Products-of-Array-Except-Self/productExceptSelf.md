# Products of Array Except Self

**Difficulty:** Medium
**Pattern:** Prefix & Suffix Products

---

## Prerequisites

Before this problem, you should understand:
- **What a product is** — just multiplying numbers together. `2 × 3 × 4 = 24`.
- **Prefix sums/products** — the idea of building a running total from left to right. If you've seen prefix sums, this is the same thing but with multiplication.
- **Multiple passes through an array** — sometimes one loop isn't enough. This problem uses two passes (left-to-right, then right-to-left).

---

## Neetcode Problem

Given an integer array `nums`, return an array `output` where `output[i]` is the product of all elements of `nums` except `nums[i]`.

Follow-up: solve it in O(n) time **without using division**.

---

## Problem (In My Own Words)

For each position in the array, multiply everything together *except* the number at that position. Return all those products as a new array.

---

## ELI5 (Feynman Explanation)

Imagine 4 kids standing in a line, each holding a number card:

```
Kid 0: [1]   Kid 1: [2]   Kid 2: [3]   Kid 3: [4]
```

You ask Kid 2: "What's the product of everyone else's numbers?"
Kid 2 thinks: "Everyone to my LEFT has 1 × 2 = 2. Everyone to my RIGHT has 4. So it's 2 × 4 = 8."

That's the whole algorithm:
1. For each kid, figure out the product of everyone to their **left**
2. For each kid, figure out the product of everyone to their **right**
3. Multiply those two numbers together

The trick is: you don't recalculate from scratch each time. You build a **running product** from the left, and another **running product** from the right. Each kid just peeks at the running total.

---

## The Key Insight

For any position `i`:

```
answer[i] = (product of everything LEFT of i) × (product of everything RIGHT of i)
```

If you precompute both sides, you just multiply them together. Two passes, done.

**Why not just use division?** You could do `total_product / nums[i]`, but:
- Division by zero breaks when `nums[i] = 0`
- The problem explicitly says "without division" as a follow-up
- Interviewers want to see the prefix/suffix approach

---

## Visual Walkthrough

```
Input: nums = [1, 2, 3, 4]

PASS 1 — Build prefix products (left to right):
  prefix starts at 1

  i=0: res[0] = 1         (nothing to the left)     prefix = 1 × 1 = 1
  i=1: res[1] = 1         (left product = 1)         prefix = 1 × 2 = 2
  i=2: res[2] = 2         (left product = 1×2)       prefix = 2 × 3 = 6
  i=3: res[3] = 6         (left product = 1×2×3)     prefix = 6 × 4 = 24

  res = [1, 1, 2, 6]   ← each slot has the product of everything to its LEFT

PASS 2 — Multiply by suffix products (right to left):
  postfix starts at 1

  i=3: res[3] = 6 × 1 = 6     (nothing to the right)   postfix = 1 × 4 = 4
  i=2: res[2] = 2 × 4 = 8     (right product = 4)       postfix = 4 × 3 = 12
  i=1: res[1] = 1 × 12 = 12   (right product = 4×3)     postfix = 12 × 2 = 24
  i=0: res[0] = 1 × 24 = 24   (right product = 4×3×2)   postfix = 24 × 1 = 24

  res = [24, 12, 8, 6] ✅
```

```
Verify manually:
  res[0] = 2×3×4 = 24 ✅
  res[1] = 1×3×4 = 12 ✅
  res[2] = 1×2×4 = 8  ✅
  res[3] = 1×2×3 = 6  ✅
```

---

## Solution 1: Prefix & Suffix (Optimal — O(1) Extra Space) ⭐

```python
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)

        prefix = 1                              # running product from the left
        for i in range(len(nums)):
            res[i] = prefix                     # store left product
            prefix *= nums[i]                   # include current for next position

        postfix = 1                             # running product from the right
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix                   # multiply by right product
            postfix *= nums[i]                  # include current for next position

        return res
```

**Why this is the best interview answer:**
- O(n) time, O(1) extra space (the output array doesn't count)
- No division — handles zeros naturally
- Two clean passes, easy to explain on a whiteboard
- No extra arrays needed — we reuse `res` for both passes

| Pros | Cons |
|---|---|
| Optimal time and space | Two passes (but still O(n)) |
| No division, no zero edge cases | The right-to-left pass can be confusing at first |
| Clean and concise | |

---

## Solution 2: Prefix & Suffix Arrays (Easier to Understand)

```python
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        left = [1] * n                         # left[i] = product of everything left of i
        right = [1] * n                        # right[i] = product of everything right of i

        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        res = []
        for i in range(n):
            res.append(left[i] * right[i])     # left product × right product
        return res
```

This is your current solution — it's the same idea but uses two separate arrays. Easier to see what's happening, but uses O(n) extra space.

| Pros | Cons |
|---|---|
| Very clear what left[] and right[] represent | O(n) extra space for two arrays |
| Great for learning the concept | Interviewer may ask you to optimize space |
| Good stepping stone to Solution 1 | |

**Interview tip:** Start by explaining this version (it's clearer), then say "I can optimize space by reusing the result array" and show Solution 1.

---

## Solution 3: Brute Force

```python
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n
        for i in range(n):
            prod = 1
            for j in range(n):
                if i != j:
                    prod *= nums[j]
            res[i] = prod
        return res
```

| Pros | Cons |
|---|---|
| Dead simple, follows the problem statement directly | O(n²) — way too slow |
| Good to mention as starting point | Interviewer will immediately ask for better |

---

## All Three Compared

| Approach | Time | Space | When to use |
|---|---|---|---|
| Brute force | O(n²) | O(1) | Mention as "obvious approach" |
| Prefix/Suffix arrays | O(n) | O(n) | Explain the concept clearly |
| **Prefix/Suffix optimal** | **O(n)** | **O(1)** | **Final interview answer** |

---

## Why Does `prefix *= nums[i]` Come AFTER `res[i] = prefix`?

This is the part that confuses beginners. Think about it:

- `res[i]` should be the product of everything **before** `i` (not including `i`)
- So you store the running product **first**, then update it with `nums[i]`
- That way, `nums[i]` only affects positions **after** `i`

Same logic in reverse for the postfix pass.

---

## Complexity Analysis

| | Complexity | Why |
|---|---|---|
| **Time** | O(n) | Two passes through the array |
| **Space** | O(1) extra | Only the output array (which doesn't count per the problem) |

---

## Gotchas & Edge Cases

- **Zeros in the array** → prefix/suffix handles this naturally. No special cases needed.
- **`[-1, 0, 1, 2, 3]` → `[0, -6, 0, 0, 0]`** — only the position with 0 gets a non-zero result
- **Two elements** → `[2, 3]` → `[3, 2]` — simplest case, still works
- **Negative numbers** → the algorithm doesn't care about signs, multiplication handles it
- **Off-by-one** → `left[0]` and `right[n-1]` must start at 1 (nothing to the left/right)

---

## Pattern Recognition

This problem teaches the **prefix/suffix decomposition** pattern — break a problem into "everything before me" and "everything after me."

You'll see this same idea in:
- Trapping Rain Water (prefix max + suffix max)
- Best Time to Buy and Sell Stock
- Maximum Subarray (Kadane's is a prefix variant)

Whenever you see "compute something for each position based on the rest of the array" → think **prefix + suffix**.
