# Encode and Decode Strings

**Difficulty:** Medium
**Pattern:** Length-Prefix Encoding

---

## Neetcode Problem

Design an algorithm to encode a list of strings into a single string. The encoded string is sent over a network and decoded back to the original list of strings.

---

## Problem (In My Own Words)

Turn a list of strings into ONE string, then turn that one string back into the original list. The tricky part: the strings can contain *any* character — commas, colons, even `#`. So you can't just join them with a delimiter.

---

## ELI5 (Feynman Explanation)

Imagine you're packing boxes to ship. Each box has stuff inside, and you need to label them so the person on the other end knows how to unpack.

You can't just tape the boxes together and hope they figure it out — what if one box has tape inside it? They'd get confused about where one box ends and the next begins.

So you write a label on each box: **"this box has 4 items inside"**, then the items.

```
Box label: 4 items → [n, e, e, t]
Box label: 4 items → [c, o, d, e]
```

When unpacking, you read the label → grab exactly that many items → move to the next label.

That's **length-prefix encoding**: before each string, you write its length, then a `#` separator, then the string itself. The length tells you *exactly* how many characters to read, so it doesn't matter what's inside the string.

---

## The Key Insight

Why can't you just use a delimiter like `,` or `|`?

Because the strings can contain ANY character. If a string is `"hello,world"` and you join with `,`, you'd get `"hello,world,foo"` — now you can't tell if that first comma is a delimiter or part of the string.

The length-prefix trick solves this completely. When you see `11#hello,world`, you know to read exactly 11 characters after the `#`. The comma inside doesn't matter — you're counting characters, not looking for delimiters.

---

## Visual Walkthrough

```
Encode: ["neet", "code", "love", "you"]

"neet" → len=4 → "4#neet"
"code" → len=4 → "4#code"
"love" → len=4 → "4#love"
"you"  → len=3 → "3#you"

Encoded string: "4#neet4#code4#love3#you"
```

```
Decode: "4#neet4#code4#love3#you"

i=0: read digits until '#' → "4" → length=4
     skip '#', read 4 chars → "neet"
     i moves to 7

i=7: read digits until '#' → "4" → length=4
     skip '#', read 4 chars → "code"
     i moves to 14

i=14: read digits until '#' → "4" → length=4
      skip '#', read 4 chars → "love"
      i moves to 21

i=21: read digits until '#' → "3" → length=3
      skip '#', read 3 chars → "you"
      i moves to 27

Output: ["neet", "code", "love", "you"] ✅
```

---

## Tricky Example — Why Delimiters Fail

```
Encode: ["5#hello", "world"]

With a naive delimiter approach, this breaks.
With length-prefix:

"5#hello" → len=7 → "7#5#hello"
"world"   → len=5 → "5#world"

Encoded: "7#5#hello5#world"

Decode:
i=0: read "7" → length=7, skip '#', read 7 chars → "5#hello" ✅
i=10: read "5" → length=5, skip '#', read 5 chars → "world" ✅

The "5#" inside the string doesn't confuse us because we're counting characters, not searching for '#'.
```

---

## Solution (Length-Prefix — Optimal) ⭐

```python
class Solution:

    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s   # length + separator + string
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":            # find the '#' separator
                j += 1
            length = int(s[i:j])           # everything before '#' is the length
            i = j + 1                      # skip past '#'
            j = i + length                 # jump exactly 'length' characters
            res.append(s[i:j])             # extract the string
            i = j                          # move to next encoded segment

        return res
```

---

## How the Decode Pointer Works

This is the part that trips people up, so let's be explicit:

```
Encoded: "4#neet4#code"
          ^
          i=0

Step 1: j scans forward to find '#'
        "4#neet4#code"
         ^
         j=1 (found '#')

        length = int("4") = 4
        i = 2 (skip past '#')
        j = 2 + 4 = 6
        extract s[2:6] = "neet"
        i = 6

Step 2: j scans forward to find '#'
        "4#neet4#code"
                ^
                j=7 (found '#')

        length = int("4") = 4
        i = 8 (skip past '#')
        j = 8 + 4 = 12
        extract s[8:12] = "code"
        i = 12 → done
```

Two pointers: `i` marks where you are, `j` scans ahead. That's it.

---

## Complexity Analysis

| | Complexity | Why |
|---|---|---|
| **Time (encode)** | O(m) | One pass through all characters |
| **Time (decode)** | O(m) | One pass through the encoded string |
| **Space** | O(m + n) | Storing the encoded/decoded strings |

Where m = sum of all string lengths, n = number of strings.

---

## Gotchas & Edge Cases

- **Empty list** `[]` → encode returns `""`, decode returns `[]`
- **List with empty string** `[""]` → encodes as `"0#"`, decodes back to `[""]`
- **Strings containing `#`** → works fine because length tells you exactly how far to read
- **Strings containing digits** → works fine, the `#` separates the length from the content
- **Multi-digit lengths** → `"12#helloworldhi"` — the decode loop reads all digits until `#`, not just one digit

---

## Pattern Recognition

This problem teaches **length-prefix encoding** — a real-world technique used in:

- Network protocols (TCP frames prefix data with length)
- Binary file formats
- Serialization (Protocol Buffers, MessagePack)

In interviews, whenever you see "encode/decode" or "serialize/deserialize" with arbitrary content → think **length-prefix**. It's the only approach that's truly safe against any character appearing in the data.
