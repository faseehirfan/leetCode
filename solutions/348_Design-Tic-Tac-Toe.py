
class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [['0'] * n for i in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player

        if self.is_winning_move(row, col, player):
            return player

        return 0

    # this function runs in O(n) time!!!
    def is_winning_move(self, row, col, player):
        directions = [(0,1), (1,0), (1,1), (1,-1)]

        for drow, dcol in directions:
            is_winner = True

            # figure out where to start scanning
            if (drow, dcol) == (0, 1):       # row → leftmost cell
                start_row, start_col = row, 0
            elif (drow, dcol) == (1, 0):     # col → topmost cell
                start_row, start_col = 0, col
            elif (drow, dcol) == (1, 1):     # main diagonal → top-left corner
                start_row, start_col = 0, 0
            else:                            # anti-diagonal → top-right corner
                start_row, start_col = 0, self.n - 1

            r, c = start_row, start_col
            while 0 <= r < self.n and 0 <= c < self.n:
                if self.board[r][c] != player:
                    is_winner = False
                    break

                r += drow
                c += dcol

            if is_winner:
                return True

        return False

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)


# OPTIMIZED CHECK O(1) TC for moves O(N^2 space)

class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.moves = defaultdict(int)

    def move(self, row: int, col: int, player: int) -> int:
        self.moves[('row', row, player)] += 1
        self.moves[('col', col, player)] += 1

        # main diagnonal check
        if row == col:
            self.moves[('diag', player)] += 1

        # anti diagnoal check
        if row + col == self.n - 1:
            self.moves[('antidiag', player)] += 1

        if self.is_winning_move(row, col, player):
            return player

        return 0

    def is_winning_move(self, row, col, player):
        return (
            self.moves[('row', row, player)] == self.n or
            self.moves[('col', col, player)] == self.n or
            self.moves[('diag', player)] == self.n or
            self.moves[('antidiag', player)] == self.n
        )

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)