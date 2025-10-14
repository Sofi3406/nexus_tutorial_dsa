class Solution:
    def mostCommonWord(self, paragraph, banned):
        banned_set = set(banned)
        freq = {}
        word = ''
        for ch in paragraph.lower() + ' ':  
            if ch.isalpha():
                word += ch
            elif word:
                if word not in banned_set:
                    freq[word] = freq.get(word, 0) + 1
                word = ''
        return max(freq, key=freq.get)
