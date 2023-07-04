#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num= sorted(nums)
        a = 1
        if num[-1]<0:
            return a
        for i in num:
            if i == a:
                a += 1
        return a
# @lc code=end

