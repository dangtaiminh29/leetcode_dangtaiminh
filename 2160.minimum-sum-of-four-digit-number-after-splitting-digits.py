#
# @lc app=leetcode id=2160 lang=python3
#
# [2160] Minimum Sum of Four Digit Number After Splitting Digits
#

# @lc code=start
class Solution:
    def minimumSum(self, num: int) -> int:
        l = sorted(str(num))
        return int(l[0]+l[2])+int(l[1]+l[3])
# @lc code=end

