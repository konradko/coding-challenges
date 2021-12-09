from text_justification import TextJustification


def test_text_justification_example_1():
    assert TextJustification(max_width=16).get_justified_lines(
        words=["This", "is", "an", "example", "of", "text", "justification."]
    ) == ["This    is    an", "example  of text", "justification.  "]


def test_text_justification_example_2():
    assert TextJustification(max_width=16).get_justified_lines(
        words=["What", "must", "be", "acknowledgment", "shall", "be"]
    ) == ["What   must   be", "acknowledgment  ", "shall be        "]


def test_text_justification_example_3():
    assert TextJustification(max_width=20).get_justified_lines(
        words=[
            "Science",
            "is",
            "what",
            "we",
            "understand",
            "well",
            "enough",
            "to",
            "explain",
            "to",
            "a",
            "computer.",
            "Art",
            "is",
            "everything",
            "else",
            "we",
            "do",
        ],
    ) == [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  ",
    ]
