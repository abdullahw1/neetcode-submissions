# Valid Anagram

**Difficulty:** Easy
**Pattern:** Hash Map / Frequency Count

---

## Neetcode Problem

Given two strings `s` and `t`, return `true` if the two strings are anagrams of each other, otherwise return `false`.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

---

## Problem (In My Own Words)

Given two words, check if they use the exact same letters the exact same number of times.
Same letters, same counts → `True`. Anything off → `False`.

---

## ELI5 (Feynman Explanation)

Imagine you have two bags of Scrabble tiles. Dump each bag out and sort the tiles into piles by letter.
Now compare the piles — does each letter have the same number of tiles in both bags?

- **Yes** → they're anagrams.
- **No** → they're not.

We use a **hash map (dictionary)** to count the tiles in each bag.

---

## Intuition — Why Does This Work?

Two strings are anagrams if and only if they have the **same character frequencies**.

- "racecar" and "carrace" → both have {r:2, a:2, c:2, e:1} → anagram ✅
- "jar" and "jam" → {j:1, a:1, r:1} vs {j:1, a:1, m:1} → not anagram ❌

So the whole problem boils down to: **count characters, compare counts**.

---

## Why Hash Map and Not Hash Set?

- A **set** only tracks *existence* — "is this character present?"
- A **dictionary/hash map** tracks *frequency* — "how many times does this character appear?"
- For anagrams, "a" appearing once vs twice matters. You need counts, not just presence.

---

## Visual Walkthrough

```
Input: s = "racecar", t = "carrace"

Build count_s:
  r → 1, a → 1, c → 1, e → 1, c → 2, a → 2, r → 2
  count_s = {r:2, a:2, c:2, e:1}

Build count_t:
  c → 1, a → 1, r → 1, r → 2, a → 2, c → 2, e → 1
  count_t = {c:2, a:2, r:2, e:1}

count_s == count_t? YES → return True ✅
```

```
Input: s = "jar", t = "jam"

count_s = {j:1, a:1, r:1}
count_t = {j:1, a:1, m:1}

count_s == count_t? NO → return False ✅
```

---

## Your Solution (Hash Map — Manual Counting)

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}

        for char in s:
            if char not in count_s:
                count_s[char] = 1
            else:
                count_s[char] += 1

        for char in t:
            if char not in count_t:
                count_t[char] = 1
            else:
                count_t[char] += 1

        return count_s == count_t
```

This works and is totally valid for an interview. You're manually building frequency maps and comparing them.

---

## Cleaner Version (Same Idea, Less Code)

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):       # quick exit — different lengths can't be anagrams
            return False

        count_s = {}
        count_t = {}

        for i in range(len(s)):    # single loop since lengths are equal
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1

        return count_s == count_t
```

**Why this is better for interviews:**
- The `len` check at the top is an instant O(1) short-circuit — interviewers love seeing you handle the obvious case first
- `.get(key, 0)` replaces the if/else block — shows you know Python idioms
- Single loop instead of two — same time complexity but cleaner to read and write on a whiteboard

---

## Brute Force (Sorting)

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
```

One-liner, easy to remember. But interviewers will ask you to do better because sorting is O(n log n).

---

## Complexity Analysis

| Approach | Time | Space | Notes |
|---|---|---|---|
| **Hash map (your solution)** | **O(n)** | **O(n)** | **Optimal — use this in interviews** |
| Sorting | O(n log n) | O(n) | Simple but slower |

Where n = length of the strings.

---

## Gotchas & Edge Cases

- **Different lengths** → immediately `False`, no need to count anything
- **Empty strings** → two empty strings are anagrams (`"" == ""`)
- **Single character** → `"a"` and `"a"` → `True`, `"a"` and `"b"` → `False`
- **Case sensitivity** — this problem assumes same case. In a real interview, ask!

---

## Pattern Recognition

This problem teaches the **frequency count with hash map** pattern.
You'll see this same idea in:

- Group Anagrams (frequency as a key)
- Top K Frequent Elements
- Ransom Note
- First Unique Character in a String

Whenever you see "compare frequencies" or "count occurrences" → think **hash map**.
