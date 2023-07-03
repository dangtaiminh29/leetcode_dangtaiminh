#
# @lc app=leetcode id=2733 lang=python3
#
# [2733] Neither Minimum nor Maximum
#

# @lc code=start
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] != min(nums) and nums[i] != max(nums):
                return nums[i]
        return -1
       
        
# @lc code=end

