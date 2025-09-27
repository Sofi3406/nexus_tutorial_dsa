class Solution:
    def isCovered(self, ranges, left, right):
        covered = set()
        for start, end in ranges:
            covered |= set(range(start, end + 1))
        return all(num in covered for num in range(left, right + 1))
