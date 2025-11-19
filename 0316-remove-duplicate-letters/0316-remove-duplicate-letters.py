class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = [] 
        in_stack = [False] * 26 
        char_count = [0] * 26  
        for char in s:
            char_count[ord(char) - ord('a')] += 1
        for char in s:
            index = ord(char) - ord('a')
            char_count[index] -= 1
            if in_stack[index]:
                continue
            while stack and stack[-1] > char and char_count[ord(stack[-1]) - ord('a')] > 0:
                removed_char = stack.pop()
                in_stack[ord(removed_char) - ord('a')] = False
            stack.append(char)
            in_stack[index] = True
            
        return ''.join(stack)