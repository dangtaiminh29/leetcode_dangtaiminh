#
# @lc app=leetcode id=908 lang=python3
#
# [908] Smallest Range I
#

# @lc code=start
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        a= max(nums)-min(nums)-2*k 
        if a > 0:
            return a
        else:
            return 0
# @lc code=end

