from split_array_largest_sum import get_split_array_largest_sum


def test_get_split_array_largest_sum_example_1():
    assert get_split_array_largest_sum([7, 2, 5, 10, 8], 2) == 18


def test_get_split_array_largest_sum_example_2():
    assert get_split_array_largest_sum([1, 2, 3, 4, 5], 2) == 9


def test_get_split_array_largest_sum_example_3():
    assert get_split_array_largest_sum([1, 4, 4], 3) == 4


def test_get_split_array_largest_sum_4():
    assert get_split_array_largest_sum([1, 2, 3], 2) == 3


def test_get_split_array_largest_sum_5():
    assert get_split_array_largest_sum([4, 5, 6, 7], 3) == 9
