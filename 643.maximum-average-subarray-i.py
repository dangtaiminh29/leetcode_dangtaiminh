#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum1 = 0
        for i in range(k):
           sum1 += nums[i]
        
        newSum = sum1
        i = k
        j = 0
        while i < len(nums):
            sum1 -= nums[j]
            sum1 += nums[i]
            newSum = max(newSum, sum1)
            i += 1
            j += 1
        return newSum/k   
# @lc code=end

