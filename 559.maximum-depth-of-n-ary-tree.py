#
# @lc app=leetcode id=559 lang=python3
#
# [559] Maximum Depth of N-ary Tree
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        maxdepth=0
        for child in root.children:
            maxdepth=max(self.maxDepth(child),maxdepth)
        return maxdepth+1
        
# @lc code=end

