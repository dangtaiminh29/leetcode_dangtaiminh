#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[x] = nums[i]
                x += 1
        return x 
# @lc code=end

