class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        time = -1
        q = deque()
        visited = set()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
  

        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in [[1,0], [-1,0], [0,1], [0,-1]]:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in visited):
                        visited.add((nr,nc))
                        q.append((nr,nc))
                        fresh -= 1
            time += 1

        if fresh > 0:
            return -1
        return max(time, 0)
