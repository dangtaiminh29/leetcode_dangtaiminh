#
# @lc app=leetcode id=2099 lang=python3
#
# [2099] Find Subsequence of Length K With the Largest Sum
#

# @lc code=start
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
       while len(nums) > k:
        nums.remove(min(nums))
       return nums
# @lc code=end

