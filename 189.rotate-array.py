#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
        for i in range(k%len(nums)):
            x=nums.pop(-1)
            nums.insert(0,x)
            
# @lc code=end

