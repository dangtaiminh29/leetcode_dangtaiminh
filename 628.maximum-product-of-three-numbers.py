#
# @lc app=leetcode id=628 lang=python3
#
# [628] Maximum Product of Three Numbers
#

# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        lens = len(nums)
        nums.sort()
        for i in nums:
          a = nums[lens-1]*nums[lens-2]*nums[lens-3]
          b = nums[lens-1]*nums[0]*nums[1]
        return max(a,b)
# @lc code=end

