import pytest
from ContainsDuplicate2 import Solution

@pytest.mark.parametrize("nums, k, res", [([1,2,3,1], 3, True),
                                          ([1,2,1,3,4], 2, True),
                                          ([1,1,1,1], 3, True),
                                          ([1,0,1,1], 1, True),
                                          ([1,2,3,1,2,3], 2, False)])
def test_solution(nums, k, res):
    solution = Solution()
    assert solution.containsNearbyDuplicate(nums, k) == res