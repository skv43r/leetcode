# Given a positive integer n, return the smallest positive integer that is
# a multiple of both 2 and n.

# Example 1:
# Input: n = 5
# Output: 10
# Explanation: The smallest multiple of both 5 and 2 is 10.

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        else:
            return n * 2
        
print(Solution().smallestEvenMultiple(5))