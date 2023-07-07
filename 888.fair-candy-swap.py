#
# @lc app=leetcode id=888 lang=python3
#
# [888] Fair Candy Swap
#

# @lc code=start
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        Sa, Sb = sum(aliceSizes),sum(bobSizes)
        setB  = set(bobSizes)
        for i in aliceSizes:
            if i + (Sb-Sa)//2 in setB:
                return [i,i+(Sb-Sa)//2]
# @lc code=end

