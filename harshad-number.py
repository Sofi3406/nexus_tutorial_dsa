class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x):
        d_sum = sum(int(d) for d in str(x))  
        if x % d_sum == 0:
            return d_sum
        else:
            return -1

        