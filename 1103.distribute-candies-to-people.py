#
# @lc app=leetcode id=1103 lang=python3
#
# [1103] Distribute Candies to People
#

# @lc code=start
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        out = [0]*num_people
        i = 0
        j = 1
        while candies:
            if i == len(out):
                i = 0

            if candies >= j:
                out[i] += j
                candies -= j
                j += 1

            else:
                out[i] += candies
                break

            i += 1
        return out
# @lc code=end

