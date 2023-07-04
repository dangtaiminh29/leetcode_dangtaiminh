#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0]*n for _ in range(m)]
        matrix[0][0] =1
        for i in range(m):
            for j in range(n):
                if i>0:
                    matrix[i][j] += matrix[i-1][j]
                if j>0:
                     matrix[i][j] += matrix[i][j-1]
        return matrix[-1][-1]
# @lc code=end

