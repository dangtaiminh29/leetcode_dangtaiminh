#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {}
        for i in arr:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        # Kiểm tra xem số lần xuất hiện có duy nhất hay không
        result = set(counts.values())
        return len(result) == len(counts)
    
# @lc code=end

