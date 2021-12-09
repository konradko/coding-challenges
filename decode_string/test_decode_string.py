from decode_string import get_decoded_string


def test_get_decoded_string_example_1():
    assert get_decoded_string("3[a]2[bc]") == "aaabcbc"


def test_get_decoded_string_example_2():
    assert get_decoded_string("3[a2[c]]") == "accaccacc"


def test_get_decoded_string_example_3():
    assert get_decoded_string("2[abc]3[cd]ef") == "abcabccdcdcdef"


def test_get_decoded_string_example_4():
    assert get_decoded_string("abc3[cd]xyz") == "abccdcdcdxyz"


def test_get_decoded_string_example_asdf():
    assert get_decoded_string("10[asdf]") == "asdfasdfasdfasdfasdfasdfasdfasdfasdfasdf"
