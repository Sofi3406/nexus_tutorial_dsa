class Solution(object):
    def romanToInt(self, s):
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        
        for i in range(len(s)):
            total += roman_map[s[i]]
            if i > 0 and roman_map[s[i]] > roman_map[s[i - 1]]:
                total -= 2 * roman_map[s[i - 1]]  
        
        return total

