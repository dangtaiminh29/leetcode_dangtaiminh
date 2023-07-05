#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        listK = {}
        for i in range(len(nums)):
            if nums[i] in listK and abs(i - listK[nums[i]]) <= k:
                return True
            listK[nums[i]] = i
        return False   
# @lc code=end

