# Given an integer number n,return the difference between the product
# of its digits and the sum of its digits.

# Example 1:
# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        if n != 0:
            str_n = str(n)
            num = [int(el) for el in str_n]
            sum_n = sum(num)
            product = 1
            for i in range(len(num)):
                product *= num[i]
            return product - sum_n
        else:
            return 0

print(Solution().subtractProductAndSum(234))