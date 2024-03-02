#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
"""

"""
Intuition
SC : O(1)

TC : O(n^2)
1. Brute Force:
    - Do this for All values O(n)
        - Check if similar value exist in current iteration O(n)

TC : O(nlogn) + O(n) => O(2n log n) => o(nlogn)
2. Sorting with Sliding window
    - Sort 
    - sliding window to check i, i+1 
        - if similar return num
        - else + 1
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n == 1:
            return nums

        i = 0
        while i + 1 < n:
            if nums[i] == nums[i+1]:
                return nums[i]
            i += 1

"""
Dry Run
[1,3,4,2,2]

slow 0  1   2   4
fast 0  3   4   4

slow2 = 0   1   3   2
slow    4   2   4   4

[3,1,3,4,2]
slow    4   3   4   2   3   4
slow2   0   4   2   3   4   2

 0  1. 2. 3. 4. 5  6
[2, 3, 1, 3, 4, 5, 6]
"""
        
# @lc code=end

