class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(len(board)):
            column = []
            row = []
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    if board[i][j] in row:
                        return False
                    else:
                        row.append(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] in column:
                        return False
                    else:
                        column.append(board[j][i])
        for i in range(0,len(board), 3):
            for j in range(0, len(board[0]), 3):
                grid = []
                for c in range(3):
                    for d in range(3):
                        if board[i + c][j + d] != '.':
                            if board[i + c][j + d] in grid:
                                return False
                            else:
                                grid.append(board[i + c][j + d])
        return True

sol = Solution()
print(sol.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))