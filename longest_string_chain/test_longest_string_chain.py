from longest_string_chain import get_longest_string_chain


def test_get_longest_string_chain_example_1():
    assert get_longest_string_chain(["a", "b", "ba", "bca", "bda", "bdca"]) == 4


def test_get_longest_string_chain_example_2():
    assert get_longest_string_chain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]) == 5


def test_get_longest_string_chain_example_3():
    assert get_longest_string_chain(["abcd", "dbqca"]) == 1
