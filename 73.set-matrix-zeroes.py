#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def __init__(self):
        self.que = deque(())
    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for i in range(0, len(matrix)):
            for j in range(0,len(matrix[i])):
                if matrix[i][j] == 0:
                    self.que.append((i,j,0))

        while len(self.que) > 0:
            i, j, direction = self.que.popleft()
            matrix[i][j] = 0
            if direction == 0:
                self.goUp(i,j,matrix)
                self.goRight(i,j,matrix)
                self.goDown(i,j,matrix)
                self.goLeft(i,j,matrix)
            elif direction == 1:
                self.goUp(i,j,matrix)
            elif direction == 2:
                self.goRight(i,j,matrix)
            elif direction == 3:
                self.goDown(i,j,matrix)
            elif direction == 4:
                self.goLeft(i,j,matrix)

    def goUp(self, i, j, matrix):
        # i-1, j
        if i > 0:
            self.que.append((i-1, j, 1))
    def goRight(self, i, j, matrix):
        # i, j+1
        if j + 1 < len(matrix[i]) :
            self.que.append((i, j+1, 2))
    def goDown(self, i, j, matrix):
        # i+1, j
        if i + 1 < len(matrix):
            self.que.append((i+1, j, 3))
    def goLeft(self, i, j, matrix):
        # i, j-1
        if j > 0:
            self.que.append((i, j-1, 4))
        
# @lc code=end

