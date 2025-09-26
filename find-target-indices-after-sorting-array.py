class Solution:
    def targetIndices(self, nums, target):
        nums.sort()
        indices = []
        for index, num in enumerate(nums):
            if num == target:
                indices.append(index)
        return indices
# Find Target Indices After Sorting Array
# https://leetcode.com/problems/find-target-indices-after-sorting-array/