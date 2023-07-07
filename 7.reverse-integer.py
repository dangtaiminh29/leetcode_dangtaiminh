#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = -1 if x < 0 else 1
        x *= sign
        while x>0:
            res = res * 10 + x % 10
            x //=10
        if sign * res < -2**31 or sign * res > 2**31 - 1:
            return 0       
        return res * sign
# @lc code=end

