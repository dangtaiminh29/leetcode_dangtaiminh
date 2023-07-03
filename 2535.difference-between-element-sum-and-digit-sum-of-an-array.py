#
# @lc app=leetcode id=2535 lang=python3
#
# [2535] Difference Between Element Sum and Digit Sum of an Array
#

# @lc code=start
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        x = sum(nums)
        y = 0
        for i in nums:
            for j in str(i):
                y += int(j)
        return abs(x-y)
# @lc code=end

