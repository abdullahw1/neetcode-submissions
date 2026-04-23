# Top K Frequent Elements

**Difficulty:** Medium
**Pattern:** Hash Map + Bucket Sort

---

## Neetcode Problem

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. The answer is always unique. You may return the output in any order.

---

## Problem (In My Own Words)

Count how many times each number appears, then return the `k` numbers that show up the most.

---

## ELI5 (Feynman Explanation)

Imagine you're a teacher and you ask your class: "What's your favorite fruit?"

Kids shout out answers:
- "Apple! Apple! Apple! Banana! Banana! Orange!"

You tally it up on the whiteboard:
- Apple: 3
- Banana: 2
- Orange: 1

Now someone asks: "What are the top 2 favorites?"

You could sort your tally sheet and read from the bottom — that works but it's slow if you have thousands of fruits.

Or you could be clever. Make a row of buckets numbered 1 through 6 (one for each possible count).
Drop each fruit into the bucket matching its count:

```
Bucket 1: [Orange]
Bucket 2: [Banana]
Bucket 3: [Apple]
Bucket 4: []
Bucket 5: []
Bucket 6: []
```

Now just walk backwards from bucket 6 → pick fruits until you have k. Done.

That's **bucket sort** — you skip sorting entirely by using the count itself as a position.

---

## The Key Insight

Every problem like this has two steps:
1. **Count frequencies** (hash map)
2. **Find the top k** (this is where the approaches differ)

The trick with bucket sort is realizing: the maximum possible frequency is `len(nums)`. So you can make an array of that size and use the frequency as the index. No sorting needed.

---

## Visual Walkthrough (Bucket Sort)

```
Input: nums = [1, 1, 1, 2, 2, 3], k = 2

Step 1 — Count frequencies:
  count = {1: 3, 2: 2, 3: 1}

Step 2 — Build buckets (index = frequency):
  freq[0] = []
  freq[1] = [3]        ← 3 appears 1 time
  freq[2] = [2]        ← 2 appears 2 times
  freq[3] = [1]        ← 1 appears 3 times
  freq[4] = []
  freq[5] = []
  freq[6] = []

Step 3 — Walk backwards, collect k=2 elements:
  freq[6] → empty, skip
  freq[5] → empty, skip
  freq[4] → empty, skip
  freq[3] → [1] → res = [1]       (need 1 more)
  freq[2] → [2] → res = [1, 2]    (got 2, done!)

Output: [1, 2] ✅
```

---

## Solution 1: Bucket Sort (Optimal) ⭐

```python
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]  # buckets 0..n

        for num in nums:                            # step 1: count
            count[num] = 1 + count.get(num, 0)

        for num, cnt in count.items():              # step 2: drop into buckets
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):      # step 3: walk backwards
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
```

| Pros | Cons |
|---|---|
| O(n) time — no sorting at all | Uses O(n) extra space for the bucket array |
| Easy to explain once you see it | Slightly more code than sorting |
| **Best for interviews — this is what they want** | |

**Time: O(n) · Space: O(n)**

---

## Solution 2: Sorting

```python
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
```

| Pros | Cons |
|---|---|
| Simple and intuitive | O(n log n) — sorting is the bottleneck |
| Easy to write on a whiteboard | Interviewer will ask "can you do better?" |
| Good starting point to mention | Not optimal |

**Time: O(n log n) · Space: O(n)**

Use this as your "brute force" answer, then optimize to bucket sort.

---

## Solution 3: Min-Heap

```python
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)     # kick out the least frequent

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
```

| Pros | Cons |
|---|---|
| O(n log k) — faster than full sort when k is small | Harder to explain than bucket sort |
| Classic "top k" pattern used in many problems | Still not O(n) |
| Shows you know heaps (interviewers like that) | More code, easy to mess up |

**Time: O(n log k) · Space: O(n + k)**

Good to know for other "top k" problems, but bucket sort is simpler here.

---

## All Three Compared

| Approach | Time | Space | When to use |
|---|---|---|---|
| Sorting | O(n log n) | O(n) | Mention as brute force, then improve |
| Min-Heap | O(n log k) | O(n + k) | When k << n, or for streaming data |
| **Bucket Sort** | **O(n)** | **O(n)** | **Default answer for this problem** |

**Interview strategy:** Start by explaining sorting (shows you understand the problem), then jump to bucket sort (shows you can optimize). Mention the heap if they ask about alternatives.

---

## Why Min-Heap and Not Max-Heap?

This trips people up. Intuition says "I want the max frequent, so use a max-heap." But:

- **Min-heap of size k**: you push elements in, and whenever the heap exceeds k, you pop the *smallest*. What's left? The k *largest*. Efficient — heap never grows past k.
- **Max-heap**: you'd have to push ALL elements, then pop k times. The heap grows to size n, which defeats the purpose.

The min-heap acts like a bouncer at a club with a capacity of k — it always kicks out the weakest.

---

## Gotchas & Edge Cases

- **Off-by-one in bucket sort** — you need `len(nums) + 1` buckets because a number could appear `n` times (index `n` needs to exist)
- **Single element** → `[7, 7]`, k=1 → `[7]`
- **All same frequency** → any k of them is valid since the answer is guaranteed unique
- **k equals number of distinct elements** → return everything

---

## Pattern Recognition

This problem teaches the **frequency counting + bucket sort** pattern.

You'll see frequency counting in:
- Valid Anagram (compare two frequency maps)
- Group Anagrams (frequency as a key)
- Sort Characters By Frequency

You'll see "top k" in:
- K Closest Points to Origin (heap)
- Kth Largest Element (quickselect)
- Top K Frequent Words

Whenever you see "top k" or "most frequent" → think **count first, then bucket sort or heap**.
