#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(x+1):
            if i * i == x:
              return i 
            elif  i * i > x:
              return (i-1)
# @lc code=end

