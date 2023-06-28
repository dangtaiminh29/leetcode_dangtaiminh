#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0
        b = 1
        for i in range(n):
            c = a + b
            a = b
            b = c
        return b
        
# @lc code=end

