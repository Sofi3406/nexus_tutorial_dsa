class Solution:
    def addBinary(self, a, b):
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            sum_value = carry
            if i >= 0:
                sum_value += int(a[i])
                i -= 1
            if j >= 0:
                sum_value += int(b[j])
                j -= 1
            
            carry = sum_value // 2
            result.append(str(sum_value % 2))  

        return ''.join(result[::-1])