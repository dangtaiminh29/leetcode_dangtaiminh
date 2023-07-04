#
# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#

# @lc code=start
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        m = 0
        for i in range(1,len(nums)): 
            m = max(m,nums[i]-nums[i-1])
        return m
# @lc code=end

