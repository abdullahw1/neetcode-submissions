# Group Anagrams

**Difficulty:** Medium
**Pattern:** Hash Map / Frequency Key

---

## Neetcode Problem

Given an array of strings `strs`, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

---

## Problem (In My Own Words)

You get a list of words. Put all the words that are anagrams of each other into the same group. Return a list of those groups.

---

## ELI5 (Feynman Explanation)

Imagine you're a teacher and you give every kid in class a bag of letter tiles.
You tell them: "Everyone with the exact same letters in their bag, go stand in the same corner."

- "act" has tiles {a, c, t}
- "cat" has tiles {a, c, t} → same corner!
- "stop" has tiles {o, p, s, t}
- "pots" has tiles {o, p, s, t} → same corner!

But how do you quickly figure out who belongs together? You tell each kid:
"Sort your tiles alphabetically and read them out."

- "act" → "act"
- "cat" → "act" ← same!
- "stop" → "opst"
- "pots" → "opst" ← same!

Now the sorted version is like a **name tag** for each group. Kids with the same name tag go together. That name tag is the **key** in your hash map.

---

## The Key Insight

Two words are anagrams if they have the same characters. If you sort both words, anagrams become **identical strings**.

```
"act"  → sorted → "act"
"cat"  → sorted → "act"   ← same key!
"stop" → sorted → "opst"
"pots" → sorted → "opst"  ← same key!
```

So the strategy is: **sort each word, use the sorted version as a dictionary key, and group words under the same key.**

---

## Visual Walkthrough

```
Input: strs = ["act", "pots", "tops", "cat", "stop", "hat"]

Word "act"  → sorted = "act"  → groups = {"act": ["act"]}
Word "pots" → sorted = "opst" → groups = {"act": ["act"], "opst": ["pots"]}
Word "tops" → sorted = "opst" → groups = {"act": ["act"], "opst": ["pots", "tops"]}
Word "cat"  → sorted = "act"  → groups = {"act": ["act", "cat"], "opst": ["pots", "tops"]}
Word "stop" → sorted = "opst" → groups = {"act": ["act", "cat"], "opst": ["pots", "tops", "stop"]}
Word "hat"  → sorted = "aht"  → groups = {"act": ["act", "cat"], "opst": ["pots", "tops", "stop"], "aht": ["hat"]}

Output: [["act", "cat"], ["pots", "tops", "stop"], ["hat"]] ✅
```

---

## Solution (Sorting as Key)

```python
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}
        for word in strs:
            key = "".join(sorted(word))            # sort the letters → anagram "name tag"
            groups.setdefault(key, []).append(word) # group under that key
        return list(groups.values())
```

This is your solution — clean and easy to explain. `setdefault` is a nice one-liner that says "if this key doesn't exist yet, create it with an empty list, then append."

---

## Optimal Solution (Character Count as Key)

```python
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for word in strs:
            count = [0] * 26                       # 26 slots for a-z
            for char in word:
                count[ord(char) - ord('a')] += 1   # tally each letter
            groups[tuple(count)].append(word)       # use the count as the key
        return list(groups.values())
```

**Why this is technically better:**
- Sorting each word is O(n log n) where n = word length
- Counting characters is O(n) — just loop through once
- For long words, counting beats sorting

**But honestly?** The sorting solution is easier to write, easier to explain, and interviewers are usually happy with it. Mention the counting approach as a follow-up optimization if they ask.

---

## How the Count Key Works

```
"act" → count = [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
                  a   c                                   t
"cat" → count = [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
                  a   c                                   t
Same tuple → same group ✅
```

We use `tuple(count)` because lists can't be dictionary keys in Python (they're mutable), but tuples can.

---

## Complexity Analysis

| Approach | Time | Space | Notes |
|---|---|---|---|
| **Sorting as key** | **O(m · n log n)** | **O(m · n)** | Easy to write, good enough for interviews |
| Character count as key | O(m · n) | O(m · n) | Optimal, mention as follow-up |

Where m = number of strings, n = length of the longest string.

---

## Gotchas & Edge Cases

- **Empty string** → `""` sorted is still `""`, groups correctly with other empty strings
- **Single word** → returns `[["x"]]` — one group with one word
- **All same word** → `["aaa", "aaa"]` → `[["aaa", "aaa"]]`
- **Output order doesn't matter** — the problem says you can return groups in any order
- `setdefault` vs `defaultdict` — both work, `setdefault` avoids the import

---

## Pattern Recognition

This problem teaches the **canonical key grouping** pattern — transform each item into a standard form and use it as a hash map key to group related items.

You'll see this same idea in:
- Valid Anagram (same frequency concept, just for 2 strings)
- Group Shifted Strings
- Find All Anagrams in a String

Whenever you see "group things that share a property" → think **hash map with a canonical key**.
