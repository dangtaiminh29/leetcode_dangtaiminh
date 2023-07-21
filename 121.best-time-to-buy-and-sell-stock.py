#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit =0
        buy = prices[0]
        for i in prices[1:]:
            buy = min(buy, i)
            profit = max(profit, i - buy)
        return profit
        
# @lc code=end

