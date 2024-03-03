#
# @lc app=leetcode id=1899 lang=python3
#
# [1899] Merge Triplets to Form Target Triplet
#

# @lc code=start
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # loop trough the triplets to find any triplet that matches to one of the num in the target
        cur = [0] * 3
        for triplet in triplets:
            if cur == target:
                return True
            if (triplet[0] > target[0] or
                triplet[1] > target[1] or
                triplet[2] > target[2]):
                continue
            cur = [max(triplet[0], cur[0]), max(triplet[1], cur[1]), max(triplet[2], cur[2])]
        return True if cur == target else False
# @lc code=end

