from asteroid_collision import get_asteroid_collision


def test_get_asteroid_collision_example_1():
    assert get_asteroid_collision([5, 10, -5]) == [5, 10]


def test_get_asteroid_collision_example_2():
    assert get_asteroid_collision([8, -8]) == []


def test_get_asteroid_collision_example_3():
    assert get_asteroid_collision([10, 2, -5]) == [10]


def test_get_asteroid_collision_example_4():
    assert get_asteroid_collision([-2, -1, 1, 2]) == [-2, -1, 1, 2]
