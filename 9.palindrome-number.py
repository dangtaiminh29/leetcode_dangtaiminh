#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
           return False
        
        reversed_num = 0
        temp = x

        while temp != 0:
            y = temp % 10
            reversed_num = reversed_num * 10 + y 
            temp //= 10
        if reversed_num == x:
            return True  
        
# @lc code=end

 