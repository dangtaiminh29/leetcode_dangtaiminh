#
# @lc app=leetcode id=1346 lang=python3
#
# [1346] Check If N and Its Double Exist
#

# @lc code=start
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)):
            product = arr[i]*2
            l = 0
            r = len(arr)-1
            while l<=r:
                mid = (l+r)//2
                if arr[mid]==product and mid!= i:
                    return True
                elif arr[mid]<product:
                    l+=1
                else:
                    r-=1
        return False
# @lc code=end

