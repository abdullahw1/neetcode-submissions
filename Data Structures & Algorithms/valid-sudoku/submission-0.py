class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)                # rows[r] = set of digits in row r
        cols = defaultdict(set)                # cols[c] = set of digits in col c
        squares = defaultdict(set)             # squares[(r//3, c//3)] = digits in that box

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
