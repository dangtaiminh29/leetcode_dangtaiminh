#
# @lc app=leetcode id=1909 lang=python3
#
# [1909] Remove One Element to Make the Array Strictly Increasing
#

# @lc code=start
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
           temp = nums[:i]+nums[i+1:]
           if temp == sorted(set(temp)):
               return True
        return False
           
# @lc code=end

