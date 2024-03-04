#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
"""
1. Sliding Window with Sorting
    - Sort
    - Calculate maximum number of k elements

2. HashMap
    - Make a counter with key as number and value as count
    - Return k number of count

"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        return [val for val, _ in cnt.most_common(k)]
        
# @lc code=end

