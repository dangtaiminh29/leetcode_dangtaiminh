#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list1=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums2[j] == nums1[i]:
                    list1.append(nums1[i])
        list1 = list(set(list1))
        return list1
               
                
                    

# @lc code=end

