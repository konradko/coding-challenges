from logger_rate_limitter import LoggerRateLimitter


def test_get_asteroid_collision_example_1():
    logger = LoggerRateLimitter()

    output = []
    for timestamp, message in [(1, "foo"), (2, "bar"), (3, "foo"), (8, "bar"), (10, "foo"), (11, "foo")]:
        output.append(logger.should_print_message(timestamp, message))

    assert output == [True, True, False, False, False, True]


def test_get_asteroid_collision_2():
    logger = LoggerRateLimitter()

    output = []
    for timestamp, message in [
        [0, "A"],
        [0, "B"],
        [0, "C"],
        [0, "A"],
        [0, "B"],
        [0, "C"],
        [0, "A"],
        [0, "B"],
        [0, "C"],
        [0, "A"],
    ]:
        output.append(logger.should_print_message(timestamp, message))

    assert output == [True, True, True, False, False, False, False, False, False, False]
