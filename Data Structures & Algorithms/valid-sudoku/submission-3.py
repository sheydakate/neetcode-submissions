class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols = collections.defaultdict(set)     #hashmap - tracks 1-9 in cols
        rows = collections.defaultdict(set)     #hashmap - tracks 1-9 in rows
        squares = collections.defaultdict(set)  #hashmap - tracks 1-9 in squares

        for r in range(9):          #go thru every row
            for c in range(9):      #and every column
                
                if board[r][c] == ".":  #skip empty squares
                    continue
                
                if (board[r][c] in rows[r] or #if duplicare in row, or col, or 3x3 squares
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3 , c//3)]):
                    
                    return False              #invalid Sudoku
                
                rows[r].add(board[r][c])      #if not duplicate, add it to row, col and 3x3 square
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        
        return True

