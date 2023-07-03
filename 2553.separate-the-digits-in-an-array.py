#
# @lc app=leetcode id=2553 lang=python3
#
# [2553] Separate the Digits in an Array
#

# @lc code=start
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        x = []
        for i in nums:
            y = list(str(i))
            for j in y:
                x.append(int(j))
        return x
# @lc code=end

