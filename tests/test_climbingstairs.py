import pytest
from ClimbingStairs import Solution

@pytest.mark.parametrize("n, res", [(0, 0), (1, 1), (6, 13)])
def test_climbing_stairs(n, res):
    solution = Solution()
    assert solution.climbStairs(n) == res