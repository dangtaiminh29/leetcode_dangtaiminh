#
# @lc app=leetcode id=1089 lang=python3
#
# [1089] Duplicate Zeros
#

# @lc code=start
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        l = len(arr)
        i = 0
        while i < l:
            if arr[i] == 0:
                arr.insert(i+1, 0)
                arr.pop()
                i +=1
            i +=1
        
# @lc code=end

