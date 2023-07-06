#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        x = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
                x = max(x, count)
            else:
                count = 0
        return x
       
# @lc code=end

