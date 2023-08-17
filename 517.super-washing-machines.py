#
# @lc app=leetcode id=517 lang=python3
#
# [517] Super Washing Machines
#

# @lc code=start
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        target = sum(machines)
        if target % len(machines) != 0:
            return -1
        target //= len(machines)
        
        running_sum = 0
        ans = 0
        for m in machines:
            running_sum += m - target
            ans = max(ans, abs(running_sum), m-target)
        
        return ans
# @lc code=end

