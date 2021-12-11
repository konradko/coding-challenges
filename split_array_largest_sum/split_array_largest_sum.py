def get_split_array_largest_sum(numbers: list[int], split_into: int) -> int:
    # Sub-array with the largest single element is the left boundary of split array largest sum range
    left = max(numbers)
    # Sub-array with all elements is the right boundary of the range
    right = sum(numbers)

    # Binary search
    while left <= right:
        middle = (left + right) // 2

        # Use greedy to narrow down boundaries
        if can_split(middle, numbers, split_into):
            right = middle - 1
        else:
            left = middle + 1

    return left


def can_split(middle: int, numbers: list[int], split_into: int) -> bool:
    split_counter = 1
    subarray_sum = 0

    for number in numbers:
        subarray_sum += number

        if subarray_sum > middle:
            subarray_sum = number
            split_counter += 1

            if split_counter > split_into:
                # Numbers were divied into more than requested number of subarrays
                return False

    return True
