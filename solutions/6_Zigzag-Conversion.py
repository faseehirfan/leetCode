class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = ["" for _ in range(numRows)]
        row, direction = 0, 1

        for c in s:
            rows[row] += c

            if row == 0:
                direction = 1

            elif row == numRows - 1:
                direction = -1

            row += direction

        return "".join(rows)
