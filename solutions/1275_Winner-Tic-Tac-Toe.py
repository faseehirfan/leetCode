class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows, cols = [0]*3, [0]*3
        d1 = d2 = 0
        player = 1
        for r, c in moves:
            rows[r] += player
            cols[c] += player
            if r == c: d1 += player
            if r + c == 2: d2 += player
            if abs(rows[r]) == 3 or abs(cols[c]) == 3 or abs(d2) == 3 or abs(d1) == 3:
                if player == 1:
                    return 'A'
                else:
                    return 'B'
            player = -player
        
        if len(moves) == 9:
            return "Draw"
        else: 
            return "Pending"
        


