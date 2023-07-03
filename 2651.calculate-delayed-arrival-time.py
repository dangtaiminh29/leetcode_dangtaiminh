#
# @lc app=leetcode id=2651 lang=python3
#
# [2651] Calculate Delayed Arrival Time
#

# @lc code=start
class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        x = arrivalTime
        y =delayedTime
        return (x+y)%24
# @lc code=end

