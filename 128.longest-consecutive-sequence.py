#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        nums = set(nums)
        max_count = 0

        for value in nums:
            if value in seen: continue
            count = 0
            while value in nums:
                value += 1
                count += 1
                seen.add(value)
            
            max_count = max(max_count, count)

        return max_count
        
# @lc code=end

