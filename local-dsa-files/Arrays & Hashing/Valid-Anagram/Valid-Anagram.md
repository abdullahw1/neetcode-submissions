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

## Solution 1: Hash Map (Best for Interviews) ⭐

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):       # different lengths → can't be anagrams
            return False

        count_s, count_t = {}, {}

        for i in range(len(s)):    # single loop since lengths are equal
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1

        return count_s == count_t
```

| Pros | Cons |
|---|---|
| O(n) time — one pass through both strings | Uses O(1) space (at most 26 keys) but still a hash map |
| `len` check short-circuits immediately | Two dictionaries (could use one — see Solution 2) |
| `.get(key, 0)` is clean Python | |
| **Easy to explain, easy to write on a whiteboard** | |

---

## Solution 2: Character Frequency Array (Most Optimal) 🧠

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26                          # 26 slots for a-z
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1      # s increments
            count[ord(t[i]) - ord('a')] -= 1      # t decrements

        for val in count:
            if val != 0:                           # any imbalance = not anagram
                return False
        return True
```

**How it works:** Instead of two dictionaries, use one array of 26 zeros. For each character in `s`, add 1. For each character in `t`, subtract 1. If they're anagrams, every slot ends at 0 — every increment was perfectly cancelled by a decrement.

| Pros | Cons |
|---|---|
| Single array instead of two hash maps | Only works for lowercase a-z (fixed character set) |
| No hashing overhead — pure array indexing | `ord()` math is slightly less readable |
| Technically the fastest approach | Harder to extend to Unicode/mixed case |
| Great follow-up answer if interviewer pushes | |

---

## Solution 3: Sorting (Brute Force)

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
```

| Pros | Cons |
|---|---|
| One-liner, dead simple | O(n log n) — sorting is the bottleneck |
| Easy to remember under pressure | Interviewer will say "can you do better?" |
| Good starting point to mention | Creates new sorted lists (extra space) |

Use this as your "here's the obvious approach" then upgrade to the hash map.

---

## All Three Compared

| Approach | Time | Space | When to use |
|---|---|---|---|
| Sorting | O(n log n) | O(n) | Mention as brute force, then improve |
| **Hash Map** | **O(n)** | **O(1)** | **Default interview answer** |
| Frequency Array | O(n) | O(1) | Follow-up if they want you to optimize further |

Space is O(1) for both hash map and array because there are at most 26 lowercase letters — the space doesn't grow with input size.

---

## Interview Strategy

1. **Start** by mentioning sorting — "I could sort both and compare, but that's O(n log n)"
2. **Present** the hash map solution — clean, optimal, easy to explain
3. **If they push** for more optimization, mention the frequency array — "since we know it's only lowercase a-z, I can use a fixed array of 26 and avoid hashing entirely"

This shows you can think through trade-offs, which is what they're really testing.

---

## Gotchas & Edge Cases

- **Different lengths** → immediately `False`, no need to count anything. Always check this first.
- **Empty strings** → two empty strings are anagrams (`"" == ""`)
- **Single character** → `"a"` and `"a"` → `True`, `"a"` and `"b"` → `False`
- **Case sensitivity** — this problem assumes same case. In a real interview, ask! "Should I treat 'A' and 'a' as the same?"

---

## Pattern Recognition

This problem teaches the **frequency count with hash map** pattern.
You'll see this same idea in:

- Group Anagrams (frequency as a key)
- Top K Frequent Elements
- Ransom Note
- First Unique Character in a String

Whenever you see "compare frequencies" or "count occurrences" → think **hash map**.
