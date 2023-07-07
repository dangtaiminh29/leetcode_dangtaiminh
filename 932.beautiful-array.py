#
# @lc app=leetcode id=932 lang=python3
#
# [932] Beautiful Array
#

# @lc code=start
class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        res=[1]
        while len(res)<n :
            odd=[2*i-1 for i in res]
            even=[2*i for i in res]
            res=odd+even
        return [i for i in res if i<=n]
# @lc code=end

