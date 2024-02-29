#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box = [set() for x in range(0,9)]
        row = [set() for x in range(0,9)]
        col = [set() for x in range(0,9)]
        for i in range(0, 9):
            for j in range(0, 9):
                value = board[i][j]
                if value == ".":
                    continue
                if value in row[i]:
                    return False
                else:
                    row[i].add(value)
                if value in col[j]:
                    return False
                else:
                    col[j].add(value)
                k = ((i//3) * 3) + (j//3)
                if value in box[k]:
                    return False
                else:
                    box[k].add(value)
        return True
        
# @lc code=end

