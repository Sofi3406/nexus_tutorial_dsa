class Solution:
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        intersection = set1.intersection(set2)
        return list(intersection)
  
# Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/