
def is_valid(board, row, col, num):
    for c in range(9):
        if board[row][c] == num:
            return False
    for r in range(9):
        if board[r][col] == num:
            return False
    box_row_start = (row //3) * 3
    box_col_start = (col//3) * 3
    for r in range(box_row_start, box_row_start +3):
        for c in range(box_col_start, box_col_start +3):
            if board[r][c] == num:
                return False
    
    return True

def backtrack(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == '.':
                for num in '123456789':
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if backtrack(board):
                            return True
                        board[row][col] = '.'
                return False
    return True


board =    [["6",".",".",".",".",".","8",".","3"],
   [".","4",".","7",".",".",".",".","."],
   [".",".",".",".",".",".",".",".","."],
   [".",".",".","5",".","4",".","7","."],
   ["3",".",".","2",".",".",".",".","."],
   ["1",".","6",".",".",".",".",".","."],
   [".","2",".",".",".",".",".","5","."],
   [".",".",".",".","8",".","6",".","."],
   [".",".",".",".","1",".",".",".","."]]

backtrack(board)
print(board)    
