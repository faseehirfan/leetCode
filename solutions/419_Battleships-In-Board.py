class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        n, m = len(board), len(board[0])
        res = 0

        for r in range(n):
            for c in range(m):
                if board[r][c] != 'X':
                    continue
                if r > 0 and board[r-1][c] == 'X':
                    continue
                if c > 0 and board[r][c-1] == 'X':
                    continue

                res += 1

        return res

    ### BFS solution
    # def countBattleships(self, board: List[List[str]]) -> int:
    #     n, m = len(board), len(board[0])
    #     seen = set()
    #     res = 0

    #     def bfs(r, c):
    #         q = deque([(r,c)])
    #         while q:
    #             r, c = q.popleft()
                
    #             for dr, dc in [[1,0], [0,1]]:
    #                 nr, nc = r + dr, c + dc
    #                 if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 'X' and (nr, nc) not in seen:
    #                     seen.add((nr, nc))
    #                     q.append((nr, nc))

            
    #     for i in range(n):
    #         for j in range(m):
    #             if board[i][j] == 'X' and (i,j) not in seen:
    #                 seen.add((i,j))
    #                 bfs(i, j)
    #                 res += 1

    #     return res

        