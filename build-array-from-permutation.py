class Solution:
    def buildArray(self, nums):
        return [nums[nums[i]] for i in range(len(nums))]
solution = Solution()
nums1 = [0, 2, 1, 5, 3, 4]
output1 = solution.buildArray(nums1)
print(output1)  

nums2 = [5, 0, 1, 2, 3, 4]
output2 = solution.buildArray(nums2)
print(output2)
