from time_based_key_value_store import TimeMap


def test_time_based_key_value_store():
    FOO = "foo"
    BAR = "bar"

    time_map = TimeMap()

    time_map.set(FOO, BAR, 1)

    assert time_map.get(FOO, 1) == BAR
    assert time_map.get(FOO, 3) == BAR

    time_map.set(FOO, f"{BAR}2", 4)

    assert time_map.get(FOO, 4) == f"{BAR}2"
    assert time_map.get(FOO, 5) == f"{BAR}2"
