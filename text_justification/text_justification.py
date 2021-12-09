class TextJustification:
    def __init__(self, max_width: int):
        self.max_width = max_width

    def get_justified_lines(self, words: list[str]) -> list[str]:
        justified_lines = []

        line: list[str] = []
        line_words_length = 0

        for word in words:
            word_length = len(word)
            line_length = len(line)

            if (word_length + line_length + line_words_length) > self.max_width:
                justified_lines.append(self.get_justified_line(line, line_length, line_words_length))

                line = []
                line_words_length = 0

            line.append(word)
            line_words_length += word_length

        # Justify last line
        justified_lines.append(" ".join(line).ljust(self.max_width))

        return justified_lines

    def get_justified_line(self, line: list[str], line_length: int, line_words_length: int):
        # Distribute spaces evenly through Round-robin
        for index in range(self.max_width - line_words_length):
            line[index % max(1, line_length - 1)] += " "

        return "".join(line)
