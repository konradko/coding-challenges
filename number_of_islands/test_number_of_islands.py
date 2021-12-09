from number_of_islands import NumberOfIslands


def test_number_of_islands_example_1():
    assert (
        NumberOfIslands(
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        ).get_number_of_islands()
        == 1
    )


def test_number_of_islands_example_2():
    assert (
        NumberOfIslands(
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        ).get_number_of_islands()
        == 3
    )
