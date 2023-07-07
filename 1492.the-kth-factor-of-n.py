#
# @lc app=leetcode id=1492 lang=python3
#
# [1492] The kth Factor of n
#

# @lc code=start
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        uoc = []
        for i in range(1, n+1):
            if n % i == 0: 
                uoc.append(i)
                if len(uoc)>=k :
                    return uoc[k-1] 
        return -1
            
                
# @lc code=end

