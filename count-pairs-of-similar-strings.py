class Solution(object):
    def similarPairs(self, words):
        
        unique_chars = []
        
        
        for word in words:
            unique_chars.append(frozenset(word)) 
        
        count = 0
        
      
        for i in range(len(unique_chars)):
            for j in range(i + 1, len(unique_chars)):
                if unique_chars[i] == unique_chars[j]: 
                    count += 1
        
        return count