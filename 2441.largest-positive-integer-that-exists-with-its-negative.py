#
# @lc app=leetcode id=2441 lang=python3
#
# [2441] Largest Positive Integer That Exists With Its Negative
#

# @lc code=start
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        r = len(nums)-1
        l = 0
        while l<r:
            if -nums[l]<nums[r]:
                r = r-1
            elif -nums[l]>nums[r]:
                l = l+1
            else:
                return nums[r]
        return -1
# @lc code=end

