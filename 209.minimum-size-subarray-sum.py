#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        s = 0
        l = 0
        n = len(nums)
        for r, val in enumerate(nums):
            s += val
            while s >= target:
                s -= nums[l]
                n = min(n, r-l+1)
                l += 1
        return n  
# @lc code=end

