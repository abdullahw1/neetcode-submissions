# Valid Sudoku

**Difficulty:** Medium
**Pattern:** Hash Set / Duplicate Detection in 2D Grid

---

## Prerequisites

Before this problem, you should understand:
- **Hash sets** — used to check "have I seen this before?" in O(1). Same idea as Contains Duplicate, just applied to rows, columns, and boxes.
- **2D array traversal** — looping through a grid with `board[row][col]`.
- **Integer division** — `7 // 3 = 2`. This is how we figure out which 3×3 box a cell belongs to.

---

## Neetcode Problem

You are given a 9×9 Sudoku board. Return `true` if the board is valid based on these rules:
1. Each row must contain digits 1–9 without duplicates
2. Each column must contain digits 1–9 without duplicates
3. Each of the nine 3×3 sub-boxes must contain digits 1–9 without duplicates

The board doesn't need to be full or solvable — just no duplicates where there shouldn't be.

---

## Problem (In My Own Words)

Look at a partially filled Sudoku board. Check if anyone broke the rules — are there any duplicate numbers in the same row, same column, or same 3×3 box? If no duplicates, it's valid.

---

## ELI5 (Feynman Explanation)

Imagine you're a Sudoku referee. You walk around the board with three notebooks:

1. **Row notebook** — one page per row. You write down every number you see in that row.
2. **Column notebook** — one page per column. Same thing.
3. **Box notebook** — one page per 3×3 box. Same thing.

You go cell by cell, left to right, top to bottom. For each number you find:
- Check all three notebooks: "Have I written this number on this page before?"
- **Yes** → someone cheated, board is invalid. Stop.
- **No** → write it down in all three notebooks, move on.

If you get through the whole board without catching a cheat, it's valid.

The three notebooks are three **dictionaries of sets** — `rows`, `cols`, and `squares`.

---

## The Key Insight — How to Identify Which 3×3 Box?

This is the tricky part. The board has 9 boxes arranged in a 3×3 grid:

```
Box(0,0)  Box(0,1)  Box(0,2)
Box(1,0)  Box(1,1)  Box(1,2)
Box(2,0)  Box(2,1)  Box(2,2)
```

For any cell at `(row, col)`, its box is:

```
box = (row // 3, col // 3)
```

Examples:
- Cell (0, 0) → box (0, 0) — top-left
- Cell (1, 2) → box (0, 0) — still top-left
- Cell (4, 7) → box (1, 2) — middle-right
- Cell (8, 8) → box (2, 2) — bottom-right

The `// 3` groups rows 0-2 into box row 0, rows 3-5 into box row 1, rows 6-8 into box row 2. Same for columns.

---

## Visual Walkthrough

```
Board (partial):
  ["1","2",".",".","3",".",".",".","."],
  ["4",".",".","5",".",".",".",".","."],
  [".","9","1",".",".",".",".",".","3"],
  ...

Processing cell (0,0) = "1":
  row 0 seen? NO → rows[0] = {"1"}
  col 0 seen? NO → cols[0] = {"1"}
  box (0,0) seen? NO → squares[(0,0)] = {"1"}

Processing cell (0,1) = "2":
  row 0 seen? NO → rows[0] = {"1","2"}
  col 1 seen? NO → cols[1] = {"2"}
  box (0,0) seen? NO → squares[(0,0)] = {"1","2"}

Processing cell (0,2) = ".":
  Skip! Empty cell.

...

Processing cell (2,2) = "1":
  row 2 seen? NO
  col 2 seen? NO
  box (0,0) seen? "1" already in squares[(0,0)]!
  → return False ❌ (duplicate "1" in top-left box)
```

---

## Solution (Hash Set — One Pass) ⭐

```python
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = defaultdict(set)                # rows[r] = set of digits in row r
        cols = defaultdict(set)                # cols[c] = set of digits in col c
        squares = defaultdict(set)             # squares[(r//3, c//3)] = set of digits in that box

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":         # skip empty cells
                    continue

                val = board[r][c]

                if (val in rows[r] or           # duplicate in row?
                    val in cols[c] or            # duplicate in column?
                    val in squares[(r // 3, c // 3)]):  # duplicate in box?
                    return False

                rows[r].add(val)               # record in all three notebooks
                cols[c].add(val)
                squares[(r // 3, c // 3)].add(val)

        return True
```

**Why this is the best interview answer:**
- One pass through the board — visit each cell exactly once
- Three `defaultdict(set)` — clean, readable, no manual initialization
- The `(r // 3, c // 3)` tuple trick for box identification is elegant and easy to explain

---

## How `defaultdict(set)` Works

If you haven't seen this before:

```python
from collections import defaultdict
d = defaultdict(set)

d[0].add("5")    # automatically creates an empty set for key 0, then adds "5"
d[0].add("3")    # adds "3" to the existing set
"5" in d[0]      # True — O(1) lookup
```

It's just a dictionary where every new key automatically starts with an empty set. Saves you from writing `if key not in d: d[key] = set()` everywhere.

---

## Alternative: Brute Force (Three Separate Checks)

```python
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Check rows
        for row in range(9):
            seen = set()
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])

        # Check columns
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])

        # Check 3x3 boxes
        for box in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    r = (box // 3) * 3 + i
                    c = (box % 3) * 3 + j
                    if board[r][c] == ".":
                        continue
                    if board[r][c] in seen:
                        return False
                    seen.add(board[r][c])

        return True
```

| Pros | Cons |
|---|---|
| Very explicit — easy to see what's being checked | Three separate loops, more code |
| Good for understanding the problem | Visits each cell 3 times instead of once |
| Easier to debug | Same O(n²) time but more verbose |

Same time complexity, but the one-pass version is cleaner for interviews.

---

## Both Compared

| Approach | Time | Space | Notes |
|---|---|---|---|
| Three separate checks | O(n²) | O(n) | Clear but verbose |
| **One-pass hash set** | **O(n²)** | **O(n²)** | **Clean, one loop, use this in interviews** |

Where n = 9 (board size). Both are effectively O(81) = O(1) since the board is always 9×9, but we express it as O(n²) for the general case.

---

## Gotchas & Edge Cases

- **Skip "." cells** — forgetting this is the #1 bug. Empty cells are not digits.
- **Box index formula** — `(r // 3, c // 3)` not `(r / 3, c / 3)`. Must be integer division.
- **Validity ≠ solvability** — a board with no duplicates is valid even if it's impossible to complete.
- **Strings not ints** — the board contains `"1"` not `1`. Compare strings to strings.
- **Board is always 9×9** — no need to handle variable sizes.

---

## Pattern Recognition

This problem teaches **multi-dimensional duplicate detection** — checking for duplicates across multiple groupings simultaneously.

You'll see similar ideas in:
- N-Queens (check rows, columns, and diagonals)
- Word Search (tracking visited cells in a grid)
- Contains Duplicate (same concept, simpler — 1D instead of 2D)

Whenever you see "check for duplicates across rows/columns/regions" → think **hash set per group**.
