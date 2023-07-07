#
# @lc app=leetcode id=989 lang=python3
#
# [989] Add to Array-Form of Integer
#

# @lc code=start
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = 0
        for i in num:
            n = n*10+i
        n = n+k
        num1=[]
        while n !=0 :
            num1.append(n%10)
            n  //= 10
        return num1[::-1]

        
# @lc code=end

