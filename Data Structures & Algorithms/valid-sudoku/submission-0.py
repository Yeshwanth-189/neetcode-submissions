class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row wise check
        rows=9
        cols=9
        for i in range(0,9):
            seen=[]
            for j in range(0,9):
                if board[i][j]==".":
                    continue
                elif board[i][j].isalnum():
                    if board[i][j] not in seen:
                        seen.append(board[i][j])
                    else:
                        return False
                    
        #col wise check
        for i in range(0,9):
            seen=[]
            for j in range(0,9):
                if board[j][i]==".":
                    continue
                elif board[j][i].isalnum():
                    if board[j][i] not in seen:
                        seen.append(board[j][i])
                    else:
                        return False

        #3x3 check
        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                seen = []

                for i in range(row_start, row_start + 3):
                    for j in range(col_start, col_start + 3):
                        if board[i][j] == ".":
                            continue

                        if board[i][j] in seen:
                            return False

                        seen.append(board[i][j])

        return True



        