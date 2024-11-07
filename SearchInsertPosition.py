# Given a sorted array of distinct integers and a target value,
# return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0] == target or (target not in nums and target < nums[0]):
            return 0
        if nums[-1] < target:
            return len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == target:
                return i
            if nums[i] > target and nums[i-1] < target:
                return i
            
print(Solution().searchInsert([-1,3,5,6], 0))