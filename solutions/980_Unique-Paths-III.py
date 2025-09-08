class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        start = end = (-1, -1)
        res = 0
        visited = set()
        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] != -1:
                    count += 1
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)

        def backtrack(row, col, path_len):
            nonlocal res
            if (
                not (0 <= row < n and 0 <= col < m)
                or (row, col) in visited
                or grid[row][col] == -1
                ):
                return

            if (row, col) == end:
                if path_len == count:
                    res += 1
                return

            visited.add((row, col))

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                backtrack(row + dx, col + dy, path_len + 1)

            visited.remove((row, col))

        backtrack(*start, 1)
        return res
