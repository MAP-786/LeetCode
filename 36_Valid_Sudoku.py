#36. Valid Sudoku
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        double_array = []
        small_box= []
        #Check row
        for i in range(0, len(board)):
            for j in range(0, len(board)):
                if board[i][j] not in double_array: 
                    double_array.append(board[i][j])
                elif board[i][j] == ".":
                    pass
                else:
                    return False
            double_array.clear()
        #Check Column
        for i in range(0, len(board)):
            for j in range(0, len(board)):
                if board[j][i] not in double_array: 
                    double_array.append(board[j][i])
                elif board[j][i] == ".":
                    pass
                else:
                    return False
            double_array.clear()
        #Check Box
        for i in range(0, len(board)):
            for j in range(0, 2):
                for k in range(0, 2):
                    if board[j][k] not in double_array: 
                        double_array.append(board[j][k])
                    elif board[j][k] == ".":
                        pass
                    else:
                        return False
            double_array.clear()
        return True