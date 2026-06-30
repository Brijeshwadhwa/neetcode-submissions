class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range (9)]

        for row in range(9):
            for col in range (9):
                value = board[row][col]
                if value == ".":
                    continue
                
                row_key = f"{value} in row {row}"
                col_key = f"{value} in col {col}"
                box_key = f"{value} in box {(row//3) * 3 + (col // 3)}"

                if row_key in seen or col_key in seen or box_key in seen:
                    return False

                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)
        return True