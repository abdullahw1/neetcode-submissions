# Valid Palindrome

**Difficulty:** Easy
**Pattern:** Two Pointers

---

## Prerequisites

Before this problem, you should understand:
- **What a pointer is** — just a variable that holds an index (a position) in a string or array. `left = 0` means "I'm pointing at the first character."
- **Two pointers** — using two index variables, one starting at the left end and one at the right end, moving them toward each other. This is a core pattern you'll use constantly.
- **`isalnum()`** — a built-in Python method that returns `True` if a character is a letter or digit, `False` for spaces, punctuation, etc.
- **`.lower()`** — converts a character to lowercase so `'A'` and `'a'` compare as equal.

---

## Neetcode Problem

Given a string `s`, return `true` if it is a palindrome, otherwise return `false`.

A palindrome reads the same forward and backward. It is **case-insensitive** and **ignores all non-alphanumeric characters** (spaces, punctuation, etc.).

---

## Problem (In My Own Words)

Strip out everything that isn't a letter or number, lowercase everything, then check if the result reads the same forwards and backwards.

`"Was it a car or a cat I saw?"` → clean it → `"wasitacaroracatisaw"` → palindrome ✅

---

## ELI5 (Feynman Explanation)

Imagine you're reading a word on a strip of paper. You fold the strip in half. If every letter on the left half matches the letter directly across from it on the right half — it's a palindrome.

Now imagine the strip has some junk on it — spaces, commas, question marks. You just ignore those and only compare the real letters and numbers.

**Two pointers** is exactly this folding trick:
- Put your left finger at the start of the strip
- Put your right finger at the end
- Move both fingers inward, skipping junk
- Compare what each finger is pointing at
- If they ever disagree → not a palindrome
- If they meet in the middle without disagreeing → palindrome ✅

---

## Visual Walkthrough

```
Input: s = "Was it a car or a cat I saw?"

Two pointers start at opposite ends:

s = "Was it a car or a cat I saw?"
     ^                           ^
     L                           R

Step 1: L='W', R='?' → '?' is not alphanumeric, move R left
        L='W', R='w' → both alphanumeric
        'w' == 'w' ✅ → move both inward

Step 2: L='a', R=' ' → skip space, R moves left
        L='a', R='a' → 'a' == 'a' ✅ → move both inward

Step 3: L='s', R='w' → wait...
        Actually: "wasitacaroracatisaw" — let's trace the cleaned version:

Cleaned: w a s i t a c a r o r a c a t i s a w
         ^                                   ^
         L                                   R

L=w, R=w ✅ → move in
L=a, R=a ✅ → move in
L=s, R=s ✅ → move in
L=i, R=i ✅ → move in
L=t, R=t ✅ → move in
L=a, R=a ✅ → move in
L=c, R=c ✅ → move in
L=a, R=a ✅ → move in
L=r, R=r ✅ → move in
L meets R in the middle → return True ✅
```

```
Input: s = "tab a cat"

Cleaned: t a b a c a t
         ^           ^
         L           R

L=t, R=t ✅ → move in
L=a, R=a ✅ → move in
L=b, R=c ❌ → return False ✅
```

---

## Interview Approach — How to Talk Through This

In an interview, here's how you'd walk through it:

**Step 1 — Brute force first:**
> "The obvious approach is to clean the string — filter out non-alphanumeric characters, lowercase everything — then check if it equals its reverse. That's O(n) time but O(n) space because I'm creating a new string."

**Step 2 — Optimize:**
> "I can do better on space. Instead of building a new string, I'll use two pointers — one at each end — and compare characters in-place. I skip non-alphanumeric characters as I go. This is still O(n) time but now O(1) space since I'm not allocating anything extra."

**Step 3 — Code it:**
> Use the two-pointer solution below.

This progression shows the interviewer you can think through trade-offs, not just memorize solutions.

---

## Solution 1: Two Pointers (Optimal) ⭐

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1       # start at both ends

        while left < right:
            # skip non-alphanumeric characters from the left
            while left < right and not s[left].isalnum():
                left += 1
            # skip non-alphanumeric characters from the right
            while left < right and not s[right].isalnum():
                right -= 1

            # compare the characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False               # mismatch — not a palindrome

            left += 1                      # move both pointers inward
            right -= 1

        return True                        # made it through — it's a palindrome
```

| Pros | Cons |
|---|---|
| O(1) space — no extra string created | Slightly more code than brute force |
| O(n) time — single pass | Inner while loops look scary but are still O(n) total |
| **Best for interviews — optimal time AND space** | |

---

## Solution 2: Reverse String (Brute Force)

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for c in s:
            if c.isalnum():
                cleaned += c.lower()       # build cleaned string
        return cleaned == cleaned[::-1]    # compare to its reverse
```

| Pros | Cons |
|---|---|
| Super clean and readable | O(n) extra space for the cleaned string |
| Easy to write quickly | Creates two strings (cleaned + reversed) |
| Good starting point to mention | Not optimal on space |

---

## Both Compared

| Approach | Time | Space | Notes |
|---|---|---|---|
| Reverse string | O(n) | O(n) | Simple, mention as brute force |
| **Two pointers** | **O(n)** | **O(1)** | **Optimal — use this as your final answer** |

Both are O(n) time. The difference is space. The two-pointer approach avoids creating any new strings — it works directly on the original.

---

## Why Are the Inner While Loops Still O(n)?

Same question as Longest Consecutive Sequence — nested loops look like O(n²) but aren't always.

Here, `left` and `right` only ever move toward each other. They never go backwards. So across the entire run of the outer while loop, `left` moves at most n times total and `right` moves at most n times total. Total work = O(n).

---

## Complexity Analysis

| | Complexity | Why |
|---|---|---|
| **Time** | O(n) | Each character visited at most once |
| **Space** | O(1) | No extra strings — just two integer pointers |

---

## Gotchas & Edge Cases

- **Empty string** → `""` is a palindrome (vacuously true), the while loop never runs → `True`
- **Single character** → `"a"` → `left == right` immediately → `True`
- **All non-alphanumeric** → `"!!!"` → both pointers skip everything, never compare → `True`
- **Mixed case** → `"Aba"` → lowercase both before comparing → `True`
- **Numbers** → `"12321"` → digits count as alphanumeric → `True`
- **Don't forget the inner `left < right` guard** — without it, the inner while loops could cross each other

---

## Pattern Recognition

This problem introduces the **two pointers** pattern — one of the most important patterns in coding interviews.

You'll use two pointers in:
- Two Sum II (sorted array)
- 3Sum
- Container With Most Water
- Trapping Rain Water
- Remove Duplicates from Sorted Array

Whenever you see "compare from both ends" or "find a pair that satisfies a condition" → think **two pointers**.
