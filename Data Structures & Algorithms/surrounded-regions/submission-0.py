class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board),len(board[0])
        def capture(r,c):
            if r<0 or c<0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            board[r][c] = "#"
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)
        for r in range(ROWS):
            if board[r][0] == "O":
                capture(r,0)
            if board[r][COLS-1] == "O":
                capture(r,COLS-1)
            
        for c in range(COLS):
            if board[0][c] == "O":
                capture(0,c)
            if board[ROWS-1][c] == "O":
                capture(ROWS-1,c)
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == '#':
                    board[i][j] = "O"
        