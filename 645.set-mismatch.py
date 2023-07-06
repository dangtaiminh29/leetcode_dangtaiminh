#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        Sum = n*(n+1)//2
        miss = Sum - sum(set(nums))
        a = -Sum + sum(nums)+miss
        return [a,miss]

# @lc code=end

