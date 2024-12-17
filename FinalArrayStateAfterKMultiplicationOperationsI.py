# You are given an integer array nums, an integer k, and an integer multiplier.

# You need to perform k operations on nums. In each operation:

# Find the minimum value x in nums. If there are multiple occurrences of the
# minimum value, select the one that appears first.
# Replace the selected minimum value x with x * multiplier.
# Return an integer array denoting the final state of nums after performing all
# k operations.

# Example 1:
# Input: nums = [2,1,3,5,6], k = 5, multiplier = 2
# Output: [8,4,6,5,6]
from typing import List

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k != 0:
            x = min(nums)
            for i in range(len(nums)):
                if nums[i] == x:
                    nums[i] = nums[i] * multiplier
                    k -= 1
                    break
        return nums

s = Solution()
print(s.getFinalState(nums = [2,1,3,5,6], k = 5, multiplier = 2))