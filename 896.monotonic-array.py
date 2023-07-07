#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#

# @lc code=start
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        k = 0
        for i in range(len(nums)-1):
            if k == 0:
                if nums[i]<nums[i+1]: k = 1
                elif nums[i]>nums[i+1]: k = -1
            elif k == 1:
                if nums[i]>nums[i+1]:
                    return False
            elif k == -1: 
                if  nums[i]<nums[i+1]:
                    return False
        return True 
# @lc code=end

