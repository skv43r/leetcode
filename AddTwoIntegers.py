# Given two integers num1 and num2, return the sum of the two integers.
 

# Example 1:

# Input: num1 = 12, num2 = 5
# Output: 17
# Explanation: num1 is 12, num2 is 5, and their sum is 12 + 5 = 17,
# so 17 is returned.

class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2

print(Solution().sum(12, 5))