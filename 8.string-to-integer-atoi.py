#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        s = s.strip()
        pos = True
        if s and s[0] == '-':
            pos = False
            s = s[1:]
        elif s and s[0] == '+':
            s = s[1:]
        i = 0
        while i < len(s) and s[i] == '0':
            i += 1
        res = None
        while i < len(s) and s[i] in '0123456789':
            if res is None:
                res = int(s[i])
            else:
                res = (res * 10) + int(s[i])
            i += 1
        res = 0 if res is None else res
        res = res if pos else -res
        res = max(res, -2**31)
        res = min(res, (2**31)-1)
        return res
# @lc code=end

