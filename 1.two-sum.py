# @before-stub-for-debug-begin
from python3problem1 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, integer in enumerate(nums):
            current = target - integer
            if current in map:
                return [map.get(current), index]
            map[integer] = index
        return []


# @lc code=end

