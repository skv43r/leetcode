# Given the array nums consisting of 2n elements in the form
# [x1,x2,...,xn,y1,y2,...,yn].

# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

# Example 1:
# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7] 

# Example 2:
# Input: nums = [1,2,3,4,4,3,2,1], n = 4
# Output: [1,4,2,3,3,2,4,1]

# Example 3:
# Input: nums = [1,1,2,2], n = 2
# Output: [1,2,1,2]
from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums2 = []

        for i in range(int(len(nums) / 2)):
            nums2.append(nums[i])
            nums2.append(nums[i + n])
        return nums2
    
print(Solution().shuffle([1,2,3,4,4,3,2,1], 4))