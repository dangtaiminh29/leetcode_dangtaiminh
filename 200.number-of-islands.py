#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Count = 0 
        m = len(grid)
        n = len(grid[0])
        def dfs(i, j): 
            grid[i][j] = -1
            if i < m - 1 and grid[i + 1][j] == "1": 
                dfs(i + 1, j)
            if i > 0 and grid[i - 1][j] == "1": 
                dfs(i - 1, j)
            if j < n - 1 and grid[i][j + 1] == "1": 
                dfs(i, j + 1)
            if j > 0 and grid[i][j - 1] == "1": 
                dfs(i, j - 1)
        
        for k in range(m): 
            for l in range(n): 
                if grid[k][l] == "1": 
                    Count += 1
                    dfs(k, l)
        return Count
# @lc code=end

