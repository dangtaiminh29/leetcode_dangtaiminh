#
# @lc app=leetcode id=2161 lang=python3
#
# [2161] Partition Array According to Given Pivot
#

# @lc code=start
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        list1 = []
        list2 = []
        list3 = []
        for i in range(len(nums)):
            if nums[i] < pivot:
                list1.append(nums[i])
            elif nums[i] == pivot :
                list2.append(nums[i])
            else  :
                list3.append(nums[i])
        return list1 +list2+list3

# @lc code=end

