#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from collections import deque
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        que = deque(
            [
                ('(', 1, 0)
            ]
        )
        while len(que) > 0:
            string, opening_count, closing_count = que.popleft()
            if (opening_count + closing_count) == n*2:
                output.append(string)
                continue
            if opening_count+1 <= n:
                que.append((string+'(',opening_count+1, closing_count))
            if opening_count >= closing_count+1:
                que.append((string+')',opening_count, closing_count+1))
        return output
# @lc code=end

