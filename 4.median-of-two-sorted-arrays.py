#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = (nums1 + nums2)
        nums.sort()
        x = len(nums)
        if x % 2 == 0:
            return (nums[(x//2)-1] +nums[(x//2)]) / 2
        else:
            return nums[x//2]
# @lc code=end

