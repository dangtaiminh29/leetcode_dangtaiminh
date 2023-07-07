#
# @lc app=leetcode id=1122 lang=python3
#
# [1122] Relative Sort Array
#

# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr12 = []
        arr = []
        arr1 = Counter(arr1)
        for i in arr2 :
          arr12 += [i]* arr1[i]
        for i in arr1 :
            if i not in arr2:
                arr+=[i]*arr1[i]
        return arr12+sorted(arr)
# @lc code=end

