class Solution(object):
    def commonFactors(self, a, b):
        smaller = min(a, b)
        count = 0
        for i in range(1, smaller + 1):
            if a % i == 0 and b % i == 0:
                count += 1
        
        return count

# Number of Common Factors
# https://leetcode.com/problems/number-of-common-factors/