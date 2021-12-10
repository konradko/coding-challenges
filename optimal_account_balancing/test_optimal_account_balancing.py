from optimal_account_balancing import get_optimal_account_balancing


def test_get_optimal_account_balancing_example_1():
    assert get_optimal_account_balancing([[0, 1, 10], [2, 0, 5]]) == 2


def test_get_optimal_account_balancing_example_2():
    assert get_optimal_account_balancing([[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]) == 1
