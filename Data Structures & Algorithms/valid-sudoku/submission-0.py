class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        colms = collections.defaultdict(set)
        sq = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                elif (board[r][c] in rows[r] or
                    board[r][c] in colms[c] or
                    board[r][c] in sq[(r//3,c//3)]):
                    return False
                else:
                    rows[r].add(board[r][c])
                    colms[c].add(board[r][c])
                    sq[(r//3,c//3)].add(board[r][c])
        return True
        