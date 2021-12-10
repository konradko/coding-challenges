def get_longest_string_chain(words: list[str]) -> str:
    chain_length_per_word = {}

    for word in sorted(words, key=len):
        # A single word has chain length of 1
        chain_length = 1
        previous_chain_lengths = []

        for char_index in range(len(word)):
            chars_before = word[:char_index]
            chars_after = word[char_index + 1 :]

            # Get previous chain length
            if previous_chain_length := chain_length_per_word.get(f"{chars_before}{chars_after}"):
                previous_chain_lengths.append(previous_chain_length)

        if previous_chain_lengths:
            chain_length += max(previous_chain_lengths)

        chain_length_per_word[word] = chain_length

    return max(chain_length_per_word.values())
