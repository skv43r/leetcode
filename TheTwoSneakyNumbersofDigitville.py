# In the town of Digitville, there was a list of numbers called nums containing
# integers from 0 to n - 1. Each number was supposed to appear exactly once in
# the list, however, two mischievous numbers sneaked in an additional time,
# making the list longer than usual.

# As the town detective, your task is to find these two sneaky numbers.
# Return an array of size two containing the two numbers (in any order),
# so peace can return to Digitville.

# Example 1:
# Input: nums = [0,1,1,0]
# Output: [0,1]

from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        d = {}
        my_list = []
        for num in nums:
            d[num] = d.get(num, 0) + 1
            if d[num] == 2:
                my_list.append(num)
        return my_list
    
print(Solution().getSneakyNumbers([0,1,1,0]))