class Solution:
    def missingNumber(self, nums):
       count = len(nums)
       for i in range(len(nums)):
           count += (i - nums[i])
       return count
        
        