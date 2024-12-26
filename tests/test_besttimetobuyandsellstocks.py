import pytest
from BestTimeToBuyAndSellStock import Solution

@pytest.mark.parametrize("prices, res",[([7,1,5,3,6,4], 5), ([7,6,4,3,1], 0)])
def test_BestTimeToBuyAndSellStock(prices, res):
    solution = Solution()
    assert solution.maxProfit(prices) == res