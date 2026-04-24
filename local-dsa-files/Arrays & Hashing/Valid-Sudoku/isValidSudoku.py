from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
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

        # --- Alternative: Three separate checks (brute force) ---
        # for row in range(9):
        #     seen = set()
        #     for col in range(9):
        #         if board[row][col] != "." :
        #             if board[row][col] in seen: return False
        #             seen.add(board[row][col])
        # for col in range(9):
        #     seen = set()
        #     for row in range(9):
        #         if board[row][col] != ".":
        #             if board[row][col] in seen: return False
        #             seen.add(board[row][col])
        # for box in range(9):
        #     seen = set()
        #     for i in range(3):
        #         for j in range(3):
        #             r, c = (box // 3) * 3 + i, (box % 3) * 3 + j
        #             if board[r][c] != ".":
        #                 if board[r][c] in seen: return False
        #                 seen.add(board[r][c])
        # return True


if __name__ == "__main__":
    sol = Solution()

    valid_board = [
        ["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"],
    ]

    invalid_board = [
        ["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","1",".",".",".",".",".","3"],  # "1" duplicates in top-left box
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"],
    ]

    empty_board = [["." for _ in range(9)] for _ in range(9)]

    tests = [
        (valid_board,   True,  "valid board"),
        (invalid_board, False, "duplicate 1 in top-left box"),
        (empty_board,   True,  "all empty — still valid"),
    ]

    print("Valid Sudoku")
    print("Time: O(n²) | Space: O(n²)\n")

    for i, (board, expected, label) in enumerate(tests, 1):
        result = sol.isValidSudoku(board)
        status = "✅" if result == expected else "❌"
        print(f"  {status} Test {i}: {label} → {result}")
