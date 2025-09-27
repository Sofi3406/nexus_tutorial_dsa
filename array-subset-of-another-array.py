from collections import Counter

class Solution:
    def isSubset(self, a, b):
        count_a = Counter(a)
        count_b = Counter(b)
        
        for elem in count_b:
            if count_b[elem] > count_a.get(elem, 0):
                return False
        return True
