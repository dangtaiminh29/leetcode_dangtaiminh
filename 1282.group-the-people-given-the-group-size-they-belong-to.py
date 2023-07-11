#
# @lc app=leetcode id=1282 lang=python3
#
# [1282] Group the People Given the Group Size They Belong To
#

# @lc code=start
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        progress = {}
        finished = []
        
        for i, size in enumerate(groupSizes):
            progress[size] = progress.get(size, []) + [i]
            if len(progress[size]) == size:
                finished += [progress.pop(size)]
        
        return finished
# @lc code=end

