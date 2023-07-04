#
# @lc app=leetcode id=561 lang=python3
#
# [561] Array Partition
#

# @lc code=start
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum = 0
        for i in range(0, len(nums), 2):
            max_sum += nums[i] 
        return max_sum
# @lc code=end

