from minimum_number_of_refueling_stops import get_minimum_number_of_refueling_stops


def test_get_minimum_number_of_refueling_stops_example_1():
    assert get_minimum_number_of_refueling_stops(1, 1, []) == 0


def test_get_minimum_number_of_refueling_stops_example_2():
    assert get_minimum_number_of_refueling_stops(100, 1, [[10, 100]]) == -1


def test_get_minimum_number_of_refueling_stops_example_3():
    assert get_minimum_number_of_refueling_stops(100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]) == 2


def test_get_minimum_number_of_refueling_stops():
    assert get_minimum_number_of_refueling_stops(100, 50, [[25, 25], [50, 50]]) == 1
