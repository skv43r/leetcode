import pytest
from RichestCustomerWealth import Solution

@pytest.mark.parametrize("accounts, res", [([[1,2,3],[3,2,1]], 6),
                                           ([[1,5],[7,3],[3,5]], 10),
                                           ([[2,8,7],[7,1,3],[1,9,5]], 17)])
def test_maximumWealth_good(accounts, res):
    solution = Solution()
    assert solution.maximumWealth(accounts) == res

@pytest.mark.parametrize("excepted_exception, accounts", [(TypeError, "[1,2,3],[3,2,1]")])
def test_maximumWealth_with_error(excepted_exception, accounts):
    with pytest.raises(excepted_exception):
        solution = Solution()
        assert solution.maximumWealth(accounts)
