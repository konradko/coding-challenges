def get_decoded_string(encoded_string: str):
    stack = []

    current_string = ""
    current_multiplier = ""

    for char in encoded_string:

        if char.isdigit():
            current_multiplier += char

        if char == "[":
            stack.append(current_string)
            stack.append(current_multiplier)

            current_string = ""
            current_multiplier = ""

        elif char.isalpha():
            current_string += char

        elif char == "]":
            last_multiplier = stack.pop()
            last_string = stack.pop()

            current_string = f"{last_string}{current_string * int(last_multiplier)}"

    return current_string
